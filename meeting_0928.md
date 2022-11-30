# **meeting 09/28**
Advisor: Dr. Chih-Yu Wang
Presenter: Shao-Heng Chen
Date: September 28, 2022
## **Original goals**
- establish entry point for using CARRADA Dataset
  - failed
- discuss the pros and cons of using real dataset and of using simluated data with Prof. Chung
  - also failed


### **CARRADA Dataset**
- CARRADA Dataset 在 IEEE 有 [8](https://ieeexplore.ieee.org/document/9413181/citations?tabFilter=papers#citations) 篇文章引用，在 google scholar 可以找到 [43](https://scholar.google.com.tw/scholar?cites=4617103630695360689&as_sdt=2005&sciodt=0,5&hl=zh-TW) 篇。
- R. Zheng, S. Sun, D. Scharff and T. Wu, "[Spectranet: A High Resolution Imaging Radar Deep Neural Network for Autonomous Vehicles](https://ieeexplore.ieee.org/document/9827798)," *2022 IEEE 12th Sensor Array and Multichannel Signal Processing Workshop (SAM)*, 2022, pp. 301-305.
  - design a novel transmit and receive signal processing pipeline of imaging radar systems to generate high resolution radar spectra from raw data
  - construct a high resolution radar RA spectra dataset that encodes the critical details of object's shape
  - propose a vanilla SpectraNet to detect moving targets of interests, based on their dataset
![](https://i.imgur.com/ibEgHIG.png)
![](https://i.imgur.com/ErZ1Bmk.png)
![](https://i.imgur.com/E2DjAY9.png)
<!-- - C. Grimm, T. Fei, E. Warsitz, R. Farhoud, T. Breddermann and R. Haeb-Umbach, "[Warping of Radar Data Into Camera Image for Cross-Modal Supervision in Automotive Applications](https://ieeexplore.ieee.org/document/9797876)," in *IEEE Transactions on Vehicular Technology*, vol. 71, no. 9, pp. 9435-9449, Sept. 2022. -->



### **Brief Introduction of FMCW Radar**
- 常見低成本 FMCW 雷達平台有 AWR 1x系列 跟 IWR 1x系列，可對應於 一般傳感器 和 ADAS 的 76-81-GHz 傳感器陣列
  - AWR 1642 EVM module 是眾多參考設計基礎，該開發板是基於PCB板的天線系統，有配置用於添加外圍設備的 TI BoosterPack連接器，常見外圍設備如通訊裝置、傳感器、無線行動通訊應用等等
  - [AWR 1642](https://www.ti.com/product/AWR1642#params) 雷達的主要元件有 C674x DSP processor 和 ARM-Cortex R4F CPU ，另外通常會配合 [DCA1000EVM](https://www.ti.com/tool/DCA1000EVM) 雷達數據採集卡使用
  - AWR 1642 附有DSP及SDK軟體可以濾除雜訊、分析車輛周邊環境、生成目標物的熱圖(頻譜圖)、檢查傳感器的周邊區域的目標物的特徵，視野角是 120 度
  - AWR 1x系列批發價是 299 美金，工業級 IWR 1x系列批發價是 135 美金
    - IWR 常用於工業生產、室內定位、照明和冷暖氣空調系統
- AWR1642Boost
  - [AWR1642](https://www.ti.com/product/AWR1642#features) 德州儀器官網介紹，售價 NT$12,689，散裝，有現貨
  - 實驗室之前好像是用這款
  - SDK [AWR1642-Read-Data-Python-MMWAVE-SDK-2](https://github.com/ibaiGorordo/AWR1642-Read-Data-Python-MMWAVE-SDK-2)
- AWR1843Boost 
  - [AWR1843](https://www.ti.com/product/AWR1843) 德州儀器官網介紹，售價 NT$12,689，盒裝，無現貨
  - SDK [AWR1843-Read-Data-Python-MMWAVE-SDK-3](https://github.com/ibaiGorordo/AWR1843-Read-Data-Python-MMWAVE-SDK-3-)


