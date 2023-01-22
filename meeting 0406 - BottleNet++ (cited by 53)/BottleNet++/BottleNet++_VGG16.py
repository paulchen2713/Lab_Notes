import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from torchvision import transforms
from torchvision.utils import save_image
from compression_module import *
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedShuffleSplit
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-channel', type=str, default='a', help='channel type, using \'a\' as AWGN and \'e\' as BEC ')
parser.add_argument('-noise', type=float, default=0.1, help='channel condition')
parser.add_argument('-hid_dim', type=int, default=32, help='lens of encoded vector')
parser.add_argument('-in_dim', type=int, default=512, help='input dimension')
parser.add_argument('-div_position', type=int, default=13, help='divide the layer')
#parser.add_argument('-sub_div_position', type=int, default=1, help='sub_divide the layer')
parser.add_argument('-spatial', type=int, default=0, help='compress feature map')
parser.add_argument('-epoch', type=int, default=70, help='epoch')
parser.add_argument('-batch', type=int, default=32, help='batch size')
parser.add_argument('-phase', type=int, default=2, help='phase = 1,2,3, means to different training phase')
parser.add_argument('-lr', type=float, default=1e-4, help='leaerning rate')
args = parser.parse_args()

print('splitting point:',str(args.div_position),'input dim:',args.in_dim,'encoded dim',args.hid_dim,'spatial shrink:',args.spatial)
print('channel model:',args.channel,'channel condition:',args.noise)
print('phase:',args.phase,'epoch:',args.epoch,'batch:',args.batch,'learning rate:',args.lr)


# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                     std=[0.229, 0.224, 0.225])
'''
normalize = transforms.Normalize(mean=[0.5070751592371323, 0.48654887331495095, 0.4409178433670343],
                                     std=[0.2673342858792401, 0.2564384629170883, 0.27615047132568404])                                     
'''

test_set_this = torchvision.datasets.CIFAR100(root='../../CIFAR100', train=False, transform=transforms.Compose([
            transforms.ToTensor(),
            normalize,
        ]), download=True)
        
test_loader_this = torch.utils.data.DataLoader(test_set_this,
        batch_size=batch_size, shuffle=False,
        num_workers=4, pin_memory=True)
        
class BottleNetPlusPlus_VGG(nn.Module):
    def __init__(self,input_channel = args.in_dim, hidden_channel = args.hid_dim, noise = args.noise, channel = args.channel,div_position = args.div_position,spatial =args.spatial):
        super(BottleNetPlusPlus_VGG, self).__init__()

        self.vgg_model = torch.load('vgg16_74.02.pth')
        self.vgg_model.features = self.vgg_model.features.module
        self.div_position = args.div_position


        for para in self.vgg_model.parameters():
            if args.phase == 2:
                para.requires_grad = False
            elif args.phase ==1 or 3:
                para.requires_grad = True

        

        self.compression_module = compression_module(input_channel = input_channel , hidden_channel = hidden_channel,noise = noise,channel = channel, spatial = spatial)
        

    
    def forward(self, x):
    
        insert_vae_flag = 0
        #insert_list=[43,33,23,13,6]
        insert_list=[2,6,9,13,16,19,23,26,29,33,36,39,43]
        insert_vae_flag = insert_list[args.div_position - 1]
            
    
        for i in range (len(list(self.vgg_model.features))):
            x = list(self.vgg_model.features)[i](x)
            if i==insert_vae_flag:
                x = self.compression_module(x)
            
        x = x.view(-1,512)
        #print('cla',x.size())
        x =self.vgg_model.classifier(x)
        return x

        
model = BottleNetPlusPlus_VGG().to(device)
#model = torch.nn.DataParallel(model)
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

def accuracy(output, labels):
    preds = output.max(1)[1].type_as(labels)
    
    correct = preds.eq(labels).double()
    correct = correct.sum()

    return correct / len(labels)

# Start training
def train(model=model):

    for epoch in range(num_epochs):
        if (epoch)%10 == 0:
            train_set = torchvision.datasets.CIFAR100(root='../CIFAR100', train=True, transform=transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.RandomCrop(32, 4),
            transforms.ToTensor(),
            normalize,
        ]), download=True)
            data_loader = torch.utils.data.DataLoader(train_set,batch_size=batch_size, shuffle=True,
        num_workers=4, pin_memory=True)
        
        
        for i, (x, y) in enumerate(data_loader):
        
            if (i+epoch)==0:
                print('load model')
                
            x = x.to(device)
            y = y.to(device)

            model.train()
            output = model(x)

            # Backprop and optimize
            criterion = nn.CrossEntropyLoss()
            criterion = criterion.to(device)
            loss = criterion(output, y)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            accuracy_result = accuracy(output,y)
            
            if (i+1) % int(50000/(args.batch*20)) == 0:
                print ("Epoch[{}/{}], Step [{}/{}], Reconst Loss: {:.4f}, acc: {:.4f}" 
                       .format(epoch+1, num_epochs, i+1, len(data_loader), loss.item(), accuracy_result.item()))
                torch.save(model,'BottleNetPlusPlus_VGG.pkl')
                
        
        if (epoch)%3 == 0:
            test(epoch)
            
        
def test(epoch):
    with torch.no_grad():
        model.eval()

        correct = 0
        correct_top5 = 0#top5
        total = 0

        for i, (images, labels) in enumerate(test_loader_this): 
            images = images.to(device)
            labels = labels.to(device)
            outputs= model(images)
            maxk = max((1,5))
            labels_relize = labels.view(-1,1)
            _, top5_pred = outputs.topk(maxk, 1, True, True)
            
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct_top5 +=torch.eq(top5_pred, labels_relize).sum().float().item()
            correct += (predicted == labels).sum().item()
            #print('['+str(total)+'/10000]',(100 * correct / total))
            
        if (100 * correct / total) > 60:
                pred_best = (100 * correct / total)
                torch.save(model,args.channel+'_div:'+str(args.div_position)+'_spatial:_'+str(args.spatial)+'_hid:'+str(args.hid_dim)+'_noise:'+str(args.noise)+'_acc{:.4f}_top5:{:.4f}_'.format((100 * correct / total),(100 *correct_top5/total))+'epoch:'+str(epoch)+'.pkl')
        print('Accuracy of the network on the 10000 test images: {} %'.format(100 * correct / total),'top5: {} %'.format(100* correct_top5/total))



def adjust_learning_rate(optimizer, epoch):
    lr = 0.001 * (0.5 ** (epoch // 10))
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr


      
if __name__=='__main__':
    train()
