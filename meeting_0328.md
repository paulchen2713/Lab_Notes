# **meeting 03/28**

**Advisor: Dr. Chih-Yu Wang \
Presenter: Shao-Heng Chen \
Date: March 28, 2023**


## **Current progress**
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







