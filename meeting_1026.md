# **meeting 10/26**
Advisor: Dr. Chih-Yu Wang
Presenter: Shao-Heng Chen
Date: October 26, 2022

## **Original goals**
- 可以用 ```CARRADA Dataset``` 的資料讓 ```YOLOv3``` 跑起來
- 至少先確認可以解決 ```RD Map``` 的 "多目標 多類別" 偵測問題，因為 ```RA Map``` 的部分超難

## **Approaches**
- 重寫 ```DataLoader```，就是重刻一個可以讀 ```COCO format``` 的 ```DataLoader``` 
  - 但要改```config.py```, ```dataset.py```, ```train.py```，幾乎跟寫新的差不多
<img src=https://i.imgur.com/SlqIUyK.png width=100% height=75%>
- 找新的 ```YOLOv3``` ，直接找另一個可以讀 ```COCO format``` 的 ```YOLOv3``` 把東西跑起來
  - 要把另一個現成的 ```YOLOv3``` 跑起來並確認基本的正確性
  - 無法確定可以讀現有的 ```JSON string``` 格式的 annotation，畢竟 ```CARRADA Dataset``` 的格式跟標準的 ```COCO format``` 也不太一樣
  - 一開始選擇客製化、輕量化的設計就是為了之後可能要做模型切割、壓縮的方便性
- 離線資料處理，把 annotation 從 ```COCO format``` 整理成 ```YOLO foramt```，餵進之前確認過大致可行的 ```YOLOv3``` 看看成效
  - 選項一 [coco2yolo](https://github.com/tw-yshuang/coco2yolo)
  - 選項二 [pylabel](https://github.com/pylabel-project/pylabel)
  - 選項三 自己造輪子

## **Offline preprocessing**
- 目前有 3 個想法可以試試看
  - 先從 ```json file``` 把有 ```bbox annotation``` 的字串 parse 出來，重新換算為 ```YOLO format``` 並存成 ```.txt file```
    - ```COCO format``` 的 ```json string``` 給的是絕對大小!
    - 訓練資料圖片大小為 ```64-by-256``` 或 ```310-by-1240``` 的長方形
  - 把 parse 出來的 ```annotation``` 重新 rescale 成 ```256-by-256``` 的大小，也就是把 x 軸 (Doppler 軸) 拉長或放大 4 倍，好方便直接餵進之前的 ```YOLOv3```，因為不確定餵長方形 ```(64-by-256)``` 的圖片的 ```feature map size``` 對不對得上
    - 訓練資料圖片大小為 ```256-by-256``` 或 ```1240-by-1240``` 的正方形
  - 把同一張 ```256-by-256``` 的圖片保持不變切成 4 張，每張都是 ```64-by-64```，但很有可能滿多圖片會變成沒有目標
    - 為此是否多考慮 "沒有目標" 的情況

## **Issues**
- 標記缺失問題
  - ```CARRADA Dataset```  裡 ```bounding box``` 的標記有少
  - e.g. ```2020-02-28-13-09-58``` 影像有 ```232```  張、有目標的只有 ```000 069~000 231``` 共 ```162```張，但 ```boxes``` 只有 ```000 035~000 177``` 共 ```142``` 張，至少 ```RD Map``` 跟 ```RA Map``` 應該是缺一樣的資料。
  - 有的 frame 是 ```RD Map``` 跟 ```RA Map```  有資料，但對應的影像資料 ```.jpg``` 中是沒有物體的!
- 多目標問題
  - 也許可以考慮 "沒有目標" 的情況?
  - ```CARRADA Dataset``` 的多目標看起來滿稀疏且大小目標在 ```RD Map``` 上看起來差不多
    - 也許可以試試看合成類似的 ```RD Map``` 
- ```Anchor box``` 大小問題
  - 因為現在的 ```bounding box``` 不再是固定 ```0.125-by-0.125``` 得重新計算
- 之前 ```YOLOv3``` 原有的問題
  - 有很多 ```unfixed bugs!``` 而且在自己電腦跟在學校電腦的執行結果不一樣!!
  - 用 ```CPU``` 跑的跟 ```GPU``` 跑的結果不一樣，是 ```albumentation``` 的預期結果不一樣
  - 理論上原電腦用 ```CPU``` 跑的才是正確的，但那台現在已經呈報廢狀態

## **Conclusion**
- **Pipeline**
  - 把部分資料集裡面有 ```bbox annotation``` 的 frame 的資料取出來
  - 把標記換算為 ```YOLO format``` 並存成 ```.txt file```
  - 把對應的 ```RD Map``` 存成 ```.png```
- 先確認至少能跑再整理全部的資料集，整合成一個完整的版本

## **Note**
- 如果說某張 ```RD Map``` 的維度 ```m-by-n``` 是指 ```Range``` 軸 (y軸) 的維度為 ```m```、```Doppler``` 軸 (x軸) 的維度為 ```n```，剛好跟圖片相反，```RA Map``` 同理。
- 透過影像資料確認正確性的作法得重新考慮


