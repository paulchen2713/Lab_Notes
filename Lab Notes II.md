
# **Lab Notes II**








## **06/07**
- 2023.06.07
  - ```6-fold validation``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 15e-5``` under ```100``` epochs




## **06/06**
- 2023.06.06
  - write a ```read_camera.py``` to extract camera images
    ![](https://hackmd.io/_uploads/HkSZc838h.png)
  - the camera results
    ![](https://hackmd.io/_uploads/B1Iej83Uh.png)
  - some issues
    - e.g. the RD maps of ```6373-6375```
    ![](https://hackmd.io/_uploads/r1y1TInU2.jpg)
    - the camera images of ```6373-6375```
    ![](https://hackmd.io/_uploads/HysBTInLn.jpg)



## **05/30**
- 2023.05.30
  - write a ```test()``` to see the prediction results of every validation sample
    ![](https://hackmd.io/_uploads/H1lHqGmL3.png)
    ![](https://hackmd.io/_uploads/BkJiFMQU3.png)
    ![](https://hackmd.io/_uploads/ByBIszQU2.png)
  - Preliminary results
    ![](https://hackmd.io/_uploads/Hkn02z7I2.png)
  - e.g. ```6375.jpg``` with label: ```0 0.515625 0.26953125 0.046875 0.01171875```
      <img src = 'https://hackmd.io/_uploads/Bk5I8Qm8n.jpg' width = 40% height = 40%>
  - from ```6373-6375``` with labels:
    - ```[0 0.468750 0.28515625 0.046875 0.01171875]```, 
    - ```[0 0.515625 0.27343750 0.046875 0.01171875]```, 
    - ```[0 0.515625 0.26953125 0.046875 0.01171875]```.
    ![](https://hackmd.io/_uploads/r1K0DQQL2.jpg)
- some issues
  - ```228 / 600 = 38%``` of the predictions are actually ```'empty'```. If we set a higher threshold for ```'normal'```, then the ratio would be even higher
    - cause normally we hope to set the accuracy bar at least ```50.0000```
  - there are ```228``` samples with ```object_accuracy: 0.0000```
    - ```199``` samples with ```object_accuracy: 33.3333```
    - ```26``` samples with ```object_accuracy: 16.6667```
    - ```70``` samples with ```object_accuracy: 50.0000``` 
  - there are in total ```523``` bad results




## **05/23**
- 2023.05.23
  - Need to figure out which part the model performed bad ASAP
  - Need to determine the specific types or categories of "basic augmentations" that are considered acceptable or valid
    - Additionally, these augmentations should not contradict or violate the rules of physics when implemented



## **05/22**
- 2023.05.22
  - Install required packages for ```tensorboard```
    - [tensorboard](https://anaconda.org/conda-forge/tensorboard) ```conda install -c conda-forge tensorboard```
    - [torch-tb-profiler](https://pypi.org/project/torch-tb-profiler/) ```pip install torch-tb-profiler```
  - Dependency for Lab PC ```pt3.8```
    - tensorboard
        ```clike
        tensorboard==2.10.0
        tensorboard-data-server==0.6.1
        tensorboard-plugin-wit==1.8.1
        ```
    - PyTorch Profiler TensorBoard
        ```clike
        torch-tb-profiler==0.4.1
        ```
  - Dependency for My PC ```pt3.7```




## **05/20**
- 2023.05.20
  - looking into researching synthetic methods like GANs to increase the size of my training set in an unsupervised manner
    - maybe we can use conditional GANs for synthesizing data with labels/bounding boxes
    - Keras [Conditional GAN](https://keras.io/examples/generative/conditional_gan/)
  - M. Hammami, D. Friboulet and R. Kechichian, "[Cycle GAN-Based Data Augmentation For Multi-Organ Detection In CT Images Via Yolo](https://ieeexplore.ieee.org/abstract/document/9191127)," *2020 IEEE International Conference on Image Processing (ICIP)*, Abu Dhabi, United Arab Emirates, 2020, pp. 390-393.
  - Search Results for "[GAN for data augmentation](https://paperswithcode.com/search?q_meta=&q_type=&q=GAN+for+data+augmentation)" on paper with code



<!-- 
## **05/12**
- 2023.05.12
  - The training  -->




## **05/11**
- 2023.05.11
  - The training duration is ```13.2833 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 15e-5```
    - Under ```200``` epochs
    - Strike a new new high ```max mAP:  0.4755```
    ```shell
    --------------------------------------------------
    The stats of 2023-05-11-1 training: 
    --------------------------------------------------
    max mAP:  0.4755074977874756
    mean mAP: 0.4086848013103008

    max training loss: 332.6708984375
    min training loss: 0.7371702194213867

    max training loss on average: 17.663408323923747
    min training loss on average: 1.0476918365557988

    min training accuracy: 2.8955674171447754
    max training accuracy: 96.7979507446289

    min testing accuracy: 33.447410583496094
    max testing accuracy: 72.30207061767578
    --------------------------------------------------
    ```


## **05/10**
- 2023.05.10
  - Some blogs for deep learning basics, but I haven't studied it yet
    - cccbook / [py2cs](https://github.com/cccbook/py2cs/tree/master/03-%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7) by 陳鍾誠教授, 國立金門大學 資訊工程學系
    - Andrej Karpathy blog [Hacker's guide to Neural Networks](http://karpathy.github.io/neuralnets/?fbclid=IwAR2z-tnZ185hsxg3wabLvlV29Zr53Q_sVJs1tNhUzlw0CTl7Z68r1EJtq0o) in ```javascript```
    - Andrej Karpathy blog [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/?fbclid=IwAR0pkk7kd-lxixV00lWbtHx7wnYRRgvb26exg0YzUmi0mpjKKBUrWX32LY8)



## **05/09**
- 2023.05.09
  - The training duration is ```22.8276 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 14e-5```
    - Under ```300``` epochs
    - Try to observe the difference between training directly for ```200``` epochs versus the combination of separate training for ```100``` epochs each 
    ```
    --------------------------------------------------
    The stats of 2023-05-09-1 training:
    --------------------------------------------------
    max mAP:  0.4652663767337799
    mean mAP: 0.41992816428343455

    max training loss: 120.43387603759766
    min training loss: 0.7253801822662354

    max training loss on average: 15.41774600982666
    min training loss on average: 0.9773107906182606

    min training accuracy: 2.3786652088165283
    max training accuracy: 97.95069122314453

    min testing accuracy: 35.47798538208008
    max testing accuracy: 72.39334106445312
    --------------------------------------------------
    ```



## **05/08**
- 2023.05.08
  - The training duration is ```14.2820 hours``` with higher ```WEIGHT_DECAY = 1e-3``` and ```LEARNING_RATE = 15e-5```
    - Under ```200``` epochs and higher weight decay setting
    - Try to see how the previous best learning rate goes with higher weight decay
    ```
    --------------------------------------------------
    The stats of 2023-05-08-1 training: 
    --------------------------------------------------
    max mAP:  0.42102280259132385
    mean mAP: 0.37317809015512465

    max training loss: 174.62034606933594
    min training loss: 1.0440865755081177

    max training loss on average: 17.338274812698366
    min training loss on average: 1.3041423439979554

    min training accuracy: 0.4254150986671448
    max training accuracy: 92.8823013305664

    min testing accuracy: 34.81633758544922
    max testing accuracy: 69.26762390136719
    --------------------------------------------------
    ```
    ![](https://hackmd.io/_uploads/S1AfaBD43.png)
- Using ```torchinfo.summary()``` to get the result
  - The second way to get model summary in PyTorch besides ```torchsummary.summary()```
  - sample code
    ```python
    import torchsummary            # torchsummary.summary()
    from torchinfo import summary  # torchinfo.summary()

    # simple test settings
    IMAGE_SIZE = 416  # multiples of 32 are workable with stride [32, 16, 8]
    num_classes = 3   # 
    batch_size = 20   # num_examples
    num_channels = 3  # num_anchors

    model = YOLOv3(num_classes=num_classes) # initialize a YOLOv3 model as model

    # simple test with random inputs of 20 examples, 3 channels, and IMAGE_SIZE-by-IMAGE_SIZE input
    x = torch.randn((batch_size, num_channels, IMAGE_SIZE, IMAGE_SIZE))

    out = model(x)

    # print out the model summary using torchinfo.summary()
    summary(model.cuda(), input_size=(batch_size, num_channels, IMAGE_SIZE, IMAGE_SIZE))
    ```
  - model parameter summary
    ```clike
    ====================================================================================================
    Total params: 61,534,648
    Trainable params: 61,534,648
    Non-trainable params: 0
    Total mult-adds (G): 653.05
    ====================================================================================================
    Input size (MB): 41.53
    Forward/backward pass size (MB): 12265.99
    Params size (MB): 246.14
    Estimated Total Size (MB): 12553.66
    ====================================================================================================
    ```


## **05/07**
- 2023.05.07
  - The training duration is ```8.3639 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 14e-5```
    - Still ```100``` epochs
    - Continued the training with the weights of ```checkpoint-2023-05-02-2.pth.tar``` with same weight decay and learning rate
    ```
    --------------------------------------------------
    The stats of 2023-05-07-1 training:
    --------------------------------------------------
    max mAP:  0.44356226921081543
    mean mAP: 0.42320117354393005

    max training loss: 4.268791675567627
    min training loss: 0.8072612285614014

    max training loss on average: 2.3641905311743416
    min training loss on average: 1.0348780262470245

    min training accuracy: 68.03897857666016
    max training accuracy: 96.88028717041016

    min testing accuracy: 59.59388732910156
    max testing accuracy: 67.21424102783203
    --------------------------------------------------
    ```
    ![](https://hackmd.io/_uploads/H1GT2zI4n.png)



## **05/06**
- 2023.05.06
  - The training duration is ```8.7493 hours``` with higher weight decay of ```WEIGHT_DECAY = 1e-3``` and ```LEARNING_RATE = 14e-5``` 
    - Switching back to ```100``` epochs
    - Continued the training with the weights of ```checkpoint-2023-05-02-2.pth.tar``` (with ```WEIGHT_DECAY = 1e-4```)
    ```
    --------------------------------------------------
    The stats of 2023-05-06-1 training:
    --------------------------------------------------
    max mAP:  0.4469827115535736
    mean mAP: 0.41541612446308135

    max training loss: 7.434675216674805
    min training loss: 0.8201318383216858

    max training loss on average: 5.396891689300537
    min training loss on average: 1.0210446101427078

    min training accuracy: 65.16170501708984
    max training accuracy: 96.99007415771484

    min testing accuracy: 49.76043701171875
    max testing accuracy: 65.93656921386719
    --------------------------------------------------
    ```
    ![](https://hackmd.io/_uploads/By_I1zUN3.png)



## **05/05**
- 2023.05.05
  - The training duration is ```26.4082 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 15e-5``` 
    - Switching up to ```400``` epochs
    ```
    --------------------------------------------------
    The stats of 2023-05-05-1 training: 
    --------------------------------------------------
    max mAP:  0.4396911561489105
    mean mAP: 0.4000327423214912

    max training loss: 171.85177612304688
    min training loss: 0.6924741864204407

    max training loss on average: 15.746856501897176
    min training loss on average: 0.9486591788132985

    min training accuracy: 3.29353666305542
    max training accuracy: 97.90494537353516

    min testing accuracy: 34.040611267089844
    max testing accuracy: 74.72051239013672
    --------------------------------------------------
    ```
    ![](https://hackmd.io/_uploads/rJAy0W8E2.png)




## **05/04**
- 2023.05.04
  - The training duration is ```7.4228 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 19e-5```
    ```
    --------------------------------------------------
    The stats of 2023-05-04-1 training: 
    --------------------------------------------------
    max mAP:  0.44310665130615234
    mean mAP: 0.38241996318101884

    max training loss: 124.89086151123047
    min training loss: 1.0636780261993408

    max training loss on average: 16.811252358754476
    min training loss on average: 1.2993631919225057

    min training accuracy: 2.063034772872925
    max training accuracy: 92.96463775634766

    min testing accuracy: 31.75906753540039
    max testing accuracy: 70.13461303710938
    --------------------------------------------------
    ```
  - The training duration is ```8.4733 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 20e-5```
    ```
    --------------------------------------------------
    The stats of 2023-05-04-2 training: 
    --------------------------------------------------
    max mAP:  0.4227812588214874
    mean mAP: 0.34420192539691924

    max training loss: 138.41775512695312
    min training loss: 1.0614862442016602

    max training loss on average: 15.212103751500448
    min training loss on average: 1.326857070128123

    min training accuracy: 5.338273525238037
    max training accuracy: 93.10186767578125

    min testing accuracy: 31.074607849121094
    max testing accuracy: 69.54141235351562
    --------------------------------------------------
    ```



## **05/03**
- 2023.05.03
  - The training duration is ```7.1341 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 17e-5```
    ```
    --------------------------------------------------
    The stats of 2023-05-03-1 training: 
    --------------------------------------------------
    max mAP:  0.4469388425350189
    mean mAP: 0.3841908037662506

    max training loss: 113.7841567993164
    min training loss: 0.963789165019989

    max training loss on average: 15.0015398200353
    min training loss on average: 1.2312769017616907

    min training accuracy: 7.767257213592529
    max training accuracy: 94.10365295410156

    min testing accuracy: 33.51585388183594
    max testing accuracy: 69.63267517089844
    --------------------------------------------------
    ```
  - The training duration is ```7.1676 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 18e-5```
    ```
    --------------------------------------------------
    The stats of 2023-05-03-2 training: 
    --------------------------------------------------
    max mAP:  0.44689252972602844
    mean mAP: 0.3790498897433281

    max training loss: 175.32229614257812
    min training loss: 1.0493061542510986

    max training loss on average: 17.080741675694785
    min training loss on average: 1.291623563369115

    min training accuracy: 7.433328628540039
    max training accuracy: 93.3305892944336

    min testing accuracy: 34.49692153930664
    max testing accuracy: 70.79625701904297
    --------------------------------------------------
    ```



## **05/02**
- 2023.05.02
  - The training duration is ```6.8200 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 13e-5```
    ```
    --------------------------------------------------
    The stats of 2023-05-02-1 training:
    --------------------------------------------------
    max mAP:  0.4374929666519165
    mean mAP: 0.3631990686058998

    max training loss: 134.36065673828125
    min training loss: 0.9601410627365112

    max training loss on average: 18.045101165771484
    min training loss on average: 1.2157120569547017

    min training accuracy: 2.877269983291626
    max training accuracy: 94.9224624633789

    min testing accuracy: 42.20853042602539
    max testing accuracy: 70.84188842773438
    --------------------------------------------------
    ```
  - The training duration is ```5.8219 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 14e-5```
    ```
    --------------------------------------------------
    The stats of 2023-05-02-2 training: 
    --------------------------------------------------
    max mAP:  0.452169269323349
    mean mAP: 0.3887074992060661

    max training loss: 135.23342895507812
    min training loss: 0.9823306798934937

    max training loss on average: 16.633436683019003
    min training loss on average: 1.268118454615275

    min training accuracy: 3.00077748298645
    max training accuracy: 94.62512969970703

    min testing accuracy: 30.800823211669922
    max testing accuracy: 73.10061645507812
    --------------------------------------------------
    ```
  - The training duration is ```5.5819 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 15e-5```
    ```
    --------------------------------------------------
    The stats of 2023-05-02-3 training: 
    --------------------------------------------------
    max mAP:  0.45209288597106934
    mean mAP: 0.3701558232307434

    max training loss: 217.28318786621094
    min training loss: 1.000074863433838

    max training loss on average: 16.713819392522176
    min training loss on average: 1.2200019482771556

    min training accuracy: 5.814006328582764
    max training accuracy: 94.16769409179688

    min testing accuracy: 41.84348678588867
    max testing accuracy: 69.8380126953125
    --------------------------------------------------
    ```
  - The training duration is ```8.4758 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 16e-5```
    ```
    --------------------------------------------------
    The stats of 2023-05-02-4 training: 
    --------------------------------------------------
    max mAP:  0.43429771065711975
    mean mAP: 0.3629924669861794

    max training loss: 178.13705444335938
    min training loss: 0.9736015796661377

    max training loss on average: 16.70783141930898
    min training loss on average: 1.2728607519467672

    min training accuracy: 6.477288246154785
    max training accuracy: 93.60047912597656

    min testing accuracy: 21.12708282470703
    max testing accuracy: 72.98653411865234
    --------------------------------------------------
    ```
- The comparison between different ```LEARNING_RATE``` under the same ```WEIGHT_DECAY = 1e-4```
  - The ```loss``` value for every updates
    ![](https://i.imgur.com/cOoZd7K.png)
  - The ```train-object-accuracy``` for every epochs
    ![](https://i.imgur.com/H7ymC2V.png)
  - The ```test-object-accuracy``` for every ```10``` epochs
    ![](https://i.imgur.com/vwLXQYD.png)
  - The ```mAP``` for every ```10``` epochs 
    ![](https://i.imgur.com/WxKZwJM.png)
- The training time comparison
  - The training duration with different weight decay
    ![](https://i.imgur.com/mHUL8jJ.png)
  - The training duration with different learning rate
    ![](https://i.imgur.com/9EF6Bw4.png)
- The training logs
    ```cpp
    2023-05-02-1  epoch: 100   duration:  6.8200 hours  WEIGHT_DECAY = 1e-4  LEARNING_RATE = 13e-5  max mAP:  0.4374
    2023-05-01-3  epoch: 100   duration:  7.1689 hours  WEIGHT_DECAY = 1e-4  LEARNING_RATE = 12e-5  max mAP:  0.4372
    2023-05-01-2  epoch: 100   duration:  7.0366 hours  WEIGHT_DECAY = 1e-4  LEARNING_RATE = 11e-5  max mAP:  0.4490
    2023-05-01-1  epoch: 100   duration:  5.7350 hours  WEIGHT_DECAY = 1e-4  LEARNING_RATE = 10e-5  max mAP:  0.4386
    2023-04-30-2  epoch: 100   duration:  5.5800 hours  WEIGHT_DECAY = 1e-4  LEARNING_RATE = 9e-5   max mAP:  0.4356
        
    2023-04-30-1  epoch: 100   duration:  6.7780 hours  WEIGHT_DECAY = 1e-4  LEARNING_RATE = 8e-5   max mAP:  0.4340
    2023-04-29-2  epoch: 100   duration:  7.1015 hours  WEIGHT_DECAY = 1e-4  LEARNING_RATE = 7e-5   max mAP:  0.4309
    2023-04-29-1  epoch: 100   duration:  7.0542 hours  WEIGHT_DECAY = 1e-4  LEARNING_RATE = 6e-5   max mAP:  0.4267
    2023-04-28-3  epoch: 100   duration:  7.1785 hours  WEIGHT_DECAY = 1e-4  LEARNING_RATE = 5e-5   max mAP:  0.4143
    2023-04-28-2  epoch: 100   duration:  8.1383 hours  WEIGHT_DECAY = 1e-4  LEARNING_RATE = 4e-5   max mAP:  0.3963

    2023-04-22    epoch: 100   duration:  7.2117 hours  WEIGHT_DECAY = 1e-4  LEARNING_RATE = 3e-5   max mAP:  0.3792
    2023-04-27-2  epoch: 100   duration:  7.2838 hours  WEIGHT_DECAY = 1e-4  LEARNING_RATE = 2e-5   max mAP:  0.3233
    2023-04-28    epoch: 100   duration:  7.5511 hours  WEIGHT_DECAY = 1e-4  LEARNING_RATE = 1e-5   max mAP:  0.2697

    2023-04-27    epoch: 100   duration:  7.1676 hours  WEIGHT_DECAY = 1e-1  LEARNING_RATE = 3e-5   max mAP:  0.3289
    2023-04-26    epoch: 100   duration:  7.7900 hours  WEIGHT_DECAY = 1e-2  LEARNING_RATE = 3e-5   max mAP:  0.3646
    2023-04-25    epoch: 100   duration:  6.2753 hours  WEIGHT_DECAY = 1e-3  LEARNING_RATE = 3e-5   max mAP:  0.3603
    2023-04-22    epoch: 100   duration:  7.2117 hours  WEIGHT_DECAY = 1e-4  LEARNING_RATE = 3e-5   max mAP:  0.3792

    2023-04-23    epoch: 300   duration: 20.8263 hours                                                                              max mAP:  0.4179
    2023-04-22    epoch: 100   duration:  7.2117 hours  WEIGHT_DECAY = 1e-4  LEARNING_RATE = 3e-5  'k_means() anchor'  'Shuffled'   max mAP:  0.3792
    2023-04-16    epoch: 100   duration:  8.0922 hours                                             'MiniBatchKMeans'                max mAP:  0.1736
    2023-04-15    epoch: 100   duration:  6.6698 hours                                             'KMeans() anchor'                max mAP:  0.1628
    2023-04-07    epoch: 1000  duration: 80.3616 hours  WEIGHT_DECAY = 1e-4  LEARNING_RATE = 1e-4  'YOLOv3 anchor'     'Serialized' max mAP:  0.1819
    ```



## **05/01**
- 2023.05.01
  - The training duration is ```5.7350 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 10e-5```
    ```
    --------------------------------------------------
    The stats of 2023-05-01-1 training:
    --------------------------------------------------
    max mAP:  0.43861937522888184
    mean mAP: 0.3436750084161758

    max training loss: 140.25660705566406
    min training loss: 0.8655197024345398

    max training loss on average: 18.507166700363157
    min training loss on average: 1.1550286275148391

    min training accuracy: 4.963176250457764
    max training accuracy: 94.96363067626953

    min testing accuracy: 36.68720245361328
    max testing accuracy: 68.37782287597656
    --------------------------------------------------
    ```
  - The training duration is ```7.0366 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 11e-5```
    ```
    --------------------------------------------------
    The stats of 2023-05-01-2 training:
    --------------------------------------------------
    max mAP:  0.449009507894516
    mean mAP: 0.38735678046941757

    max training loss: 102.38961791992188
    min training loss: 0.9561270475387573

    max training loss on average: 17.273788038889567
    min training loss on average: 1.2045013213157654

    min training accuracy: 3.2843875885009766
    max training accuracy: 96.39083099365234

    min testing accuracy: 35.68332290649414
    max testing accuracy: 73.03217315673828
    --------------------------------------------------
    ```
  - The training duration is ```7.1689 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 12e-5```
    ```
    --------------------------------------------------
    The stats of 2023-05-01-3 training:
    --------------------------------------------------
    max mAP:  0.4372125566005707
    mean mAP: 0.38275537043809893

    max training loss: 125.8486099243164
    min training loss: 0.9757415056228638

    max training loss on average: 17.398162371317547
    min training loss on average: 1.2320519105593364

    min training accuracy: 1.1024198532104492
    max training accuracy: 94.62055206298828

    min testing accuracy: 34.86196517944336
    max testing accuracy: 73.3515853881836
    --------------------------------------------------
    ```



## **04/30**
- 2023.04.30
  - The training duration is ```7.0542 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 6e-5```
    ```
    --------------------------------------------------
    The stats of 2023-04-29-1 training:
    --------------------------------------------------
    max mAP:  0.4267594814300537
    mean mAP: 0.3732090950012207

    max training loss: 70.09312438964844
    min training loss: 0.9483757019042969

    max training loss on average: 20.225014870961505
    min training loss on average: 1.1955717974901199

    min training accuracy: 0.8279584646224976
    max training accuracy: 95.35245513916016

    min testing accuracy: 32.3294563293457
    max testing accuracy: 73.48847961425781
    --------------------------------------------------
    ```
  - The training duration is ```7.1015 hours``` and ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 7e-5```
    ```
    --------------------------------------------------
    The stats of 2023-04-29-2 training:
    --------------------------------------------------
    max mAP:  0.4309697151184082
    mean mAP: 0.37477160841226576

    max training loss: 105.76203155517578
    min training loss: 0.8929504752159119

    max training loss on average: 20.704750878016153
    min training loss on average: 1.1069866104920705

    min training accuracy: 4.180961608886719
    max training accuracy: 96.9443359375

    min testing accuracy: 37.37166213989258
    max testing accuracy: 77.36710357666016
    --------------------------------------------------
    ```
  - The training duration is ```6.7780 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 8e-5```
    ```
    --------------------------------------------------
    The stats of 2023-04-30-1 training:
    --------------------------------------------------
    max mAP:  0.4340965747833252
    mean mAP: 0.36167612075805666

    max training loss: 104.89147186279297
    min training loss: 0.9307739734649658

    max training loss on average: 19.40190040588379
    min training loss on average: 1.1852473825216294

    min training accuracy: 1.6238964796066284
    max training accuracy: 95.42564392089844

    min testing accuracy: 30.458589553833008
    max testing accuracy: 71.52635192871094
    --------------------------------------------------
    ```
  - The training duration is ```5.5800 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 9e-5```
    ```
    --------------------------------------------------
    The stats of 2023-04-30-2 training:
    --------------------------------------------------
    max mAP:  0.43561217188835144
    mean mAP: 0.3712215393781662

    max training loss: 125.58506774902344
    min training loss: 0.9454944729804993

    max training loss on average: 18.3668585618337
    min training loss on average: 1.1890920907258988

    min training accuracy: 2.2048397064208984
    max training accuracy: 96.52349090576172

    min testing accuracy: 30.778005599975586
    max testing accuracy: 72.59867858886719
    --------------------------------------------------
    ```
- How to get model summary in PyTorch?
  - Using ```torchsummary.summary()``` to get the result
    - sample code
        ```python
        # from torchsummary import summary  # changing the way of import due to naming conflicts
        import torchsummary  

        # simple test settings
        IMAGE_SIZE = 416  # multiples of 32 are workable with stride [32, 16, 8]
        num_classes = 3   # 
        batch_size = 20   # num_examples
        num_channels = 3  # num_anchors

        model = YOLOv3(num_classes=num_classes) # initialize a YOLOv3 model as model

        # simple test with random inputs of 20 examples, 3 channels, and IMAGE_SIZE-by-IMAGE_SIZE input
        x = torch.randn((batch_size, num_channels, IMAGE_SIZE, IMAGE_SIZE))

        out = model(x) 

        # print out the model summary using third-party library called 'torchsummary'
        torchsummary.summary(model.cuda(), (num_channels, IMAGE_SIZE, IMAGE_SIZE), bs=batch_size)
        ```
    - model parameter summary
        ```
        ================================================================
        Total params: 61,534,504
        Trainable params: 61,534,504
        Non-trainable params: 0
        ----------------------------------------------------------------
        Input size (MB): 31.69
        Forward/backward pass size (MB): 13175.06
        Params size (MB): 234.74
        Estimated Total Size (MB): 13441.48
        ----------------------------------------------------------------
        ```
  - Reference
    - stackoverflow [How do I print the model summary in ```PyTorch```?](https://stackoverflow.com/questions/42480111/how-do-i-print-the-model-summary-in-pytorch)
    - PyTorch Doc [Is there similar pytorch function as ```model.summary()``` as ```keras```?](https://discuss.pytorch.org/t/is-there-similar-pytorch-function-as-model-summary-as-keras/2678)



## **04/29**
- 2023.04.29
  - The comparison between different ```WEIGHT_DECAY``` under the same ```LEARNING_RATE = 3e-5```
    - The ```loss``` value for every updates
      ![](https://i.imgur.com/c3i8F03.png)
    - The ```train-object-accuracy``` for every epochs
      ![](https://i.imgur.com/5oO2CyN.png)
    - The ```test-object-accuracy``` for every ```10``` epochs
      ![](https://i.imgur.com/XNy01W4.png)
    - The ```mAP``` for every ```10``` epochs
        ```cpp
        2023-04-27, epoch: 100, duration: 7.1676 hours, WEIGHT_DECAY = 1e-1, LEARNING_RATE = 3e-5, max mAP: 0.3289
        2023-04-26, epoch: 100, duration: 7.7900 hours, WEIGHT_DECAY = 1e-2, LEARNING_RATE = 3e-5, max mAP: 0.3646
        2023-04-25, epoch: 100, duration: 6.2753 hours, WEIGHT_DECAY = 1e-3, LEARNING_RATE = 3e-5, max mAP: 0.3603
        2023-04-22, epoch: 100, duration: 7.2117 hours, WEIGHT_DECAY = 1e-4, LEARNING_RATE = 3e-5, max mAP: 0.3792
        ```
      ![](https://i.imgur.com/eftQ9Tb.png)



## **04/28**
- 2023.04.28
  - The training duration is ```7.5511 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 1e-5```
    ```
    --------------------------------------------------
    The stats of 2023-04-28 training:
    --------------------------------------------------
    max mAP:  0.2697495222091675
    mean mAP: 0.18186791352927684

    max training loss: 92.10067749023438
    min training loss: 1.1181566715240479

    max training loss on average: 32.7851714070638
    min training loss on average: 1.3748071026802062

    min training accuracy: 2.0996294021606445
    max training accuracy: 92.99666595458984

    min testing accuracy: 19.9406795501709
    max testing accuracy: 64.90988159179688
    --------------------------------------------------
    ```
  - The training duration is ```7.2838 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 2e-5```
    ```
    --------------------------------------------------
    The stats of 2023-04-27-2 training:
    --------------------------------------------------
    max mAP:  0.3233576714992523
    mean mAP: 0.23364422097802162

    max training loss: 67.91127014160156
    min training loss: 0.9422303438186646

    max training loss on average: 27.790054613749188
    min training loss on average: 1.224434497753779

    min training accuracy: 0.37967154383659363
    max training accuracy: 95.5811767578125

    min testing accuracy: 22.19940757751465
    max testing accuracy: 69.38169860839844
    --------------------------------------------------
    ```
  - The training duration is ```7.2117 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 3e-5```
    ```
    --------------------------------------------------
    The stats of 2023-04-22 training:
    --------------------------------------------------
    max mAP:  0.37920689582824707
    mean mAP: 0.3020245939493179

    max training loss: 72.82600402832031
    min training loss: 0.8917444944381714

    max training loss on average: 25.31787603378296
    min training loss on average: 1.1737037108341852

    min training accuracy: 0.5489227175712585
    max training accuracy: 96.67901611328125

    min testing accuracy: 28.838693618774414
    max testing accuracy: 70.72781372070312
    --------------------------------------------------
    ```
  - The training duration is ```8.1383 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 4e-5```
    ```
    --------------------------------------------------
    The stats of 2023-04-28-2 training:
    --------------------------------------------------
    max mAP:  0.3963651657104492
    mean mAP: 0.3341544926166534

    max training loss: 67.77149963378906
    min training loss: 0.9209076166152954

    max training loss on average: 22.19623363494873
    min training loss on average: 1.146754193107287

    min training accuracy: 0.7410457134246826
    max training accuracy: 96.36795806884766

    min testing accuracy: 33.926536560058594
    max testing accuracy: 70.9787826538086
    --------------------------------------------------
    ```
  - The training duration is ```7.1785 hours``` with ```WEIGHT_DECAY = 1e-4``` and ```LEARNING_RATE = 5e-5```
    ```
    --------------------------------------------------
    The stats of 2023-04-28-3 training:
    --------------------------------------------------
    max mAP:  0.41434526443481445
    mean mAP: 0.3443592220544815

    max training loss: 65.99470520019531
    min training loss: 0.8718012571334839

    max training loss on average: 20.811571718851724
    min training loss on average: 1.0752028383811314

    min training accuracy: 1.0612506866455078
    max training accuracy: 96.4731674194336

    min testing accuracy: 35.318275451660156
    max testing accuracy: 74.19575500488281
    --------------------------------------------------
    ```



## **04/27**
- 2023.04.27
  - The training duration is ```7.1676 hours``` with  ```WEIGHT_DECAY = 1e-1```
    ```
    --------------------------------------------------
    The stats of 2023-04-27 training: 
    --------------------------------------------------
    max mAP:  0.328988641500473
    mean mAP: 0.26167472153902055

    max training loss: 57.49835968017578
    min training loss: 2.0004570484161377

    max training loss on average: 23.69808032989502
    min training loss on average: 2.260551511446635

    min training accuracy: 1.3860299587249756
    max training accuracy: 78.02479553222656

    min testing accuracy: 25.644535064697266
    max testing accuracy: 53.70750427246094
    --------------------------------------------------
    ```
    - mean mAP: ```0.26167472153902055```
        ![](https://i.imgur.com/Sp7dtJZ.png)
    - loss range: ```[57.49835968017578, 2.0004570484161377]```
    ![](https://i.imgur.com/nudeE2B.png)
    - max training accuracy: ```78.02479553222656```
    ![](https://i.imgur.com/LeC7FqK.png)
    - max testing accuracy: ```53.70750427246094```
    ![](https://i.imgur.com/q5ghBLQ.png)



## **04/26**
- 2023.04.26
  - Performing a grid search to find the optimal weight decay setting, all tests have the same settings except for the weight decay parameter
    ![](https://i.imgur.com/iUf6L9i.png)
  - The training duration is ```7.7900 hours``` with  ```WEIGHT_DECAY = 1e-2```
    ```
    --------------------------------------------------
    The stats of 2023-04-26 training: 
    --------------------------------------------------
    max mAP:  0.36460867524147034
    mean mAP: 0.2820669665932655

    max training loss: 59.46959686279297
    min training loss: 1.341576099395752

    max training loss on average: 24.546935682296752
    min training loss on average: 1.5733012755711873

    min training accuracy: 0.7913635969161987
    max training accuracy: 89.63908386230469

    min testing accuracy: 29.956649780273438
    max testing accuracy: 64.81861114501953
    --------------------------------------------------
    ```
    - mean mAP: ```0.2820669665932655```
    ![](https://i.imgur.com/au8uc9m.png)
    - loss range: ```[59.46959686279297, 1.341576099395752]```
    ![](https://i.imgur.com/dQZQtky.png)
    - max training accuracy: ```89.63908386230469```
    ![](https://i.imgur.com/Y5d47HL.png)
    - max testing accuracy: ```64.81861114501953```
    ![](https://i.imgur.com/t1zuJTp.png)
  - The training duration is ```6.2753 hours``` with ```WEIGHT_DECAY = 1e-3``` 
    ```
    --------------------------------------------------
    The stats of 2023-04-25 training: 
    --------------------------------------------------
    max mAP:  0.3603482246398926
    mean mAP: 0.2835115119814873

    max training loss: 61.669921875
    min training loss: 0.9460040330886841

    max training loss on average: 23.978200359344484
    min training loss on average: 1.233974441687266

    min training accuracy: 1.289968490600586
    max training accuracy: 95.745849609375

    min testing accuracy: 23.180469512939453
    max testing accuracy: 69.15354919433594
    --------------------------------------------------
    ```
    - mean mAP: ```0.2835115119814873```
    ![](https://i.imgur.com/5dtS7Sy.png)
    - loss range: ```[61.669921875, 0.9460040330886841]```
    ![](https://i.imgur.com/AQ5wZ7L.png)
    - max training accuracy: ```95.745849609375```
    ![](https://i.imgur.com/YUQTLki.png)
    - max testing accuracy: ```69.15354919433594```
    ![](https://i.imgur.com/ih4zhbz.png)
  - The training duration is ```7.2117``` hours with ```WEIGHT_DECAY = 1e-4``` 
    ```
    --------------------------------------------------
    The stats of 2023-04-22 training: 
    --------------------------------------------------
    max mAP:  0.37920689582824707
    mean mAP: 0.3020245939493179

    max training loss: 72.82600402832031
    min training loss: 0.8917444944381714

    max training loss on average: 25.31787603378296
    min training loss on average: 1.1737037108341852

    min training accuracy: 0.5489227175712585
    max training accuracy: 96.67901611328125

    min testing accuracy: 28.838693618774414
    max testing accuracy: 70.72781372070312
    --------------------------------------------------
    ```
    - mean mAP: ```0.3020245939493179```
    ![](https://i.imgur.com/YMORvXt.png)
    - loss range: ```[72.82600402832031, 0.8917444944381714]```
    ![](https://i.imgur.com/Zn8u5Dy.png)
    - max training accuracy: ```96.67901611328125```
    ![](https://i.imgur.com/3kdOs6a.png)
    - max testing accuracy: ```70.72781372070312```
    ![](https://i.imgur.com/vKFuAXX.png)



## **04/25**
- 2023.04.25
  - The train and test settings
    ![](https://i.imgur.com/6FZ7c9e.png)
- The result of training for ```100``` epochs, with ```k_means()``` anchor that rounded to ```3``` decimal places 
  - The training duration: ```7.2117``` hours
    ```shell
    --------------------------------------------------
    The stats of 2023-04-22 training: 
    --------------------------------------------------
    max mAP:  0.37920689582824707
    mean mAP: 0.3020245939493179

    max training loss: 72.82600402832031
    min training loss: 0.8917444944381714

    max training loss on average: 25.31787603378296
    min training loss on average: 1.1737037108341852

    min training accuracy: 0.5489227175712585
    max training accuracy: 96.67901611328125

    min testing accuracy: 28.838693618774414
    max testing accuracy: 70.72781372070312
    --------------------------------------------------
    ```
- The result of training for ```300``` epochs, with same anchors above
  - The training duration: ```20.8263``` hours
    ```
    --------------------------------------------------
    The stats of 2023-04-23 training: 
    --------------------------------------------------
    max mAP:  0.4179251194000244
    mean mAP: 0.3632150818904241

    max training loss: 72.01780700683594
    min training loss: 0.5801995992660522

    max training loss on average: 24.274858560562134
    min training loss on average: 0.7920041881004969

    min training accuracy: 0.45743560791015625
    max training accuracy: 99.13544464111328

    min testing accuracy: 35.75177001953125
    max testing accuracy: 72.34770965576172
    --------------------------------------------------
    ```
- The figures for the stats
  - max mAP:  ```0.4179251194000244```
    ![](https://i.imgur.com/aB3nZLB.png)
  - loss range: ```[72.82600402832031, 0.8917444944381714]```
    ![](https://i.imgur.com/qTgtTPY.png)
  - max training accuracy: ```99.13544464111328```
    ![](https://i.imgur.com/kODi2F4.png)
  - max testing accuracy: ```72.34770965576172```
    ![](https://i.imgur.com/bWHb0MP.png)
    
    
    

## **04/24**
- 2023.04.24
  - Shuffle the dataset and randomly select the testset (in a index sort style) works pretty well
    ![](https://i.imgur.com/KWEMqI0.png)
    - But still facing an overfitting issue
- Possible ways to solve overfitting problem
  - Gain more training data is clearly unfeasible
  - Use a larger learning rate may cause instability
  - Use a smaller batch size may raise training time
  - Use weight decay may also cause instability
    - requires a grid search to determine the proper magnitude
  - Redesign the feature extractor network
    - Reduce layers, parameters, or features
    - Add dropout layer
- What is weight decay?
  - It's a regularization technique by adding a small penalty, usually the L2 norm of the weights (all the weights of the model), to the loss function
    ```
    loss = loss + weight decay parameter * L2 norm of the weights
    ```
- Why using weight decay?
  - To prevent overfitting
  - To keep the weights small and avoid exploding gradient
- The result of training for ```100``` epochs, with ```k_means()``` anchor that rounded to ```3``` decimal places 
  - The training duration: ```7.2117``` hours
    ```
    --------------------------------------------------
    The stats of 2023-04-22 training: 
    --------------------------------------------------
    max mAP:  0.37920689582824707
    mean mAP: 0.3020245939493179

    max training loss: 72.82600402832031
    min training loss: 0.8917444944381714

    max training loss on average: 25.31787603378296
    min training loss on average: 1.1737037108341852

    min training accuracy: 0.5489227175712585
    max training accuracy: 96.67901611328125

    min testing accuracy: 28.838693618774414
    max testing accuracy: 70.72781372070312
    --------------------------------------------------
    ```
- The result of training for ```300``` epochs, with same anchors above
  - The training duration: ```20.8263``` hours
    ```
    --------------------------------------------------
    The stats of 2023-04-23 training: 
    --------------------------------------------------
    max mAP:  0.4179251194000244
    mean mAP: 0.3632150818904241
    
    max training loss: 72.01780700683594
    min training loss: 0.5801995992660522
    
    max training loss on average: 24.274858560562134
    min training loss on average: 0.7920041881004969
    
    min training accuracy: 0.45743560791015625
    max training accuracy: 99.13544464111328
    
    min testing accuracy: 35.75177001953125
    max testing accuracy: 72.34770965576172
    --------------------------------------------------
    ```
  - The figures for the stats
    - max mAP:  ```0.4179251194000244```
    ![](https://i.imgur.com/aB3nZLB.png)
    - loss range: ```[72.82600402832031, 0.8917444944381714]```
    ![](https://i.imgur.com/qTgtTPY.png)
    - max training accuracy: ```99.13544464111328```
    ![](https://i.imgur.com/kODi2F4.png)
    - max testing accuracy: ```72.34770965576172```
    ![](https://i.imgur.com/bWHb0MP.png)
- Weight Decay 
  - Some people prefer to only apply weight decay to the weights and not the bias. 
    - PyTorch applies weight decay to both weights and bias
  - Applies weight decay only to weights with ```model.named_parameters()``` function
    - PyTorchDiscuss: [Changing the weight decay on bias using named_parameters](https://discuss.pytorch.org/t/changing-the-weight-decay-on-bias-using-named-parameters/19132/1)
  - Applies weight decay in different layers also with ```model.named_parameters()``` function
    - PyTorchDiscuss: [Problem on different learning rate and weight decay in different layers](https://discuss.pytorch.org/t/problem-on-different-learning-rate-and-weight-decay-in-different-layers/3619)
  - Weight decay in Adam
    - Loshchilov, Ilya, and Frank Hutter. "[Decoupled weight decay regularization](https://arxiv.org/abs/1711.05101)." *arXiv preprint arXiv:1711.05101* (2017).
    - Published as a conference paper at ICLR 2019
  - References
    - PyTorchDiscuss: [How pytorch implement weight_decay](https://discuss.pytorch.org/t/how-pytorch-implement-weight-decay/8436)
    - PyTorchDiscuss: [How does SGD weight_decay work](https://discuss.pytorch.org/t/how-does-sgd-weight-decay-work/33105)
- Interesting stuffs that I haven't read yet
  - [Tech Hive](https://sheng-fang.github.io/) 
    - [Review of YOLO: drawback and improvement from v1 to v3](https://sheng-fang.github.io/2020-04-25-review_yolo/)
    - [Tech notes of implementation of YOLO V3](https://sheng-fang.github.io/2020-04-29-implement_yolo/)
    - [Hyper-parameters tuning practices](https://sheng-fang.github.io/2020-04-13-hyper-parameters-tuning-practices/)


## **04/23**
- 2023.04.23
  - Script for plotting the figures ```plot_training_state.py```
    ![](https://i.imgur.com/lRGOLFg.png)
    ![](https://i.imgur.com/VXSmBJJ.png)
    ![](https://i.imgur.com/rTh7e1x.png)
    ![](https://i.imgur.com/EOHHXsY.png)
    ![](https://i.imgur.com/CDqXE74.png)
    ![](https://i.imgur.com/R08ByyL.png)
    ![](https://i.imgur.com/CQO3qML.png)



## **04/21**
- 2023.04.21
  - Script for creating random samples ```create_csv.py```
    ![](https://i.imgur.com/FGOJ31Z.png)
    ![](https://i.imgur.com/aIZdzWG.png)



## **04/19**
- 2023.04.19
- A guide on 'how to use this code?'
  - First, download the ```CARRADA Dataset```, the ```Pascal_VOC Dataset``` from kaggle, or the ```CFAR Dataset``` and structure the folders as shown in the file tree below
  - Second, set up a virtual environment using Anaconda, e.g. 
    - ```conda create --name pt3.7 python=3.7``` 
    - ```conda create --name pt3.8 python=3.8```
  - Before installing any packages, remember to enter your conda virtual environment, e.g. 
    - ```conda activate pt3.7```
    - ```conda activate pt3.8```
  - Third, you can manually install all the packages that you need, or you can install with ```pip install -r requirements.txt```
  - Then, copy the code to anywhere you like, and make sure you have changed the file path in ```config.py``` before running the code
    - Just click the 'run' button and see the results
  - Caveats:
    - There are a bunch of dead code, commented code, and outdated comments in my program
    - I use ```albumentations``` library solely for the purpose of padding
  - Dataset file tree 
    ```python
    D:\Datasets\RADA\RD_JPG>tree
    D:.
    ├─checks
    ├─images
    ├─imagesc
    ├─imwrite
    ├─labels
    ├─mats
    └─training_logs
        ├─mAP
        ├─test
        │  ├─class_accuracy
        │  ├─no_object_accuracy
        │  └─object_accuracy
        └─train
            ├─class_accuracy
            ├─losses
            ├─mean_loss
            ├─no_object_accuracy
            └─object_accuracy
    ```
  - Stable dependency
    - for python 3.7 
        ```python
        python==3.7.13
        numpy==1.19.2
        pytorch==1.7.1
        torchaudio==0.7.2
        torchvision==0.8.2
        pandas==1.2.1
        pillow==8.1.0 
        tqdm==4.56.0
        albumentations==0.5.2 
        matplotlib==3.3.4
        ```
    - for python 3.8
        ```python
        python==3.8.16
        numpy==1.23.5
        pytorch==1.13.1
        pytorch-cuda==11.7
        torchaudio==0.13.1
        torchvision==0.14.1
        pandas==1.5.2
        pillow==9.3.0
        tqdm==4.64.1
        albumentations==1.3.0
        matplotlib==3.6.2
        ```
    - It's well tested, and the code can be properly executed under these settings


## **04/18**
- 2023.04.18
  - The third clustering result using custom ```k_means()```
    ```python
    Number of clusters: 9
    Average IoU: 0.6639814720619468

    Anchors original: 
    (0.42412935323383083, 0.09495491293532338), (0.040049518201284794, 0.04793729925053533), (0.12121121241202815, 0.02474208253358925), 
    (0.21935948581560283, 0.041091810726950354), (0.015625, 0.016347497459349592), (0.21888516435986158, 0.09671009948096886), 
    (0.038657583841463415, 0.008815858422256097), (0.125454418344519, 0.07256711409395973), (0.058373810467882634, 0.018722739888977002), 

    Anchors rounded to 2 decimal places: 
    (0.42, 0.09), (0.04, 0.05), (0.12, 0.02), 
    (0.22, 0.04), (0.02, 0.02), (0.22, 0.10), 
    (0.04, 0.01), (0.13, 0.07), (0.06, 0.02), 

    Anchors rounded to 3 decimal places: 
    (0.424, 0.095), (0.040, 0.048), (0.121, 0.025), 
    (0.219, 0.041), (0.016, 0.016), (0.219, 0.097), 
    (0.039, 0.009), (0.125, 0.073), (0.058, 0.019), 
    ```
  - The comparison of 
    - original anchor for general image dataset 
    ```python
    (0.28, 0.22), (0.38, 0.48), (0.9,  0.78),
    (0.07, 0.15), (0.15, 0.11), (0.14, 0.29),
    (0.02, 0.03), (0.04, 0.07), (0.08, 0.06)
    ```
    - ```sklearn.cluster.KMeans()``` result
    ```python
    (0.211, 0.098), (0.339, 0.087), (0.495, 0.092),
    (0.158, 0.033), (0.232, 0.043), (0.125, 0.082), 
    (0.033, 0.017), (0.065, 0.027), (0.107, 0.024),
    ```
    - ```sklearn.cluster.MiniBatchKMeans()``` result
    ```python
    (0.329, 0.085), (0.424, 0.096), (0.530, 0.089),
    (0.157, 0.031), (0.232, 0.064), (0.164, 0.094),
    (0.027, 0.016), (0.056, 0.024), (0.105, 0.029),
    ```
    - Custom ```k_means()``` result
    ```python
    (0.125, 0.073), (0.219, 0.097), (0.424, 0.095),
    (0.040, 0.048), (0.121, 0.025), (0.219, 0.041),
    (0.016, 0.016), (0.039, 0.009), (0.058, 0.019),
    ```
  - training for 1000 epochs with original anchors
    ```
    max mAP:  0.18192845582962036 (the highest mAP obtained out of 10 tests)
    mean mAP: 0.1663009986281395  (the average mAP obtained out of 10 tests)
    
    max training loss: 125.03005981445312
    min training loss: 0.6005923748016357
    
    max training loss on average: 19.55863230228424
    min training loss on average: 0.8333272246519724
    
    min training accuracy: 2.8318750858306885
    max training accuracy: 98.84278869628906

    min testing accuracy: 33.172786712646484
    max testing accuracy: 70.57997131347656
    ```
    - The figures fot the stats
    ![](https://i.imgur.com/XzHCdeK.png)
    ![](https://i.imgur.com/4uwzdv8.png)
    ![](https://i.imgur.com/n1YbQBr.png)
    ![](https://i.imgur.com/T6eq1gA.png)
    ![](https://i.imgur.com/w1rvagY.png)
  - training for 100 epochs with ```sklearn.cluster.KMeans()``` anchor that rounded to 2 decimal places
    ```
    max training loss on average: 17.887332406044006
    min training loss on average: 1.1761843407154082
    
    min training accuracy: 1.1478031873703003
    max training accuracy: 96.33079528808594

    min testing accuracy: 28.48825454711914
    max testing accuracy: 67.01465606689453
    
    max mAP:  0.1628512293100357
    mean mAP: 0.1628512293100357 (only test once)
    ```
  - training for 100 epochs with ```sklearn.cluster.KMeans()``` anchor that rounded to 3 decimal places
    ```
    max training loss on average: 18.193040917714438
    min training loss on average: 1.2186308292547863
    
    min training accuracy: 4.069056510925293
    max training accuracy: 94.63731384277344

    min testing accuracy: 28.80947494506836
    max testing accuracy: 66.93435668945312
    
    max mAP:  0.17361223697662354
    mean mAP: 0.17361223697662354 (only test once)
    ```
- The YOLO network seems not able to properly learn this task
  - Keep improving the anchor settings
    - Plot the comparison between different anchor settings
  - Redesign the feture extractor structure
    - Change the detection head network
  - Apply certain training strategy for our task, e.g. Weight Initialization:
    - Random Initialization (current method)
    - Xavier Initialization, or Glorot Initialization
    - Kaiming Initialization, or He Initialization
    - LeCun Initialization
    - Ref. Deeplizard [Weight Initialization Explained](https://deeplizard.com/learn/video/8krd5qKVw-Q)
  - Using k-fold cross-validation to ensure that there's no training data selection bias



## **04/17**
- 2023.04.17
  - The code for handcrafted-from-scratch version of ```k_means()``` which consider IoU in its distance metric
    ![](https://i.imgur.com/L4O0tu4.png)
    ![](https://i.imgur.com/i730QvA.png)
  - The first clustering result using ```sklearn.cluster.KMeans()``` 
    ```python
    Estimator: KMeans(n_clusters=9, verbose=True)
    Number of Clusters: 9
    Average IoU: 0.6268763251152744
    Inertia: 4.175114625246291
    Silhouette Score: 0.4465142389008657
    Date and Duration: 2023-04-13 / 0.0951 seconds

    Anchors: 
      1: (0.03258875446251471852, 0.01661357100357002681)   5.414155861808978
      2: (0.06474560301507539806, 0.02702967964824120467)   17.50052908129688
      3: (0.10668965880370681609, 0.02383240311710192738)   25.426709570360032
      4: (0.15826612903225806273, 0.03252153592375366803)   51.47057600836014
      5: (0.23229679802955666146, 0.04291102216748768350)   99.68093049682716
      6: (0.12471330275229357276, 0.08154147553516821745)   101.69306725286172
      7: (0.21058315334773208827, 0.09842400107991366998)   207.26436512508812
      8: (0.33944144518272417743, 0.08742992109634553644)   296.77338769155074
      9: (0.49540441176470573215, 0.09187346813725494332)   455.1452143932022

    Anchors original: 
    (0.03258875446251472, 0.016613571003570027), (0.0647456030150754, 0.027029679648241205), (0.10668965880370682, 0.023832403117101927), 
    (0.15826612903225806, 0.03252153592375367), (0.23229679802955666, 0.042911022167487683), (0.12471330275229357, 0.08154147553516822), 
    (0.2105831533477321, 0.09842400107991367), (0.3394414451827242, 0.08742992109634554), (0.49540441176470573, 0.09187346813725494), 

    Anchors rounded to 2 decimal places: 
    (0.03, 0.02), (0.06, 0.03), (0.11, 0.02), 
    (0.16, 0.03), (0.23, 0.04), (0.12, 0.08), 
    (0.21, 0.10), (0.34, 0.09), (0.50, 0.09), 

    Anchors rounded to 3 decimal places: 
    (0.033, 0.017), (0.065, 0.027), (0.107, 0.024), 
    (0.158, 0.033), (0.232, 0.043), (0.125, 0.082), 
    (0.211, 0.098), (0.339, 0.087), (0.495, 0.092), 
    ```
  - The second clustering result using
    ```python
    Estimator: MiniBatchKMeans(n_clusters=9, tol=0.0001, verbose=True)
    Number of Clusters: 9
    Average IoU: 0.6075905487924542
    Inertia: 4.375712040766109
    Silhouette Score: 0.41462042329969084
    Date and Duration: 2023-04-13 / 0.0423 seconds

    Anchors: 
      1: (0.02677950180907319802, 0.01550867137489563008)   4.153144931403392
      2: (0.05614595190665907370, 0.02351197887023335348)   13.201024348785062
      3: (0.10527306967984934039, 0.02908427495291902171)   30.61790903706541
      4: (0.15678998161764706731, 0.03086224724264705413)   48.388911778539104
      5: (0.23159116755117511999, 0.06435983699772555855)   149.0516979370658
      6: (0.16395052370452040114, 0.09384044239250277641)   153.85189674914707
      7: (0.32857417864476384795, 0.08490278490759754770)   278.9686281566692
      8: (0.42449951171874988898, 0.09640502929687500000)   409.23887863755215
      9: (0.53048469387755103899, 0.08938137755102043558)   474.1545270850689

    Anchors original: 
    (0.026779501809073198, 0.01550867137489563), (0.056145951906659074, 0.023511978870233353), (0.10527306967984934, 0.02908427495291902), 
    (0.15678998161764707, 0.030862247242647054), (0.23159116755117512, 0.06435983699772556), (0.1639505237045204, 0.09384044239250278), 
    (0.32857417864476385, 0.08490278490759755), (0.4244995117187499, 0.096405029296875), (0.530484693877551, 0.08938137755102044), 

    Anchors rounded to 2 decimal places: 
    (0.03, 0.02), (0.06, 0.02), (0.11, 0.03), 
    (0.16, 0.03), (0.23, 0.06), (0.16, 0.09), 
    (0.33, 0.08), (0.42, 0.10), (0.53, 0.09), 

    Anchors rounded to 3 decimal places: 
    (0.027, 0.016), (0.056, 0.024), (0.105, 0.029), 
    (0.157, 0.031), (0.232, 0.064), (0.164, 0.094), 
    (0.329, 0.085), (0.424, 0.096), (0.530, 0.089),
    ```
  - The original anchor for general image dataset
    ```python
    ANCHORS = [
        [(0.28, 0.22), (0.38, 0.48), (0.9,  0.78)], 
        [(0.07, 0.15), (0.15, 0.11), (0.14, 0.29)], 
        [(0.02, 0.03), (0.04, 0.07), (0.08, 0.06)], 
    ]  # Note these have been rescaled to be between [0, 1]
    ```



## **04/13**
- 2023.04.13
  - stackoverflow [Custom Python list sorting](https://stackoverflow.com/questions/11850425/custom-python-list-sorting)
    ```python
    from functools import cmp_to_key
    cmp_key = cmp_to_key(cmp_function)
    mylist.sort(key=cmp_key)
    ```
  - ```get_anchors2.py```
    - Finishing the part where I use  ```sklearn.cluster.KMeans()``` and ```sklearn.cluster.MiniBatchKMeans()``` for clustering
    - The custom-designed / handcrafted-from-scratch version of ```k_means()``` is also finished, but it hasn't been well-tested yet
  - The part of the code
    ![](https://i.imgur.com/2S6N6t9.png)
    ![](https://i.imgur.com/254IZGY.png)
    ![](https://i.imgur.com/FLtmwaM.png)
    ![](https://i.imgur.com/fUJmBSC.png)



## **04/10**
- 2023.04.10
  - Need to recompute / regenerate anchors for YOLO [Training YOLO? Select Anchor Boxes Like This](https://towardsdatascience.com/training-yolo-select-anchor-boxes-like-this-3226cb8d7f0b)
  - for YOLOv2 ```AlexeyAB/darknet/scripts/``` [```gen_anchors.py```](https://github.com/AlexeyAB/darknet/blob/master/scripts/gen_anchors.py)
    - The anchor boxes were calculated with a k-means clustering algorithm only
    - With ```1 - IoU``` as a distance metric
    - Doing k-means clustering only is a good approach already
  - for YOLOv5 / YOLOv7 ```ultralytics/yolov5/utils/``` [```autoanchor.py```](https://github.com/ultralytics/yolov5/blob/master/utils/autoanchor.py)
  - ultralytics YOLOv5 Docs [Train Custom Data](https://docs.ultralytics.com/yolov5/train_custom_data/)
- Auto-anchor algorithm
  - ```Step 0.``` K-means (with simple Euclidean distance) is used to get the initial guess for anchor boxes
    - We also can do it with ```1 - IoU``` as a distance metric
  - ```Step 1.``` Get bounding box sizes from the train data
  - ```Step 2.``` Choose a metric to define anchor fitness
    - Ideally, the metric should be connected to the loss function
  - ```Step 3.``` Do clustering to get an initial guess for anchors
  - ```Step 4.``` Evolve anchors to improve anchor fitness
- Things I'm Googling but haven't finished reading
  - Faster RCNN with PyTorch
    - PyTorch Docs [TORCHVISION OBJECT DETECTION FINETUNING TUTORIAL](https://pytorch.org/tutorials/intermediate/torchvision_tutorial.html)
    - PyTorch Docs [MODELS AND PRE-TRAINED WEIGHTS](https://pytorch.org/vision/main/models.html)
    - PyTorch Source Code [```fasterrcnn_resnet50_fpn()```](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/faster_rcnn.html#fasterrcnn_resnet50_fpn)
    - 知呼 FasterRCNN 解析 [pytorch官方FasterRCNN代碼](https://zhuanlan.zhihu.com/p/145842317)
  - Faster RCNN reproduction
    - Kaggle object detection [Aquarium Dataset](https://www.kaggle.com/datasets/sharansmenon/aquarium-dataset)
      - [Object Detection FasterRCNN Tutorial](https://www.kaggle.com/code/pdochannel/object-detection-fasterrcnn-tutorial)
    - Kaggle Pytorch Starter -  [FasterRCNN Train](https://www.kaggle.com/code/pestipeti/pytorch-starter-fasterrcnn-train/notebook)
      - Global Wheat Dataset 不給下載
    - github search for [faster-r-cnn](https://github.com/search?q=faster-r-cnn&type=repositories&p=5)
  - Kmeans implementation
    - scikit-learn [Clustering with kmeans](https://scikit-learn.org/stable/modules/clustering.html#k-means)
    - scikit-learn [Clustering performance evaluation](https://scikit-learn.org/stable/modules/clustering.html#clustering-evaluation)
    - scikit-learn [```sklearn.cluster.KMeans()```](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
    - Tech-with-Tim [Implementing K Means Clustering](https://www.techwithtim.net/tutorials/machine-learning-python/k-means-2/) 
    ![](https://i.imgur.com/bgqHKHr.png)
    - Sentdex [K-Means from Scratch in Python](https://pythonprogramming.net/k-means-from-scratch-machine-learning-tutorial/)
    ![](https://i.imgur.com/FVv5sMX.png)



## **04/09**
- 2023.04.09
  - 過去 10 天確診啥也沒做


## **03/28**
- 2023.03.28
  - I tried to train the model until a point where we're satisfied with its performance, then we can do the edge computing modifications on it
  - Quick recap:
    - The [DAROD paper](https://ieeexplore.ieee.org/document/9827281) propose a light architecture for the ```Faster R-CNN``` object detector on this particular task
    - They can reach respectively an ```mAP@0.5``` and ```mAP@0.3``` of ```55.83``` and ```70.68```
    - So our goal is to at least get a better mAP then they did
  - The current ```mAP@50``` (for every ```100``` epochs) and ```mean loss``` (for every epoch), for a total of ```300``` epochs of training:
    ![](https://i.imgur.com/4xcdypl.png)
    ```
    max training loss (on average): 20.516442289352415
    min training loss (on average): 1.0732185713450113
    ```
  - To further analyze where the problems are, I first extracted some of the data that I think might be helpful 
  - The file tree structure:
    ```
    D:/Datasets/RADA/RD_JPG/training_logs>tree
    D:.
    ├─mAP
    ├─test
    │  ├─class_accuracy
    │  ├─no_object_accuracy
    │  └─object_accuracy
    └─train
        ├─class_accuracy
        ├─losses
        ├─mean_loss
        ├─no_object_accuracy
        └─object_accuracy
    ```
  - Some other results
    - train-class-accuracy vs. test-class-accuracy
        ![](https://i.imgur.com/8I03exy.png)
    - train-no-object-accuracy vs. test-no-object-accuracy
        ![](https://i.imgur.com/dXqZ2Ft.png)
    - train-object-accuracy vs. test-object-accuracy
        ![](https://i.imgur.com/HADZnUl.png)
        ```
        min training accuracy: 2.3661680221557617
        max training accuracy: 94.16690826416016

        min testing accuracy: 46.69877624511719
        max testing accuracy: 72.34597778320312
        ```
  - The layers of the model
    ```python
    layer 0:  torch.Size([20, 32, 416, 416])
    layer 1:  torch.Size([20, 64, 208, 208])
    layer 2:  torch.Size([20, 64, 208, 208])
    layer 3:  torch.Size([20, 128, 104, 104])
    layer 4:  torch.Size([20, 128, 104, 104])
    layer 5:  torch.Size([20, 256, 52, 52])
    layer 6:  torch.Size([20, 256, 52, 52])
    layer 7:  torch.Size([20, 512, 26, 26])
    layer 8:  torch.Size([20, 512, 26, 26])
    layer 9:  torch.Size([20, 1024, 13, 13])
    layer 10:  torch.Size([20, 1024, 13, 13])
    layer 11:  torch.Size([20, 512, 13, 13])
    layer 12:  torch.Size([20, 1024, 13, 13])
    layer 13:  torch.Size([20, 1024, 13, 13])
    layer 14:  torch.Size([20, 512, 13, 13])
    layer 16:  torch.Size([20, 256, 13, 13])
    layer 17:  torch.Size([20, 256, 26, 26])
    layer 18:  torch.Size([20, 256, 26, 26])
    layer 19:  torch.Size([20, 512, 26, 26])
    layer 20:  torch.Size([20, 512, 26, 26])
    layer 21:  torch.Size([20, 256, 26, 26])
    layer 23:  torch.Size([20, 128, 26, 26])
    layer 24:  torch.Size([20, 128, 52, 52])
    layer 25:  torch.Size([20, 128, 52, 52])
    layer 26:  torch.Size([20, 256, 52, 52])
    layer 27:  torch.Size([20, 256, 52, 52])
    layer 28:  torch.Size([20, 128, 52, 52])
    ```
    ```python
    config = [
        (32, 3, 1),   # (32, 3, 1) is the CBL, CBL = Conv + BN + LeakyReLU
        (64, 3, 2),
        ["B", 1],     # (64, 3, 2) + ["B", 1] is the Res1, Res1 = ZeroPadding + CBL + (CBL + CBL + Add)*1
        (128, 3, 2),
        ["B", 2],     # (128, 3, 2) + ["B", 2] is th Res2, Res2 = ZeroPadding + CBL + (CBL + CBL + Add)*2
        (256, 3, 2),
        ["B", 8],     # (256, 3, 2) + ["B", 8] is th Res8, Res8 = ZeroPadding + CBL + (CBL + CBL + Add)*8
        (512, 3, 2),
        ["B", 8],     # (512, 3, 2) + ["B", 8] is th Res8, Res8 = ZeroPadding + CBL + (CBL + CBL + Add)*8
        (1024, 3, 2),
        ["B", 4],     # (1024, 3, 2) + ["B", 4] is th Res4, Res4 = ZeroPadding + CBL + (CBL + CBL + Add)*4
        # to this point is Darknet-53 which has 52 layers
        (512, 1, 1),  # 
        (1024, 3, 1), #
        "S",
        (256, 1, 1),
        "U",
        (256, 1, 1),
        (512, 3, 1),
        "S",
        (128, 1, 1),
        "U",
        (128, 1, 1),
        (256, 3, 1),
        "S",
    ]
    ```



## **03/19**
- 2023.03.19
  - The actual size of each input image is: 
    - ```875-by-1489``` or ```310-by-1240```
    ![](https://i.imgur.com/Cjg1AiQ.png)
  - The resizing results are completely different. We could even conclude that they are wrong (and I don't know why), since we might not need to resize images anymore. Currently, I am just ignoring this issue
  ![](https://i.imgur.com/QoYz9TP.jpg)
  ![](https://i.imgur.com/wexdIfa.png)
  - Some samples of person, cyclist and car:
    ![](https://i.imgur.com/2axeJNC.jpg)
    ![](https://i.imgur.com/w3ivjzM.jpg)
    ![](https://i.imgur.com/bbIMrqB.jpg)
  - I first tried to run ```train.py``` for ```100``` epochs with the following config settings:
    ![](https://i.imgur.com/M2u8BtK.png)
  - The resulted ```mAP``` is ```0.182485```
    ![](https://i.imgur.com/eGgLni0.png)
    ![](https://i.imgur.com/faPMJob.png)
  - The code for extracting the data from the log files ```read_logs.py```
    ![](https://i.imgur.com/yzPEsUE.png)
    ![](https://i.imgur.com/CEeq9LO.png)
    ![](https://i.imgur.com/EGTWlkP.png)
    ![](https://i.imgur.com/XIehPQV.png)





## **03/16**
- 2023.03.16
  - It's finally trainable now
    ![](https://i.imgur.com/Q8anAyR.png)
  - The major mistakes that I made were: Misinterpreting the labels, but actually translating them correctly.
    - In short, simply switching the ```x``` and ```y``` coordinates will solve our problems
    - This makes me wonder, How did I get it right when replicating ```YOLO-CFAR``` before?
    - Since the shape of the feature map is printed as ```torch.Size([256, 64, 3])```, it shows the same coordinate system as the ```RD map``` where the origin ```(0, 0)``` is located at the top left corner
    - But it turns out that's not the case. The model still recognizes the bottom left corner as the origin, which is the same as we usually do.
  - The correct way to translate the labels
    ![](https://i.imgur.com/DoAn99t.png)
    ![](https://i.imgur.com/skwA1D3.png)
  - The values of training loss, training accuracy and test accuracy
    - training loss = ```[15.2, 7.16, 6.26, 5.75, 5.35, 5.04, 4.72, 4.5, 4.21, 3.99, 3.69, 3.57, 3.3, 3.22, 3.08, 2.89, 2.79, 2.79, 2.62, 2.59, 2.52, 2.27, 2.34, 2.68, 2.23, 2.07, 2.13, 2.33, 2.23, 2.06, 1.95, 1.93, 2.39, 2.09, 2.25, 1.9, 1.72, 1.71, 1.81, 1.96, 2.35, 2.0, 1.69, 1.6, 2.14, 1.9, 1.64, 1.58, 1.63, 1.76, 1.82, 2.32, 1.88, 1.6, 1.54, 1.5, 1.57, 1.69, 2.16, 1.85, 1.52, 1.42, 1.48, 1.58, 1.74, 2.09, 1.69, 1.46, 1.4, 1.46, 1.58, 2.14, 1.65, 1.44, 1.36, 1.36, 1.5, 1.65, 2.21, 1.67, 1.4, 1.29, 1.32, 1.45, 1.57, 1.63, 1.58, 1.56, 1.72, 1.8, 1.41, 1.27, 1.26, 1.42, 1.85, 1.89, 1.63, 1.41, 1.27, 1.24]```
    - num of loss samples: ```100```
    - train obj accuracy = ```[4.765, 18.71, 15.92, 10.55, 29.82, 28.52, 22.56, 23.77, 24.76, 31.47, 34.53, 36.45, 44.58, 48.02, 42.87, 59.59, 61.62, 57.15, 64.11, 63.36, 69.5, 71.31, 66.77, 67.49, 75.09, 73.42, 61.87, 75.83, 72.21, 77.93, 80.76, 78.95, 69.45, 77.32, 74.59, 85.04, 86.72, 84.16, 83.46, 84.53, 69.05, 83.64, 86.28, 89.1, 74.92, 84.12, 88.02, 89.16, 86.14, 87.57, 84.91, 74.47, 84.79, 85.28, 89.33, 91.11, 91.97, 83.31, 77.62, 86.2, 90.33, 91.34, 90.65, 89.82, 86.9, 84.81, 87.93, 90.73, 90.6, 90.64, 90.18, 82.33, 86.82, 89.31, 91.77, 92.38, 89.89, 89.59, 83.69, 87.44, 92.25, 94.87, 92.24, 91.11, 90.11, 89.76, 88.76, 88.35, 72.4, 89.63, 91.92, 95.16, 92.85, 90.79, 79.25, 82.2, 90.09, 91.73, 92.62, 93.03]```
    - num of train samples: ```100```
    - test obj accuracy = ```[27.31, 56.63, 66.7, 69.19, 67.6, 65.34, 64.05, 59.62, 62.23, 61.46, 61.46]```
    x1- num of test samples: ```11```


## **03/15**
- 2023.03.15
  - Still not actually trainable
    ```clike!
    ValueError: Expected x_min for bbox (-0.103515625, 0.306640625, 0.224609375, 0.365234375, 2.0) to be in the range [0.0, 1.0], got -0.103515625.
    ```
    - The issue stems from my erroneous translation of the labels
    - The way we figured this out is by feeding the model with correct but actually wrong answers, so that we can distinguish whether the issue lies in the content of the label or my code implementation
  - What I mean by wrong labels is that I use the previously well-tested synthetic radar dataset labels for training
![](https://i.imgur.com/H4HTexN.jpg)
  - It is trainable with correct but actually wrong labels
![](https://i.imgur.com/tKcw2LA.png)
  - When testing ```PASCAL_VOC``` dataset, I actually used padding for the input images, but I forgot that padding existed. So we can now confirm that my code can only take square inputs



## **03/14**
- 2023.03.14
  - Ref. Albumentations Documentation [Full API Reference](https://albumentations.ai/docs/api_reference/full_reference/)
    - testing different border modes
    ![](https://i.imgur.com/5m01r0U.png)
    - comparison of the 4 different modes: 
    ![](https://i.imgur.com/EOvisqk.png)
    - ```cv2.BORDER_CONSTANT```, ```cv2.BORDER_REFLECT```, ```cv2.BORDER_DEFAULT```, ```cv2.BORDER_REPLICATE``` with the value of ```0```, ```2```, ```4``` and ```1```, respectively
  - Remove useless transforms of ```YOLOv3-VOC```
    - we need ```LongestMaxSize()``` and ```PadIfNeeded()``` to avoid ```RuntimeError: Trying to resize storage that is not resizable```
    - we need ```Normalize()``` to avoid ```RuntimeError: Input type (torch.cuda.ByteTensor) and weight type (torch.cuda.HalfTensor) should be the same```
    - we need ```ToTensorV2()``` to avoid ```RuntimeError: Given groups=1, weight of size [32, 3, 3, 3], expected input[10, 416, 416, 3] to have 3 channels, but got 416 channels instead```
  - The execution result and the error messages of the same code are different when using my PC compared to the lab PC, which is weird and annoying.



## **03/10**
- 2023.03.10
  - Still untrainable
    - First, I prepare ```3``` types of square sizes of images, 64-by-64, 256-by-256, and 416-by-416, respectively.
    - The way I tested it is by simply changing the input images to the previously successful version, without changing anything else, and seeing how it goes.
    - Even though I resized all the images to a square size, the exact same error persists. Specifically:
        ```clike!
        RuntimeError: Given groups=1, weight of size [32, 3, 3, 3], expected input[16, 64, 64, 3] to have 3 channels, but got 64 channels instead
        ```
        ```clike!
        RuntimeError: Given groups=1, weight of size [32, 3, 3, 3], expected input[16, 256, 256, 3] to have 3 channels, but got 256 channels instead
        ```
        ```clike!
        RuntimeError: Given groups=1, weight of size [32, 3, 3, 3], expected input[16, 416, 416, 3] to have 3 channels, but got 416 channels instead
        ```
  - It still doesn't work, but every piece of code is the same, so I speculate that maybe it's because the images are not actually encoded in the ```'JPEG'``` format.
  - So I re-read the dataset, stored the ```.mat``` files out, and converted the ```.mat``` files into scaled color and grayscale.
    - Plotting 7193 frames of the CARRADA Dataset in scaled color using MATLAB [link](https://www.youtube.com/watch?v=DyZ7rPXPHjE)
  - Then I used the scaled color images to train, still getting errors, but at least now we have a different error message.
    ```clike!
    ValueError: Expected x_min for bbox (-0.103515625, 0.306640625, 0.224609375, 0.365234375, 2.0) to be in the range [0.0, 1.0], got -0.103515625.
    ```



## **03/09**
- 2023.03.09
  - The function for converting ```.mat``` files to ```.jpg``` images
<img src=https://i.imgur.com/HLDGo78.png width=75% height=75%>
<img src=https://i.imgur.com/XqgPJW8.png width=75% height=75%>



## **03/04**
- 2023.03.04
  - New breach, image file format may be the issue
  - Regenerate all data in ```.jpg```



## **02/25**
- 2023.02.25
  - Reading [You Might Be Resizing Your Images Incorrectly](https://blog.roboflow.com/you-might-be-resizing-your-images-incorrectly/)
    - What If Images Need to be Square?
  - Reading [The dangers behind image resizing](https://zuru.tech/blog/the-dangers-behind-image-resizing)
    - the most correct behavior is given by the Pillow resize





## **02/21**
- 2023.02.21
  - modified from YOLO-CFAR
    ```clike!
    (pt3.8) D:\Datasets\YOLOv3-PyTorch\YOLOv3-debug1>D:/ProgramData/Anaconda3/envs/pt3.8/python.exe d:/Datasets/YOLOv3-PyTorch/YOLOv3-debug1/train.py
      0%|                               | 0/375 [00:03<?, ?it/s]
    Traceback (most recent call last):
      File "d:/Datasets/YOLOv3-PyTorch/YOLOv3-debug1/train.py", line 166, in <module>
        main()
      File "d:/Datasets/YOLOv3-PyTorch/YOLOv3-debug1/train.py", line 107, in main    
        train_fn(train_loader, model, optimizer, loss_fn, scaler, scaled_anchors)    
      File "d:/Datasets/YOLOv3-PyTorch/YOLOv3-debug1/train.py", line 57, in train_fn
        out = model(x)
      File "D:\ProgramData\Anaconda3\envs\pt3.8\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
        return forward_call(*input, **kwargs)
      File "d:\Datasets\YOLOv3-PyTorch\YOLOv3-debug1\model.py", line 191, in forward
        x = layer(x) #
      File "D:\ProgramData\Anaconda3\envs\pt3.8\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
        return forward_call(*input, **kwargs)
      File "d:\Datasets\YOLOv3-PyTorch\YOLOv3-debug1\model.py", line 110, in forward
        return self.leaky(self.bn(self.conv(x))) # bn_act()
      File "D:\ProgramData\Anaconda3\envs\pt3.8\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
        return forward_call(*input, **kwargs)
      File "D:\ProgramData\Anaconda3\envs\pt3.8\lib\site-packages\torch\nn\modules\conv.py", line 463, in forward
        return self._conv_forward(input, self.weight, self.bias)
      File "D:\ProgramData\Anaconda3\envs\pt3.8\lib\site-packages\torch\nn\modules\conv.py", line 459, in _conv_forward
        return F.conv2d(input, weight, bias, self.stride,
    RuntimeError: Given groups=1, weight of size [32, 3, 3, 3], expected input[16, 256, 64, 3] to have 3 channels, but got 256 channels instead
    ```
  - modified from YOLO-Pascal_VOC
    ```clike!
    (pt3.8) D:\Datasets\YOLOv3-PyTorch\YOLOv3-debug2>D:/ProgramData/Anaconda3/envs/pt3.8/python.exe d:/Datasets/YOLOv3-PyTorch/YOLOv3-debug2/train.py
      0%|                | 0/5999 [00:00<?, ?it/s]
    x:  torch.Size([1, 3, 256, 64])
    y0: torch.Size([1, 3, 2, 2, 6])
    y1: torch.Size([1, 3, 2, 2, 6])
    y2: torch.Size([1, 3, 2, 2, 6])
      0%|                | 0/5999 [00:04<?, ?it/s]
    Traceback (most recent call last):
      File "d:/Datasets/YOLOv3-PyTorch/YOLOv3-debug2/train.py", line 144, in <module>
        main()
      File "d:/Datasets/YOLOv3-PyTorch/YOLOv3-debug2/train.py", line 91, in main
        train_fn(train_loader, model, optimizer, loss_fn, scaler, scaled_anchors)
      File "d:/Datasets/YOLOv3-PyTorch/YOLOv3-debug2/train.py", line 47, in train_fn
        loss_fn(out[0], y0, scaled_anchors[0])
      File "D:\ProgramData\Anaconda3\envs\pt3.8\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
        return forward_call(*input, **kwargs)
      File "d:\Datasets\YOLOv3-PyTorch\YOLOv3-debug2\loss.py", line 83, in forward
        no_object_loss = self.bce((predictions[..., 0:1][noobj]), (target[..., 0:1][noobj]),)
    IndexError: The shape of the mask [1, 3, 2, 2] at index 2 does not match the shape of the indexed tensor [1, 3, 8, 2, 1] at index 2
    ```



## **02/20**
- 2023.02.20
  - We now have the model trained on ```Pascal_VOC``` dataset with the following result
    ![](https://i.imgur.com/mZN3b25.png)
  - The model was evaluated with confidence ```0.6``` and IOU threshold ```0.5``` using NMS
    |          Model          |     mAP_50    |
    | ----------------------- | ------------- |
    | ```YOLOv3-Pascal_VOC``` | ```75.7776``` |
    - The overlapped area means <img src = 'https://i.imgur.com/SHNltVr.png' height=10% width=10% >
    - IoU threshold value to the actual overlapped area
    <img src = 'https://i.imgur.com/quULxhX.png' height=70% width=70% >








## **02/18**
- 2023.02.18
  - The virtual envs are summarized below:
  - My PC ```(Intel i7-8700 + Nvidia Geforce RTX 2060)```: 
    - env ```pt3.7``` with CUDA 
        ```python
        python==3.7.13
        numpy==1.19.2
        pytorch==1.7.1
        torchaudio==0.7.2
        torchvision==0.8.2
        pandas==1.2.1
        pillow==8.1.0 
        tqdm==4.56.0
        matplotlib==3.3.4
        albumentations==0.5.2
        ```
  - Lab PC ```(Intel i7-12700 + Nvidia Geforce RTX 3060 Ti)```: 
    - env ```pt3.7``` without CUDA
        ```python
        python==3.7.13
        numpy==1.21.6
        torch==1.13.1
        torchvision==0.14.1
        pandas==1.3.5
        pillow==9.4.0
        tqdm==4.64.1
        matplotlib==3.5.3
        albumentations==1.3.0
        ```
    - env ```pt3.8``` with CUDA
        ```python
        python==3.8.16
        numpy==1.23.5
        pytorch==1.13.1
        pytorch-cuda==11.7
        torchaudio==0.13.1             
        torchvision==0.14.1
        pandas==1.5.2
        pillow==9.3.0
        tqdm==4.64.1
        matplotlib==3.6.2
        albumentations==1.3.0
        ```
  - An annoying bug in ```dataset.py``` due to pytorch version
    - The code segment that contains potential bug (on line ```149``` and ```155```)
    ![](https://i.imgur.com/w5hUN05.png)
    ![](https://i.imgur.com/R7TKmAo.png)
    - ```scale_idx = anchor_idx // self.num_anchors_per_scale``` works fine on my PC, but on lab PC will get the following warning, so I naturally followed the suggestions and changed the syntax to ([```torch.div()```](https://pytorch.org/docs/stable/generated/torch.div.html))
        ```clike!
        UserWarning: __floordiv__ is deprecated, and its behavior will change in a future version of pytorch.
        ```
    - After following the suggestion and chage  the deprecated usage ```//``` we have: ```scale_idx = torch.div(anchor_idx, self.num_anchors_per_scale, rounding_mode='floor')```. This piece of code works fine on lab PC, under both env ```pt3.7``` and ```pt3.8```, but failed on my PC.
    - The error only occur on my PC, under env ```pt3.7```, but this env is the initial and stable one.
        ```clike
        Original Traceback (most recent call last):
          File "C:\Users\paulc\.conda\envs\pt3.7\lib\site-packages\torch\utils\data\_utils\worker.py", line 198, in _worker_loop
            data = fetcher.fetch(index)
          File "C:\Users\paulc\.conda\envs\pt3.7\lib\site-packages\torch\utils\data\_utils\fetch.py", line 44, in fetch
            data = [self.dataset[idx] for idx in possibly_batched_index]
          File "C:\Users\paulc\.conda\envs\pt3.7\lib\site-packages\torch\utils\data\_utils\fetch.py", line 44, in <listcomp>
            data = [self.dataset[idx] for idx in possibly_batched_index]
          File "d:\Datasets\YOLOv3-PyTorch\dataset.py", line 153, in __getitem__
            scale_idx = torch.div(anchor_idx, self.num_anchors_per_scale, rounding_mode='floor')
        TypeError: div() got an unexpected keyword argument 'rounding_mode'
        ```
  - Way to solve it:
    - First, try using ```torch.div()```. If it doesn't work, then change it back to ```//```.



## **02/13**
- 2023.02.13
  - The actual dependency, the new requirement is:
    ```python
    numpy==1.23.5
    matplotlib==3.6.2
    pytorch==1.13.1
    pytorch-cuda==11.7
    torchaudio==0.13.1             
    torchvision==0.14.1
    tqdm==4.64.1
    albumentations==1.3.0
    pandas==1.5.2
    pillow==9.3.0
    ```



## **02/10**
- 2023.02.10
  - Trying newer stable PyTorch and CUDA version for the project
  - Python 3.8 + CUDA 11.7 
    - ```conda create --name pt3.8 python=3.8```
    - ```conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia``` ([Install PyTorch](https://pytorch.org/))
  - **Interesting to know!** 
    - 如果透過系統管理員開啟 ```Anaconda Prompt``` 並安裝的環境會存在 D 槽的 ```D:/ProgramData/Anaconda3/envs/```
    ![](https://i.imgur.com/G979f4e.png)
    - 反之，直接開 ```Anaconda Prompt``` 安裝的環境會存在 C 槽的 ```C:/Users/Paul/.conda/envs/```
    - 以後記得都用系統管理員執行!




## **02/08**
- 2023.02.08
  - The ```YOLOv3``` model is trainable with ```Pascal_VOC``` dataset
    - But it's bind with ```Albumentations``` / data augmentations, which means we need to decoupling it
  - To our knowledge, we know that **pre-training is good for our task**, least that's what the paper says, so I was trying to solve this issue
    - C. Decourt, R. VanRullen, D. Salle and T. Oberlin, "[DAROD: A Deep Automotive Radar Object Detector on Range-Doppler maps](https://ieeexplore.ieee.org/abstract/document/9827281)," *2022 IEEE Intelligent Vehicles Symposium (IV)*, Aachen, Germany, 2022, pp. 112-118.
  - Originally, I want to convert the pre-trained weights from darknet_format to pytorch_format, **it does not work**
  - Add two additional functions ```load_CNN_weights()``` and ```load_darknet_weights()``` in ```model.py``` to read the darknet weights
    - fun fact, there are in total ```62001757``` parameters of YOLOv3
    ![](https://i.imgur.com/7D9j4Tu.png)
    ![](https://i.imgur.com/Y5feG5t.png)
    ![](https://i.imgur.com/N7vgIhC.png)
- At least, in the future, we can separate our training process if needed
  - we can "save checkpoint" for every epoch or every 10, 20 epochs
  - **but the correctness of doing so is unsure**, what I mean unsure is that say we already train for 100 epochs and achieve centain level of preformance, but if we stop and continue the training for another 100 epochs, the performance may drop
  - **remember** to test it with ```seed_everything()``` and make sure it works
- Need to find a newer dependency
  - **Currently run without CUDA** support since there will be PyTorch 2.0 updates soon
  - [Deprecation of CUDA 11.6 and Python 3.7 Support](https://pytorch.org/blog/deprecation-cuda-python-support/?utm_content=236805635&utm_medium=social&utm_source=linkedin&hss_channel=lcp-78618366)
    - Please note that as of **Feb 1**, **CUDA 11.6 and Python 3.7 are no longer included** in the Stable CUDA
  - There is a new paper that says their model can learn spatial and temporal relationships between frames by leveraging the characteristics of the FMCW radar signal
    - Decourt, Colin, et al. "[A recurrent CNN for online object detection on raw radar frames](https://arxiv.org/abs/2212.11172)." *arXiv preprint arXiv:2212.11172* (2022).
  - The comparison between different generations showed that, though newer versions of the model may be more complex, they are not necessarily bigger
    - YOLOv3 ```222``` layers, ```62001757``` parameters
    - YOLOv4 ```488``` layers, ```64363101``` parameters
      - YOLOv4-CSP ```516``` layers, ```52921437``` parameters
    - YOLOv7 ```314``` layers, ```36907898``` parameters
- Future works
  - Make sure we can properly run ```train.py``` with radar dataset
  - Find a proper way to measure the "communication overhead"
    - e.g. compute from feature map shape
        ![](https://i.imgur.com/xq0h7jk.png)
  - Test the functionality of  ```seed_everything()```, check if it works like the way we think
  - Find a newer stable PyTorch and CUDA version for the project
- ```detect.py```
  - bunch of boilerplate codes, hard to maintain and debug
![](https://i.imgur.com/tsA5N6H.png)
![](https://i.imgur.com/hfLQh1E.png)
![](https://i.imgur.com/dw2ycec.png)



## **02/07**
- 2023.02.07
  - The code ```detect.py``` and ```model_with_weights2.py``` works fine, but the result may not be the way as we expected
  - Need to figure out the usability of the converted weights, since there is a huge difference between random weights and the converted weights, maybe it's not complete garbage



## **02/06**
- 2023.02.06
  - On lab PC, create a new env ```pt3.7``` through command ```conda create --name pt3.7 python=3.7```
    - to use the env ```conda activate pt3.7```
    - to leave the env ```conda deactivate```
    - actual env and pkgs locates at ```C:\Users\Paul\.conda\envs\pt3.7```, don't know why it is not been stored in ```D Drive```
  - Upgrade default conda env ```base``` through command ```conda update -n base -c defaults conda```
    <img src='https://i.imgur.com/6JozbHB.png' width=90% height=90%>
    - It has to be done under ```(base) C:\Windows\system32>```
    <img src='https://i.imgur.com/cYJM1XN.png' width=80% height=80%>
  - Install all the packages through ```pip install -r requirements.txt```
    - content in the requirements file
        ```python
        numpy>=1.19.2
        matplotlib>=3.3.4
        torch>=1.7.1
        tqdm>=4.56.0
        torchvision>=0.8.2
        albumentations>=0.5.2
        pandas>=1.2.1
        Pillow>=8.1.0
        ```
    - cmd output stored as ```D:/Datasets/YOLOv3-PyTorch/logs/installation_logs_0206.txt```
    - actual dependency, the new requirement is:
        ```python
        numpy==1.21.6
        matplotlib==3.5.3
        torch==1.13.1
        tqdm==4.64.1
        torchvision==0.14.1
        albumentations==1.3.0
        pandas==1.3.5
        Pillow==9.4.0
        ```
  - Currently run without CUDA support since there will be PyTorch 2.0 updates soon
    - [Deprecation of CUDA 11.6 and Python 3.7 Support](https://pytorch.org/blog/deprecation-cuda-python-support/?utm_content=236805635&utm_medium=social&utm_source=linkedin&hss_channel=lcp-78618366)
    - **Please note that as of Feb 1, CUDA 11.6 and Python 3.7 are no longer included**
  - Run ```model_with_weights2.py``` again on lab PC to generate the weights in PyTorch format
    - we name the output weights as ```checkpoint-2023-02-06.pth.tar``` also stored in the same directory
    ![](https://i.imgur.com/WAncq96.png)
  - Wanted to test the training ability using ```PASCAL_VOC``` dataset
    - download the preprocessed ```PASCAL_VOC``` dataset from [kaggle](https://www.kaggle.com/datasets/aladdinpersson/pascal-voc-dataset-used-in-yolov3-video)
    - download the preprocessed ```MS-COCO``` dataset from [kaggle](https://www.kaggle.com/datasets/79abcc2659dc745fddfba1864438afb2fac3fabaa5f37daa8a51e36466db101e)
  - But first, we have to test the converted weights to check if they actually work
    - to do so, maybe we could write a program ```detect.py``` and test the weights with some inference samples
    - if it can predict perfectly, then we may assume it is converted correctly
    - Okay, it does not work..., the inference outputs are bunch of random tags




## **02/05**
- 2023.02.05
  - The original code repository [YOLOv3-PyTorch](https://github.com/SannaPersson/YOLOv3-PyTorch)
  - first download the YOLOv3 weights from https://pjreddie.com/media/files/yolov3.weights as ```yolov3.weights``` and put it at the same directory
  - then run ```model_with_weights2.py```, it will save the weights to PyTorch format
    - we name the output weights as ```checkpoint-2023-02-05.pth.tar``` also in the same directory
    <img src='https://user-images.githubusercontent.com/95068443/216808211-7a95bcdf-4444-4116-965b-6462cb20646a.png' width=90% height=90%>
  - I override most of the files with my previous ones, except for ```model_with_weights2.py```





## **Top Publications Ranking**
- We can search the ranking of the top publications from google scholar
  - [Engineering & Computer Science](https://scholar.google.es/citations?view_op=top_venues&hl=en&vq=eng)
    - [Artificial Intelligence](https://scholar.google.es/citations?view_op=top_venues&hl=en&vq=eng_artificialintelligence)
    - [Computer Networks & Wireless Communication](https://scholar.google.es/citations?view_op=top_venues&hl=en&vq=eng_computernetworkswirelesscommunication)
    - [Computer Vision & Pattern Recognition](https://scholar.google.es/citations?view_op=top_venues&hl=en&vq=eng_computervisionpatternrecognition)
    - [Radar, Positioning & Navigation](https://scholar.google.es/citations?view_op=top_venues&hl=en&vq=eng_radarpositioningnavigation)
    - [Signal Processing](https://scholar.google.es/citations?view_op=top_venues&hl=en&vq=eng_signalprocessing)
  - [Physica & Mathmematics](https://scholar.google.es/citations?view_op=top_venues&hl=en&vq=phy)
  - [Chemical & Material Sciences](https://scholar.google.es/citations?view_op=top_venues&hl=en&vq=chm)




## **Worth Noting Researchers**
- **PhD**
  - [Chia-Hung Lin](https://ieeexplore.ieee.org/author/37087085396)
    - C. -H. Lin, Y. -C. Lin, Y. Bai, W. -H. Chung, T. -S. Lee and H. Huttunen, "[DL-CFAR: A Novel CFAR Target Detection Method Based on Deep Learning](https://ieeexplore.ieee.org/document/8891420)," *2019 IEEE 90th Vehicular Technology Conference (VTC2019-Fall)*, Honolulu, HI, USA, 2019, pp. 1-6.
    - C. -H. Lin et al., "[GCN-CNVPS: Novel Method for Cooperative Neighboring Vehicle Positioning System Based on Graph Convolution Network](https://ieeexplore.ieee.org/document/9614197)," in IEEE Access, vol. 9, pp. 153429-153441, 2021. (莠繪)
  - [Yu-Chein Lin](https://ieeexplore.ieee.org/author/37086483408)
  - [Hsin-Yuan Chang](https://ieeexplore.ieee.org/author/37087022655)
    - H. -Y. Chang, Y. -Y. Chen and W. -H. Chung, "[RangeSRN: Range Super-Resolution Network Using mmWave FMCW Radar](https://ieeexplore.ieee.org/document/10000943)," *GLOBECOM 2022 - 2022 IEEE Global Communications Conference*, Rio de Janeiro, Brazil, 2022, pp. 1-6. (逸衍)
    - H. -Y. Chang, C. -H. Hsu and W. -H. Chung, "[Fast Acquisition and Accurate Vital Sign Estimation with Deep Learning-Aided Weighted Scheme Using FMCW Radar](https://ieeexplore.ieee.org/document/9860799)," *2022 IEEE 95th Vehicular Technology Conference: (VTC2022-Spring)*, Helsinki, Finland, 2022, pp. 1-6. (芷瑄)
    - K. -Y. Chen, H. -Y. Chang, R. Y. Chang and W. -H. Chung, "[Hybrid Beamforming in mmWave MIMO-OFDM Systems via Deep Unfolding](https://ieeexplore.ieee.org/document/9860467)," *2022 IEEE 95th Vehicular Technology Conference: (VTC2022-Spring)*, Helsinki, Finland, 2022, pp. 1-7. (管元)
    - W. -Y. Chen, H. -Y. Chang, C. -Y. Wang and W. -H. Chung, "[Cooperative Neighboring Vehicle Positioning Systems Based on Graph Convolutional Network: A Multi-Scenario Transfer Learning Approach](https://ieeexplore.ieee.org/document/9838627)," *ICC 2022 - IEEE International Conference on Communications*, Seoul, Korea, Republic of, 2022, pp. 3226-3231. (宛妤)
    - C. -H. Kuo, H. -Y. Chang, R. Y. Chang and W. -H. Chung, "[Unsupervised Learning Based Hybrid Beamforming with Low-Resolution Phase Shifters for MU-MIMO Systems](https://ieeexplore.ieee.org/document/9839096)," *ICC 2022 - IEEE International Conference on Communications*, Seoul, Korea, Republic of, 2022, pp. 425-431. (嘉和)
    - S. -C. Fan, H. -Y. Chang, C. -Y. Wang and W. -H. Chung, "[Super Resolution-Based Beam Selection With Hierarchical Codebook in mmWave Communication](https://ieeexplore.ieee.org/document/9714481)," in *IEEE Wireless Communications Letters*, vol. 11, no. 5, pp. 967-971, May 2022. (聖群)
    - C. -H. Lin et al., "[GCN-CNVPS: Novel Method for Cooperative Neighboring Vehicle Positioning System Based on Graph Convolution Network](https://ieeexplore.ieee.org/document/9614197)," in *IEEE Access*, vol. 9, pp. 153429-153441, 2021. (莠繪)
    - H. -Y. Chang, C. -H. Lin, Y. -C. Lin, W. -H. Chung and T. -S. Lee, "[DL-Aided NOMP: a Deep Learning-Based Vital Sign Estimating Scheme Using FMCW Radar](https://ieeexplore.ieee.org/document/9128552)," *2020 IEEE 91st Vehicular Technology Conference (VTC2020-Spring)*, Antwerp, Belgium, 2020, pp. 1-7.
  - [Jiawei Shao](https://ieeexplore.ieee.org/author/37088447290)
    - J. Shao and J. Zhang, "[BottleNet++: An End-to-End Approach for Feature Compression in Device-Edge Co-Inference Systems](https://ieeexplore.ieee.org/document/9145068)," *2020 IEEE International Conference on Communications Workshops (ICC Workshops)*, Dublin, Ireland, 2020, pp. 1-6. 
    - J. Shao and J. Zhang, "[Communication-Computation Trade-off in Resource-Constrained Edge Inference](https://ieeexplore.ieee.org/document/9311935)," in *IEEE Communications Magazine*, vol. 58, no. 12, pp. 20-26, December 2020.
    - J. Shao, H. Zhang, Y. Mao and J. Zhang, "[Branchy-GNN: A Device-Edge Co-Inference Framework for Efficient Point Cloud Processing](https://ieeexplore.ieee.org/document/9414831)," *ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, Toronto, ON, Canada, 2021, pp. 8488-8492.
- **Professors**
  - [Wei-Ho Chung](https://ieeexplore.ieee.org/author/37538749800)
  - [Chih-Yu Wang](https://ieeexplore.ieee.org/author/37085674145)
  - [Yuyi Mao](https://ieeexplore.ieee.org/author/37085508893)
  - [Jun Zhang](https://ieeexplore.ieee.org/author/37407590900)
  - [Jung-Chieh Chen](https://ieeexplore.ieee.org/author/37280673400)
  - [Thomas Oberlin](https://ieeexplore.ieee.org/author/38232257200)
    - C. Decourt, R. VanRullen, D. Salle and T. Oberlin, "[DAROD: A Deep Automotive Radar Object Detector on Range-Doppler maps](https://ieeexplore.ieee.org/document/9827281)," *2022 IEEE Intelligent Vehicles Symposium (IV)*, Aachen, Germany, 2022, pp. 112-118.
