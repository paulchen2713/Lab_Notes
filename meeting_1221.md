# **meeting 12/21**
**Advisor: Dr. Chih-Yu Wang
Presenter: Shao-Heng Chen
Date: December 21, 2022**


## **Objectives**
- Run any newer versions of YOLO
  - currently trying to run [ScaledYOLOv4](https://github.com/WongKinYiu/ScaledYOLOv4)


## **Environment set up**
- New a separate virtual environment ```conda create -n v4 python=3.7```
  - Could run on the same env as YOLOv4
- Download the github repo [ScaledYOLOv4](https://github.com/WongKinYiu/ScaledYOLOv4) and rename the folder as ```YOLOv4-CSP```
![](https://i.imgur.com/9KHWBW4.png)
- Edit the ```requirements.txt``` as follow and install all the packages through ```pip install -r requirements.txt```
  - dependencies
    ```python!
    numpy==1.17.0
    opencv-python==4.6.0
    -f https://download.pytorch.org/whl/cu113/torch_stable.html
    torch==1.10.0+cu113
    -f https://download.pytorch.org/whl/cu113/torch_stable.html
    torchvision==0.11.1+cu113
    -f https://download.pytorch.org/whl/cu113/torch_stable.html
    torchaudio===0.10.0+cu113
    matplotlib==3.5.3
    pycocotools==2.0.6
    tqdm==4.64.1
    pillow==9.3.0
    tensorboard==2.11.0
    pyyaml==6.0
    scipy==1.7.3
    setuptools==59.5.0
    ```
- Get the pre-trained weights from somebody's google drive [yolov4-csp.weights](https://drive.google.com/u/0/uc?id=1TdKvDQb2QpP4EhOIyks8kgT8dgI1iOWT&export=download)
  - the pre-trained weights is around ```202MB```
  - put it in the same folder with ```train.py```, ```detect.py```, and ```test.py```
![](https://i.imgur.com/HwD8aNn.png)
- Put some sample images ```(*.jpg, *.png)``` or videos ```(*.mp4, *.mkv)``` that we want to test in the ```./data/samples/``` folder
  - We might need to new a ```sample``` folder on our own
  - And we can store the training and validation data in any folder we like, for instance, ```datasets1``` or ```datasets2```


## **Inference**
- Run ```detect.py``` in the terminal
  - single file inference (need to specified the name of the file, in this case it's called ```<example1.jpg>```): 
    - ```python detect.py --source data/samples/<example1.jpg> --cfg models/yolov4-csp.cfg --weights yolov4-csp.weights --conf 0.25 --img-size 640 --device 0```
  - multiple files inference (all the files in the ```sample``` folder): 
    - ```python detect.py --source data/samples --cfg models/yolov4-csp.cfg --weights yolov4-csp.weights --conf 0.25 --img-size 640 --device 0```
- Parameter settings:
  - ```--cfg``` 後面放參數設定的檔案路徑，e.g. ```cfg/yolov4.cfg```
  - ```--weights``` 後面放推論時讀取的 ```weight``` 檔案路徑，e.g. ```yolov4.weights```
  - ```--source``` 後面放要推論的圖片或資料夾路徑，e.g. ```data/samples```
  - ```--conf``` 後面放```confidence```的閾值，e.g. ```0.25```
  - ```--iou-thres``` 後面放```NMS```的閾值，e.g. 默認 ```0.5```
  - ```--img-size``` 待推論圖片輸入模型的尺寸，e.g. ```640```
  - ```--save_result``` 是否儲存圖片推論結果，e.g. ```True```
  - ```--device``` 指定推論```GPU```的編號，e.g. ```0```
- The output results will be stored at ```./inference/output/``` folder, and each time when we run ```detect.py```, the previous results will all be wash out
  - the outout file type will be the same as the one we inputed in, say we input a ```*.png``` image and the output images will also be a ```*.png``` file


## **Training**
- Train on ```COCO dataset``` with the annotations in ```YOLO .txt format```
  - ```[class_label x y w h]``` in relative scale
    - ```python train.py --batch-size 1 --img 640 640 --data coco.yaml --cfg models/yolov4-csp.cfg --weights yolov4-csp.weight --device 0 --name yolov4-csp --epochs 10 --notest``` (using pre-trained weights)
- Train on our ```CARRADA Dataset``` with the ```.txt``` annotations in three different format
  - ```Pascal_VOC format```: ```[class_label x_min y_min x_max y_max]``` in relative scale
  - ```COCO format```: ```[class_label x y w h]``` in absolute scale
  - ```YOLO format```: ```[class_label x y w h]``` in relative scale
- Run ```train.py``` in the terminal (using pre-trained weights)
  - ```python train.py --batch-size 1 --img 320 1280 --data D:/Datasets/YOLOv4-CSP/data/coco.yaml --cfg models/yolov4-csp.cfg --weights yolov4-csp.weight --device 0 --name yolov4-csp --epochs 10 --notest``` (with input dimension ```320 x 1280```)
  - ```python train.py --batch-size 1 --img 64 256 --data rdm.yaml --cfg models/yolov4-csp.cfg --weights yolov4-csp.weight --device 0 --name yolov4-csp --epochs 10 --notest``` (with input dimension ```64 x 256```)
- The hyper-paramenter settings are stored in ```hyp.scratch.yaml``` file
  - we need to put this ```.yaml``` file in the ```./data/``` folder
    ```python!
    lr0: 0.01  # initial learning rate (SGD=1E-2, Adam=1E-3)
    lrf: 0.2  # final OneCycleLR learning rate (lr0 * lrf)
    momentum: 0.937  # SGD momentum/Adam beta1
    weight_decay: 0.0005  # optimizer weight decay 5e-4
    warmup_epochs: 3.0  # warmup epochs (fractions ok)
    warmup_momentum: 0.8  # warmup initial momentum
    warmup_bias_lr: 0.1  # warmup initial bias lr
    box: 0.05  # box loss gain
    cls: 0.3  # cls loss gain
    cls_pw: 1.0  # cls BCELoss positive_weight
    obj: 0.7  # obj loss gain (scale with pixels)
    obj_pw: 1.0  # obj BCELoss positive_weight
    iou_t: 0.20  # IoU training threshold
    anchor_t: 4.0  # anchor-multiple threshold
    # anchors: 3  # anchors per output layer (0 to ignore)
    fl_gamma: 0.0  # focal loss gamma (efficientDet default gamma=1.5)
    hsv_h: 0.015  # image HSV-Hue augmentation (fraction)
    hsv_s: 0.7  # image HSV-Saturation augmentation (fraction)
    hsv_v: 0.4  # image HSV-Value augmentation (fraction)
    degrees: 0.0  # image rotation (+/- deg)
    translate: 0.1  # image translation (+/- fraction)
    scale: 0.9  # image scale (+/- gain)
    shear: 0.0  # image shear (+/- deg)
    perspective: 0.0  # image perspective (+/- fraction), range 0-0.001
    flipud: 0.0  # image flip up-down (probability)
    fliplr: 0.5  # image flip left-right (probability)
    mosaic: 1.0  # image mosaic (probability)
    mixup: 0.0  # image mixup (probability)
    ```
- Training results
![](https://i.imgur.com/ZeBatTF.png)
![](https://i.imgur.com/DJDg5h7.png)


## **Issues**
- It seems to be able to run ```train.py``` successfully, but unable to evalute the results through ```test.py```
![](https://i.imgur.com/n9Fi2BV.png)
- Originally I thought the issue is caused by annotation format, but it tuns out not to be that way 
  - because I manually checked the annotation format of the ```coco128 dataset```
  - and it's certainly not in the style of ```[class_label x_min y_min x_max y_max]```, it's actually ```[class_label x y w h]``` (in relative scale)


## **Some Progress**
- Rearranging the dataset, made it a single dataset
  - the total number of images: ```7193```
  - with two different scales: ```64 x 256``` and ```320 x 1280```
![](https://i.imgur.com/CaNzGig.png)


## **Appendix**
- ```resize_images.py```
```python=
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 18:30:27 2022

@author: Paul
@file: resize_images.py
@dependencies:
    env pt3.7
    python 3.7.13
    torch >= 1.7.1
    torchvision >= 0.8.2
    Pillow >= 8.1.0

Resize image to a certain size
"""
# import the required libraries
import torchvision.transforms as T # for resizing the images
from PIL import Image              # for loading and saving the images
import os
from os import listdir

# set the dataset path
DATASET = 'D:/Datasets/RADA/RD/'
DATASET2 = 'D:/Datasets/CARRADA2/'

CURR_PATH = 'D:/BeginnerPythonProjects/read_carrada/'

# directory names, number of directorie: 30
dir_names = ['2019-09-16-12-52-12', '2019-09-16-12-55-51', '2019-09-16-12-58-42', '2019-09-16-13-03-38', '2019-09-16-13-06-41', 
             '2019-09-16-13-11-12', '2019-09-16-13-13-01', '2019-09-16-13-14-29', '2019-09-16-13-18-33', '2019-09-16-13-20-20', 
             '2019-09-16-13-23-22', '2019-09-16-13-25-35', '2020-02-28-12-12-16', '2020-02-28-12-13-54', '2020-02-28-12-16-05', 
             '2020-02-28-12-17-57', '2020-02-28-12-20-22', '2020-02-28-12-22-05', '2020-02-28-12-23-30', '2020-02-28-13-05-44', 
             '2020-02-28-13-06-53', '2020-02-28-13-07-38', '2020-02-28-13-08-51', '2020-02-28-13-09-58', '2020-02-28-13-10-51', 
             '2020-02-28-13-11-45', '2020-02-28-13-12-42', '2020-02-28-13-13-43', '2020-02-28-13-14-35', '2020-02-28-13-15-36']

# number of images / labels in each directory, total number of labels: 7193
num_of_images = [286, 273, 304, 327, 218, 219, 150, 208, 152, 174, 
                 174, 235, 442, 493, 656, 523, 350, 340, 304, 108, 
                 129, 137, 171, 143, 104, 81, 149, 124, 121, 98]

# e.g. read "validated_seqs.txt"
def read_txt_file(file_name=""):
    dir_names = list()
    with open(DATASET + file_name, "r") as seqs_file:
        dir_names = seqs_file.read().splitlines()
    return dir_names
# temp = read_txt_file("validated_seqs.txt")


def resize_to_64_256():
    count = 1
    for dir_name in dir_names: # [23:24]: # 
        print(f"current directory: {dir_name}")

        # set the file path
        seq_path = DATASET + dir_name + '/images/'
        print(f"current seq path: {seq_path}")

        for images in os.listdir(seq_path):
            # check if the image ends with png
            if (images.endswith(".png")):
                # print(count, seq_path + images)

                # read the input image
                img = Image.open(seq_path + images)

                # # compute the size (width, height) of image
                # before = img.size
                # print(f"original image size: {before}")

                # define the transform function to resize the image with given size
                transform = T.Resize(size=(256, 64))

                # apply the transform on the input image
                img = transform(img)

                # # check the size (width, height) of image
                # after = img.size
                # print(f"resized image size: {after}")

                # overwrite the original image with the resized one
                img = img.save(f'D:/Datasets/RADA/RD_all/images/{count}.png')
                
                print(count)
                count += 1


if __name__ == '__main__':
    # testing(1, 'jpg')
    # main(1600, 'jpg')
    resize_to_64_256()
```
- ```convert_label.py```
```python=
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 17:17:12 2022

@patch: 
    2022.10.30
    2022.12.20
@author: Paul
@file: convert_label.py
@dependencies:
    envs        pt3.7
"""

import json
import time

# set the dataset path
DATASET = 'D:/Datasets/CARRADA/'
DATASET2 = 'D:/Datasets/CARRADA2/'

# directory names, number of directorie: 30
dir_names = ['2019-09-16-12-52-12', '2019-09-16-12-55-51', '2019-09-16-12-58-42', '2019-09-16-13-03-38', '2019-09-16-13-06-41', 
             '2019-09-16-13-11-12', '2019-09-16-13-13-01', '2019-09-16-13-14-29', '2019-09-16-13-18-33', '2019-09-16-13-20-20', 
             '2019-09-16-13-23-22', '2019-09-16-13-25-35', '2020-02-28-12-12-16', '2020-02-28-12-13-54', '2020-02-28-12-16-05', 
             '2020-02-28-12-17-57', '2020-02-28-12-20-22', '2020-02-28-12-22-05', '2020-02-28-12-23-30', '2020-02-28-13-05-44', 
             '2020-02-28-13-06-53', '2020-02-28-13-07-38', '2020-02-28-13-08-51', '2020-02-28-13-09-58', '2020-02-28-13-10-51', 
             '2020-02-28-13-11-45', '2020-02-28-13-12-42', '2020-02-28-13-13-43', '2020-02-28-13-14-35', '2020-02-28-13-15-36']

# number of images / labels in each directory, total number of labels: 7193
num_of_images = [286, 273, 304, 327, 218, 219, 150, 208, 152, 174, 
                 174, 235, 442, 493, 656, 523, 350, 340, 304, 108, 
                 129, 137, 171, 143, 104, 81, 149, 124, 121, 98]

# e.g. read "validated_seqs.txt"
def read_txt_file(file_name=""):
    dir_names = list()
    with open(DATASET + file_name, "r") as seqs_file:
        dir_names = seqs_file.read().splitlines()
    return dir_names

def main():
    dir_names = read_txt_file("validated_seqs.txt")

    for dir_name in dir_names: # [23:24]: # 
        # e.g. "D:/Datasets/CARRADA/2019-09-16-12-58-42/annotations/box/"
        print(f"current directory: {dir_name}")

        # "range_doppler_light.json", "range_angle_light.json"
        file_index = ["range_doppler_light.json", "range_angle_light.json"]
        with open(DATASET + f"{dir_name}/annotations/box/" + f"{file_index[0]}", "r") as json_file:
        # with open(CURR_PATH + "range_doppler_light.json", "r") as json_file:
            """
            # there are two ways to read json file
            # data = json.load(json_file)         # one using json.load(), which load the json_file
            # data = json.loads(json_file.read()) # make sure you add ".read()" when using json.loads(), the "s" means string
            """
            data = json.loads(json_file.read())
            # print(type(data)) # <class 'dict'>

        # extract all keys from the dict, and store them in a list()
        all_keys = list(data.keys())
        # print(data[f"{all_keys[0]}"]["boxes"])  # [[69, 32, 72, 35]] <class 'list'>
        # print(data[f"{all_keys[0]}"]["labels"]) # [1] <class 'list'>
        
        for key in all_keys: # [62:63]: # 
            print(f"frame name: \"{key}\"")

            # paths of RD_maps and RA_maps
            RDM_PATH = f"D:/Datasets/CARRADA2/RD_Pascal_VOC/{dir_name}/labels/" # path that we store our labels
            RAM_PATH = f"D:/Datasets/CARRADA2/RA/{dir_name}/labels/" # path that we store our labels

            # we have to set 2 different paths of 'RDM_PATH' or 'RAM_PATH',
            # 2 different data types of 'RDM' or 'RAM', and
            # 3 different output annotation types of 'Pascal_VOC', 'COCO' or 'YOLO'
            def store_labels(data_path=f'{RDM_PATH}', data_type='RDM', out_type='YOLO', mode='', store=True):
                with open(data_path + f"0000_log_{dir_name}.txt", "a") as label_txt_file:
                    print(f"{data[key]}", file=label_txt_file)
                if mode == 'debug':
                    print(f"num of boxes: {len(data[key]['boxes'])}")
                    print(f"num of labels: {len(data[key]['labels'])}")

                if (len(data[key]['boxes']) != len(data[key]['labels'])): 
                    print("boxes and labels are mismatched!")

                with open(data_path + f"{key}.txt", "w") as label_txt_file:
                    # in each rd_matrix / image it may contain 1~3 possible targets
                    for index in range(0, len(data[key]['boxes'])):
                        class_index = data[key]['labels'][index] - 1
                        if mode == 'debug':
                            print(data[key]['boxes'][index])
                            print(data[key]['labels'][index])
                            print(f"class_index = {class_index}")
                        
                        # [x, y, width, height] is COCO format in absolute scale
                        # [x_min, y_min, x_max, y_max] is Pascal_VOC format in absolute scale
                        x_min, y_min, x_max, y_max = data[key]['boxes'][index][0:4]   # extract Pascal_VOC / COCO format in absolute scale
                        if mode == 'debug':
                            print(f"(class, x_min, y_min, x_max, y_max) = ({class_index} {x_min} {y_min} {x_max} {y_max})")

                        if out_type == 'YOLO':
                            """
                            make sure it's [class_id, x, y, width, height] in relative scale
                            """
                            x, y = (x_max + x_min) / 2, (y_max + y_min) / 2
                            w, h = (y_max - y_min), (x_max - x_min)
                            if data_type == 'RDM':
                                x, y, w, h = x / 256, y / 64, w / 64, h / 256 # RD map, convert from COCO format to YOLO format in relative scale
                            elif data_type == 'RAM':
                                x, y, w, h = x / 256, y / 256, w / 256, h / 256 # RA map
                            
                            if mode == 'debug':
                                print(f"(class, x, y, w, h) = ({class_index}, {x}, {y}, {w}, {h}) in relative scale")

                            if store == True:
                                print(f"{class_index} {x} {y} {w} {h}", file=label_txt_file) # redirect 'print()' output to a file
                        elif out_type == 'COCO':
                            """
                            make sure it's [class_id, x, y, width, height] in absolute value
                            """
                            x, y = (x_max + x_min) / 2, (y_max + y_min) / 2
                            w, h = (y_max - y_min), (x_max - x_min)

                            if mode == 'debug':
                                print(f"(class, x, y, w, h) = ({class_index}, {x}, {y}, {w}, {h}) in absolute value")
                            
                            if store == True:
                                print(f"{class_index} {x} {y} {w} {h}", file=label_txt_file) # redirect 'print()' output to a file
                        elif out_type == 'Pascal_VOC':
                            """
                            make sure it's [class_id, x_min, y_min, x_max, y_max] in relative scale
                            """
                            if data_type == 'RDM':
                                x_min, y_min, x_max, y_max = x_min / 256, y_min / 64, x_max / 256, y_max / 64
                            elif data_type == 'RAM':
                                x_min, y_min, x_max, y_max = x_min / 256, y_min / 256, x_max / 256, y_max / 256
                            
                            if mode == 'debug':
                                print(f"(class, x_min, y_min, x_max, y_max) = ({class_index} {x_min} {y_min} {x_max} {y_max}) in relative scale")
                            
                            if store == True:
                                print(f"{class_index} {x_min} {y_min} {x_max} {y_max}", file=label_txt_file) # redirect 'print()' output to a file
                        # print("---------------------------")
            
            # call out store_labels function to extract the labels that we need
            store_labels(
                data_path=RDM_PATH,     # data_path=RDM_PATH or RAM_PATH
                data_type='RDM',        # data_type='RDM' or 'RAM'
                out_type='Pascal_VOC',  # out_type='YOLO', 'COCO' or 'Pascal_VOC'
                mode='',                # mode='debug' # means print everything out
                store=True              # store=True # means renew the .txt label, visa vera
            ) 
            

if __name__ == '__main__':
    tic = time.perf_counter()
    main()
    toc = time.perf_counter()
    duration = toc - tic
    print(f"duration: {duration:0.4f} seconds") 
    print(duration)
    # rd_matrix duration: 4.6774586 seconds
    # ra_matrix duration: 4.3379489 seconds
```



## **Reference**
- [Scaled YOLOv4 training on local machine (Windows)](https://ithelp.ithome.com.tw/m/articles/10304999)

