# **meeting 03/21**

**Advisor: Dr. Chih-Yu Wang \
Presenter: Shao-Heng Chen \
Date: March 21, 2023**


## **Current progress**
- It's finally trainable now
    ![](https://i.imgur.com/Q8anAyR.png)
  - Some samples of person, cyclist and car:
    ![](https://i.imgur.com/2axeJNC.jpg)
    ![](https://i.imgur.com/w3ivjzM.jpg)
    ![](https://i.imgur.com/bbIMrqB.jpg)
- I first tried to run ```train.py``` for ```100``` epochs with the following config settings:
    ![](https://i.imgur.com/M2u8BtK.png)
- The resulted ```mAP``` is ```0.182485```
    ![](https://i.imgur.com/eGgLni0.png)
    ![](https://i.imgur.com/faPMJob.png)




## **Issue summary**
- The training images don't have to be in square size, but they have to be in ```.jpg``` format
  - The actual size of each input image is: 
    - ```875-by-1489``` or ```310-by-1240```
    ![](https://i.imgur.com/Cjg1AiQ.png)
- The major mistakes that I made were: Misinterpreting the labels, but actually translating them correctly.
    - In short, simply switching the ```x``` and ```y``` coordinates will solve our problems
    - This makes me wonder, How did I get it right when replicating ```YOLO-CFAR``` before?
      - Since the shape of the feature map is printed as ```torch.Size([256, 64, 3])```, it shows the same coordinate system as the ```RD map``` where the origin ```(0, 0)``` is located at the top left corner
      - But it turns out that's not the case. The model still recognizes the bottom left corner as the origin, which is the same as we usually do.
- The resizing results are completely different. 
  - We could even conclude that they are wrong (and I don't know why), since we might not need to resize images anymore. 
  - Currently, I am just ignoring this issue
  ![](https://i.imgur.com/QoYz9TP.jpg)
  ![](https://i.imgur.com/wexdIfa.png)



## **Appendix**
- The correct way to translate the labels ```resize_labels.py```
    ![](https://i.imgur.com/DoAn99t.png)
    ![](https://i.imgur.com/skwA1D3.png)
- The code for extracting the data from the log files ```read_logs.py```
    ![](https://i.imgur.com/yzPEsUE.png)
    ![](https://i.imgur.com/CEeq9LO.png)
    ![](https://i.imgur.com/EGTWlkP.png)
    ![](https://i.imgur.com/XIehPQV.png)




