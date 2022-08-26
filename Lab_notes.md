# Lab notes
## Literature review
### First Year
- 11/29 
  - J. Shao and J. Zhang, "[Communication-Computation Trade-off in Resource-Constrained Edge Inference](https://ieeexplore.ieee.org/document/9311935)," in *IEEE Communications Magazine*, vol. 58, no. 12, pp. 20-26, December 2020. (cited by 38)
  - github repo [Edge_Inference_three-step_framework](https://github.com/shaojiawei07/Edge_Inference_three-step_framework)
  - 3個步驟分別是: 
    - (1) model splitting 考慮 data amplification effect 去選切割點
    - (2) compress on-device model 考慮 channel-wised sparsity ratio 去做 structured pruning
    - (3) intermidiate feature encoding 透過 BottleNet++ 做 JSCC 的壓縮及通道雜訊保護
  - 主流方案考慮 bit width 選切割點，利用 quantization 跟 mixed precision 壓縮，沒額外考慮無線通訊時的干擾，因為他們的機制可以跟現有的通訊協定共生，以實用性為考量
- 01/05 
  - J. Chen and X. Ran, "[Deep Learning With Edge Computing: A Review](https://ieeexplore.ieee.org/document/8763885)," in *Proceedings of the IEEE*, vol. 107, no. 8, pp. 1655-1674, Aug. 2019. (cited by 582)
  - 過時的 review paper
- 02/09 
  - N. Shlezinger, E. Farhan, H. Morgenstern and Y. C. Eldar, "[Collaborative Inference via Ensembles on the Edge](https://ieeexplore.ieee.org/document/9414740)," *ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2021, pp. 8478-8482. (cited by 6)
  - 沒考慮隱私及資安問題
- 02/23 
  - J. Song, Z. Liu, X. Wang, C. Qiu and X. Chen, "[Adaptive and Collaborative Edge Inference in Task Stream with Latency Constraint](https://ieeexplore.ieee.org/document/9500892)," *ICC 2021 - IEEE International Conference on Communications*, 2021, pp. 1-6. (cited by 2)
  - 用DRL解資源分配的最佳化問題，這類MEC資源分配問題已經被解得差不多了
  - Optimal solution是DP解, Baseline是greedy, 什麼都不做是random
- 03/23 
  - J. Shao, H. Zhang, Y. Mao and J. Zhang, "[Branchy-GNN: A Device-Edge Co-Inference Framework for Efficient Point Cloud Processing](https://ieeexplore.ieee.org/abstract/document/9414831)," *ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2021, pp. 8488-8492. (cited by 10)
  - github repo [Branchy-GNN](https://github.com/shaojiawei07/Branchy-GNN)
  - 覺得 early exit 的設計值得參考，雖然主流方案會因為 inconsistency 而不用 model pruning 或 early exit 等機制
- 04/06 
  - J. Shao and J. Zhang, "[BottleNet++: An End-to-End Approach for Feature Compression in Device-Edge Co-Inference Systems](https://ieeexplore.ieee.org/abstract/document/9145068)," *2020 IEEE International Conference on Communications Workshops (ICC Workshops)*, 2020, pp. 1-6. (cited by 53)
  - github repo [BottleNetPlusPlus](https://github.com/shaojiawei07/BottleNetPlusPlus)
  - 將 edge 要傳輸的 feature map 等資料經過預先訓練好的一組 auto-encoder 來壓縮，特點是有考慮不同種通道雜訊的影響，如 AWGN channel, BEC channel
  - 主流方案是利用 quantization 跟 mixed precision training 來壓縮，像 FP2, 4, 8, 16 對 FP32
  - Micikevicius, Paulius, et al. "[Mixed precision training](https://arxiv.org/pdf/1710.03740.pdf)." *arXiv preprint arXiv:1710.03740* (2017). (cited by 919)
- 04/20 
  - A. E. Eshratifar, A. Esmaili and M. Pedram, "[BottleNet: A Deep Learning Architecture for Intelligent Mobile Cloud Computing Services](https://ieeexplore.ieee.org/abstract/document/8824955)," *2019 IEEE/ACM International Symposium on Low Power Electronics and Design (ISLPED)*, 2019, pp. 1-6. (cited by 73)
    - 第1個(?)提出用 auto-encoder 來壓縮 intermediate feature 主要考慮 lossless compression method 所以壓縮倍率不高 
  - E. Bourtsoulatze, D. Burth Kurka and D. Gündüz, "[Deep Joint Source-Channel Coding for Wireless Image Transmission](https://ieeexplore.ieee.org/abstract/document/8723589)," in *IEEE Transactions on Cognitive Communications and Networking*, vol. 5, no. 3, pp. 567-579, Sept. 2019. (cited by 190)
    - 可以用 trainable layer 來模擬 Rayleigh fading channel 的影響 
    - 希望能學習到如何將複雜的通道衰變數學模型以 NN layers 表示
- 05/04 
  - M. Yang, C. Bian and H. -S. Kim, "[Deep Joint Source Channel Coding for Wireless Image Transmission with OFDM](https://ieeexplore.ieee.org/abstract/document/9500996)," *ICC 2021 - IEEE International Conference on Communications*, 2021, pp. 1-6. (cited by 14)
  - github repo [Deep-JSCC-for-images-with-OFDM](https://github.com/mingyuyng/Deep-JSCC-for-images-with-OFDM)
    - 包含 OFDM extension 的 Deep JSCC 設計，考慮 multi-path fading channel 影響，這篇沒仔細讀完
- 05/18 
  - C. -H. Lin, Y. -C. Lin, Y. Bai, W. -H. Chung, T. -S. Lee and H. Huttunen, "[DL-CFAR: A Novel CFAR Target Detection Method Based on Deep Learning](https://ieeexplore.ieee.org/abstract/document/8891420)," *2019 IEEE 90th Vehicular Technology Conference (VTC2019-Fall)*, 2019, pp. 1-6. (cited by 18)
- 06/29 
  - 林郁庭(2021)。YOLO-CFAR: a Novel CFAR Target Detection Method Based on YOLO。國立清華大學通訊工程研究所碩士論文，新竹市。取自 [基於YOLO之雷達目標偵測演算法](https://hdl.handle.net/11296/7n49t5)
- 07/06, 07/13, 07/20, 07/27, 08/03 
  - YOLO-CFAR reproduction
    - YOLOv3 implementation [YOLO_project](https://github.com/paulchen2713/YOLO_project)
    - RD map data generation [DL_CFAR_data
](https://github.com/paulchen2713/DL_CFAR_data)


### 08/15
- 在 read this paper 網站搜尋 "[DL CFAR](https://readthispaper.com/tw/search?p=4&q=DL+CFAR)" 找到第[3.](https://readthispaper.com/tw/paper/9ff2b88acff214a97b02dce187993d903374bf44/overview)篇，想繼續找cite這篇的文章，然後找到第2.篇，再往下找發現第1.篇。
- 文章關係是第1.篇cite第2.篇，第2.篇cite第3.篇。
- 這3篇都沒有附code。
1. T. Diskin, U. Okun and A. Wiesel, "[Learning to Detect with Constant False Alarm Rate](https://ieeexplore.ieee.org/document/9834032)," *2022 IEEE 23rd International Workshop on Signal Processing Advances in Wireless Communication (SPAWC)*, 2022, pp. 1-5 
   - 這篇有引用 DL-CFAR
2. J. Akhtar, "[Training of Neural Network Target Detectors Mentored by SO-CFAR](https://ieeexplore.ieee.org/abstract/document/9287495)," *2020 28th European Signal Processing Conference (EUSIPCO)*, 2021, pp. 1522-1526 
3. J. Akhtar and K. E. Olsen, "[GO-CFAR Trained Neural Network Target Detectors](https://ieeexplore.ieee.org/document/8835765)," *2019 IEEE Radar Conference (RadarConf)*, 2019, pp. 1-5 
4. J. Akhtar and K. E. Olsen, "[A Neural Network Target Detector with Partial CA-CFAR Supervised Training](https://ieeexplore.ieee.org/document/8557276)," *2018 International Conference on Radar (RADAR)*, 2018, pp. 1-6 
   - 作者 Jabran Akhtar 出了3篇 傳統CFAR detector輔助的NN target detecor論文，分別是2018年CA-CFAR在RadarConf, 2019年SO-CFAR在EUSIPCO, 跟2021年GO-CFAR在RadarConf 
   - [Jabran Akhtar](https://ieeexplore.ieee.org/author/37533801900) 是 Norwegian Defence Research Establishment (FFI) 的研究員，專長是雷達。挪威國防研究機構是一家研究機構，代表挪威武裝部隊進行研究和開發，並為政治和軍事防禦領導人提供專家建議。


### 08/16
- 直接google "yolo model splitting" 第一頁就看到 Auto-Split 論文，然後再去 read this paper 搜尋論文名稱，找到第[1.](https://readthispaper.com/tw/paper/9a3fa28855b6b3df9652938ccb13bfaacc346192/overview#Reading-Order)篇，2021年8月發表在ACM，目前被引用次數有5次。
  - 作者 Amin Banitalebi-Dehkordi 前Huawei研究員、現任Amazon Applied Science Manager。連結: [LinkedIn](https://ca.linkedin.com/in/amin-banitalebi-dehkordi-42888999?original_referer=https%3A%2F%2Fwww.google.com%2F), [Google Scholar](https://scholar.google.com/citations?user=fSz1PtYAAAAJ&hl=en), [IEEE Xplore Author Details](https://ieeexplore.ieee.org/author/37074168400)
  - Auto-Split 已經部屬在華為雲 [Auto-Split: Edge Cloud Collaboration](https://developer.huaweicloud.com/develop/aigallery/notebook/detail?id=5fad1eb4-50b2-4ac9-bcb0-a1f744cf85c7)
1. Amin Banitalebi-Dehkordi, Naveen Vedula, Jian Pei, Fei Xia, Lanjun Wang, and Yong Zhang. [Auto-Split: A General Framework of Collaborative Edge-Cloud AI](https://dl.acm.org/doi/abs/10.1145/3447548.3467078), 14 August 2021, *In Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery & Data Mining (KDD '21)*.


### 08/17
### **Top Publications Ranking**
- 可以從 google scholar 查詢 top publications 的排名
  - [Engineering & Computer Science](https://scholar.google.es/citations?view_op=top_venues&hl=en&vq=eng)
    1. [Artificial Intelligence](https://scholar.google.es/citations?view_op=top_venues&hl=en&vq=eng_artificialintelligence)
    2. [Computer Networks & Wireless Communication](https://scholar.google.es/citations?view_op=top_venues&hl=en&vq=eng_computernetworkswirelesscommunication)
    3. [Computer Vision & Pattern Recognition](https://scholar.google.es/citations?view_op=top_venues&hl=en&vq=eng_computervisionpatternrecognition)
    4. [Radar, Positioning & Navigation](https://scholar.google.es/citations?view_op=top_venues&hl=en&vq=eng_radarpositioningnavigation)
    5. [Signal Processing](https://scholar.google.es/citations?view_op=top_venues&hl=en&vq=eng_signalprocessing)
  - [Physica & Mathmematics](https://scholar.google.es/citations?view_op=top_venues&hl=en&vq=phy)
  - [Chemical & Material Sciences](https://scholar.google.es/citations?view_op=top_venues&hl=en&vq=chm)
- 跟王老師開會討論後總結出的近期目標(下次meeting是兩週後 8/31)
  1. 測試YOLO-CFAR於不確定數量的多目標偵測 
  2. 了解有哪些值得解的雷達訊號處理的問題 radar signal processing
  3. 了解邊緣部屬的隱私問題跟解法 secure communication?


### 08/18
- 早上在寫 [sort_binary_search](https://github.com/paulchen2713/Practices/tree/main/sort_binary_search) 的練習，memory free 還沒寫完。
- 今天文獻搜尋目標是找 "有哪些值得解的雷達訊號處理的問題?" 對各問題有基礎的了解並整理成清楚條列的表格(? 好在下週四 meeting 跟學姊還有鍾老師討論。
- 不希望用其他人現成的雷達資料集 (e.g. SAR Image)，最好是我們可以設計自己的系統模型 (system model)，形塑我們想解的問題 (formulate our problem)，並自己產模擬資料 / 訓練資料，整理成自己的資料集(generate our own dataset)。
- 但又不是自己憑空設想的，不然很難說服 reviewer 這是一個值得解的問題，跟之前找資源分配問題同理，想找到一個能參考的流程。
1. A. Zhang, F. E. Nowruzi and R. Laganiere, "[RADDet: Range-Azimuth-Doppler based Radar Object Detection for Dynamic Road Users](https://ieeexplore.ieee.org/document/9469418)," *2021 18th Conference on Robots and Vision (CRV)*, 2021, pp. 95-102.
   - [paper with code](https://paperswithcode.com/paper/raddet-range-azimuth-doppler-based-radar)
   - [read this paper](https://readthispaper.com/tw/paper/1bf79b8eae12359d2d85d193bf73cde8f6c58a41/overview)
   - [github](https://github.com/ZhangAoCanada/RADDet)


### 08/22
- 發現 `sort_binary_search` 練習有2個大bug
1. 是 `displayTree()` 不會印出全部結果，只會大致印出全部值域範圍內的值，有的重複值會被印出，有的不會，因為 default 的 binary search tree 不考慮有 duplicate 的情況，在存的時候會直接覆寫掉相同key存的value (且測資裡有很多重複值)。所以讀寫 duplicate values 的動作是未定義行為，也解釋上述 "有的會被印出，有的不會" 的現象。
2. 是 `search()` 只能找到某個等於val的元素的key(也不確定是第幾個，第1個回傳的不一定是第1次出現的)，自然沒辦法列出所有等於val的元素
- 目前解法就回到最直接的方式
1. 先用`hashmap`記錄`key`對`val`的映射 `std::unordered_map<std::string, int>` (其實可以直接用陣列存映射就好 `std::vector<std::pair<std::string, int>>` 因為我本來是先用`rb_tree`(`std::map`)發現不行，要改回來直接加`unordered_`在前面即可XD)，做為暫存緩衝。
2. 然後寫一個`sort()`對`val`排序(目前先用`std::sort()`測試，如果可行再換成自己寫的 sort )。為了用`std::sort()`排序，得先轉成`std::vector`排序完回傳，且既然都轉成陣列就不必再轉回`std::unordered_map`。
3. 然後再寫一個`binary_search()`搜尋`val`然後印出所有的`key`，但因為二元搜尋找到的不一定是第1次出現的位置，所以再寫一個`first_occur()`確定是重複元素的第1次出現的位置。
4. 然後寫一個`search()`整併`binary_search()`跟`first_occur()`的功能，先二元搜尋確定目標元素存在，接著確定第1次出現的位子，並從該位子開始逐個印出所有跟`val`相同的`key`就是我們要的答案。
- github repo [sort_binary_search](https://github.com/paulchen2713/Practices/tree/main/sort_binary_search)


### 08/23
- 常見低成本 FMCW 雷達平台有 AWR 1x系列 跟 IWR 1x系列，可對應於 一般傳感器 和 ADAS 的 76-81-GHz 傳感器陣列，參考[德州儀器單晶片毫米波雷達參考設計](http://www.ti-ic.xin/info/3699/104404.html), Aug 12, 2019.
  1. AWR 642 EVM module 是眾多參考設計基礎，該開發板是基於PCB板的天線系統，有配置用於添加外圍設備的TI BoosterPack連接器，常見外圍設備如通訊裝置、傳感器、無線行動通訊應用等等。
  2. AWR 642 用於集成 C 674 xDSP processor 和 ARM Cortex-64 F 並控制通訊。
  3. AWR 642 可用於車輛乘員探測系統，對車內人員進行調查。附有DSP軟體 (及SDK) 可以濾除雜訊、分析車輛周邊環境、生成對象物的熱圖、檢查傳感器的周邊區域的目標物的特徵，視野角(Field Of View, FOV)是120度。
  4. AWR 1x系列批發價是 45 美金，工業級 IWR 1x系列批發價是 20 美金。
  5. IWR 常用於工業生產、尋找樓內人、照明和冷暖氣空調系統。
- AWR1642 Boost
  - [AWR1642](https://www.digikey.tw/zh/products/detail/texas-instruments/AWR1642BOOST/9487449) 德州儀器官網介紹，售價 NT$12,689，散裝，有現貨。
  - 實驗室好像是用這款(不然就是 AWR642)，雖然好像已經壞掉? 也沒辦法實際用用看。 
  - [AWR1642-Read-Data-Python-MMWAVE-SDK-2](https://github.com/ibaiGorordo/AWR1642-Read-Data-Python-MMWAVE-SDK-2) Python program to read and plot the data in real time from the AWR1642 and IWR1642 mmWave radar boards.
- AWR1843Boost
  - [AWR1843](https://www.digikey.tw/zh/products/detail/texas-instruments/AWR1843BOOST/10445300?s=N4IgTCBcDaIIIHUBKBGAHAFgMwCED2eAzgC4gC6AvkA) 德州儀器官網介紹，售價 NT$12,689，盒裝，無現貨。
  - 依據 AWR1642 雷達規格，去模擬生成 Range-Azimuth Doppler, RAD 資料的 [github](https://github.com/ZhangAoCanada/FMCW_Radar_slam)，但還不確定能不能用。 
  - [AWR1843-Read-Data-Python-MMWAVE-SDK-3-](https://github.com/ibaiGorordo/AWR1843-Read-Data-Python-MMWAVE-SDK-3-)
- 在 github 搜尋 "[#fmcw](https://github.com/topics/fmcw)" 的 repo ~~找靈感~~ 找可以抄的code
  - [RadarSimPy](https://zpeng.me/index.php/2019/04/07/radarsimpy/) 
    - 貌似要付費的優質第三方python非open source函式庫。
    - github repo [radarsimpy](https://github.com/rookiepeng/radarsimpy)
  - [FMCW_Radar_slam](https://github.com/ZhangAoCanada/FMCW_Radar_slam/blob/master/illustration/README.md) 
    - 可生成 RAD 資料，屬公司私人財產，沒有公布所有程式碼跟數據。
  - [SAR Simulator](https://github.com/IMS-AS-LUH/sar-sim)
    - a graphical tool for FMCW radar simulation and interactive exploration of parameters. 
    - 還不確定能不能用。
  - [radar-target-generation-and-detection](https://github.com/davidsosa/radar-target-generation-and-detection) 
    - User Defined Range and Velocity / Radar Specifications - Frequency, Max Range, Range Resolution, Max Velocity
    - FMCW Waveform Generation
    - Signal generation and Moving Target simulation
    - Range Measurement - Range Doppler Map Generation, CA-CFAR detector (1D, sliding window method)
  - [ShadowingEffect](https://github.com/AmmarMohanna/ShadowingEffect) 
    - A CNN Based Algorithm for Shadowing Effect Removal for Target Detection Using FMCW radar. 
    - 基本應該沒什麼用，他沒說他的資料怎麼生的，但也是存成.jpg圖檔取處理，未來可以參考他怎麼讀資料的。
    - 是用`tensorflow.keras`實作，很像`PyTorch`的寫法，但沒說dependency，看來真的是純參考XD
- 在 github 搜尋 "[mmwave](https://github.com/topics/mmwave)" 沒什麼收穫，搜尋  "[sar](https://github.com/topics/sar)" 感覺sar發展的比fmcw還要多
1. Y. -C. Lin, M. -X. Gu, C. -H. Lin and T. -S. Lee, "[Deep-Learning Based Decentralized Frame-to-Frame Trajectory Prediction Over Binary Range-Angle Maps for Automotive Radars](https://ieeexplore.ieee.org/document/9437958)," in *IEEE Transactions on Vehicular Technology*, vol. 70, no. 7, pp. 6385-6398, July 2021.
   - 資料類型: RDA maps, ERA maps, Binary RA maps
   - 相關方法: ResNet, ST-LSTM, ConvLSTM, JPDA + EKF
2. M. Sahal, Z. A. Said, R. Y. Putra, R. E. Abdul Kadir and A. A. Firmansyah, "[Comparison of CFAR Methods on Multiple Targets in Sea Clutter Using SPX-Radar-Simulator](https://ieeexplore.ieee.org/abstract/document/9163697)," *2020 International Seminar on Intelligent Technology and Its Applications (ISITIA)*, 2020, pp. 260-265
   - 另一個版本的各類CFAR detector介紹
   - 有比較詳細介紹OS-CFAR
   - 資料集: SPX-Radar-Simulator


### **Radar Perception**
- 雷達感知筆記 [awesome-radar-perception](https://github.com/ZHOUYI1023/awesome-radar-perception)
  - Zhou, Yi, et al. "[Towards Deep Radar Perception for Autonomous Driving: Datasets, Methods, and Challenges](https://www.mdpi.com/1424-8220/22/11/4208)." *Sensors* 22.11 (2022): 4208.
- Radar Simulation Toolbox
  - RadarSimPy
    - [radarsimpy](https://github.com/rookiepeng/radarsimpy)
    - [documentation](https://rookiepeng.github.io/radarsimpy/)
  - Open-Source Millimeter-Wave Radar Simulation Framework
    - C. Schöffmann, B. Ubezio, C. Böhm, S. Mühlbacher-Karrer and H. Zangl, "[Virtual Radar: Real-Time Millimeter-Wave Radar Sensor Simulation for Perception-Driven Robotics](https://ieeexplore.ieee.org/document/9387149)," in *IEEE Robotics and Automation Letters*, vol. 6, no. 3, pp. 4704-4711, July 2021.
    - github repo [virtualradar](https://github.com/chstetco/virtualradar) 


### **Pre-CFAR Data** 
<!-- 不知道 [Pre-CFAR](https://blog.csdn.net/qq_38890412/article/details/121128764) 是什麼意思 -->
  - **Range Azimuth Map, RA map**
    - K. Patel, K. Rambach, T. Visentin, D. Rusev, M. Pfeiffer and B. Yang, "[Deep Learning-based Object Classification on Automotive Radar Spectra](https://ieeexplore.ieee.org/abstract/document/8835775)," *2019 IEEE Radar Conference (RadarConf)*, 2019, pp. 1-6
    - Y. Xiao, L. Daniel and M. Gashinova, "[Image Segmentation and Region Classification in Automotive High-Resolution Radar Imagery](https://ieeexplore.ieee.org/abstract/document/9288850)," in *IEEE Sensors Journal*, vol. 21, no. 5, pp. 6698-6711, 1 March1, 2021
    - Kim, Woosuk, et al. "[YOLO-based simultaneous target detection and classification in automotive FMCW radar systems](https://www.mdpi.com/1424-8220/20/10/2897)" *Sensors* 20.10 (2020): 2897.
    - Sheeny, Marcel, Andrew Wallace, and Sen Wang. "[300 GHz radar object recognition based on deep neural networks and transfer learning](https://ietresearch.onlinelibrary.wiley.com/doi/pdf/10.1049/iet-rsn.2019.0601)" *IET Radar, Sonar & Navigation* 14.10 (2020): 1483-1493.
    - Dong, Xu, et al. "[Probabilistic oriented object detection in automotive radar](https://openaccess.thecvf.com/content_CVPRW_2020/papers/w6/Dong_Probabilistic_Oriented_Object_Detection_in_Automotive_Radar_CVPRW_2020_paper.pdf)" Proceedings of the *IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops*. 2020.
    - X. Gao, S. Roy, G. Xing and S. Jin, "[Perception Through 2D-MIMO FMCW Automotive Radar Under Adverse Weather](https://ieeexplore.ieee.org/document/9551127)," *2021 IEEE International Conference on Autonomous Systems (ICAS)*, 2021, pp. 1-5
    - Y. -C. Lin, M. -X. Gu, C. -H. Lin and T. -S. Lee, "[Deep-Learning Based Decentralized Frame-to-Frame Trajectory Prediction Over Binary Range-Angle Maps for Automotive Radars](https://ieeexplore.ieee.org/document/9437958)," in *IEEE Transactions on Vehicular Technology*, vol. 70, no. 7, pp. 6385-6398, July 2021
  - **Range Doppler Map, RD map**
    - R. Pérez, F. Schubert, R. Rasshofer and E. Biebl, "[Single-Frame Vulnerable Road Users Classification with a 77 GHz FMCW Radar Sensor and a Convolutional Neural Network](https://ieeexplore.ieee.org/abstract/document/8448126)," *2018 19th International Radar Symposium (IRS)*, 2018, pp. 1-10
    - S. Kim, S. Lee, S. Doo and B. Shim, "[Moving Target Classification in Automotive Radar Systems Using Convolutional Recurrent Neural Networks](https://ieeexplore.ieee.org/abstract/document/8553185)," *2018 26th European Signal Processing Conference (EUSIPCO)*, 2018, pp. 1482-1486
    - L. Wang, J. Tang and Q. Liao, "[A Study on Radar Target Detection Based on Deep Neural Networks](https://ieeexplore.ieee.org/abstract/document/8629967)," in *IEEE Sensors Letters*, vol. 3, no. 3, pp. 1-4, March 2019
    - G. Zhang, H. Li and F. Wenger, "[Object Detection and 3d Estimation Via an FMCW Radar Using a Fully Convolutional Network](https://ieeexplore.ieee.org/abstract/document/9054511)," *ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2020, pp. 4487-4491
    - W. Jia, Y. Cao, S. Zhang and W. -Q. Wang, "[Detecting High-Speed Maneuvering Targets by Exploiting Range-Doppler Relationship for LFM Radar](https://ieeexplore.ieee.org/abstract/document/9347707)," in *IEEE Transactions on Vehicular Technology*, vol. 70, no. 3, pp. 2209-2218, March 2021
  - **Radar Object Detection, ROD**
    - Jun Yu, Xinlong Hao, Xinjian Gao, Qiang Sun, Yuyu Liu, Peng Chang, Zhong Zhang, Fang Gao, and Feng Shuang. 2021. [Radar Object Detection Using Data Merging, Enhancement and Fusion](https://doi.org/10.1145/3460426.3463653). *In Proceedings of the 2021 International Conference on Multimedia Retrieval (ICMR '21)*. Association for Computing Machinery, New York, NY, USA, 566–572. 
    - Pengliang Sun, Xuetong Niu, Pengfei Sun, and Kele Xu. 2021. [Squeeze-and-Excitation network-Based Radar Object Detection With Weighted Location Fusion](https://doi.org/10.1145/3460426.3463654). *In Proceedings of the 2021 International Conference on Multimedia Retrieval (ICMR '21)*. Association for Computing Machinery, New York, NY, USA, 545–552. 
    - Zangwei Zheng, Xiangyu Yue, Kurt Keutzer, and Alberto Sangiovanni Vincentelli. 2021. [Scene-aware Learning Network for Radar Object Detection](https://doi.org/10.1145/3460426.3463655). *In Proceedings of the 2021 International Conference on Multimedia Retrieval (ICMR '21)*. Association for Computing Machinery, New York, NY, USA, 573–579. 
    - Bo Ju, Wei Yang, Jinrang Jia, Xiaoqing Ye, Qu Chen, Xiao Tan, Hao Sun, Yifeng Shi, and Errui Ding. 2021. [DANet: Dimension Apart Network for Radar Object Detection](https://doi.org/10.1145/3460426.3463656). *In Proceedings of the 2021 International Conference on Multimedia Retrieval (ICMR '21)*. Association for Computing Machinery, New York, NY, USA, 533–539. 
    - Chih-Chung Hsu, Chieh Lee, Lin Chen, Min-Kai Hung, Yu-Lun Lin, and Xian-Yu Wang. 2021. [Efficient-ROD: Efficient Radar Object Detection based on Densely Connected Residual Network](https://doi.org/10.1145/3460426.3463657). *In Proceedings of the 2021 International Conference on Multimedia Retrieval (ICMR '21)*. Association for Computing Machinery, New York, NY, USA, 526–532. 
    - Yizhou Wang, Jenq-Neng Hwang, Gaoang Wang, Hui Liu, Kwang-Ju Kim, Hung-Min Hsu, Jiarui Cai, Haotian Zhang, Zhongyu Jiang, and Renshu Gu. 2021. [ROD2021 Challenge: A Summary for Radar Object Detection Challenge for Autonomous Driving Applications](https://doi.org/10.1145/3460426.3463658). *In Proceedings of the 2021 International Conference on Multimedia Retrieval (ICMR '21)*. Association for Computing Machinery, New York, NY, USA, 553–559. 
  - **Range Azimuth Doppler, RAD map**
    - X. Gao, G. Xing, S. Roy and H. Liu, "[Experiments with mmWave Automotive Radar Test-bed](https://ieeexplore.ieee.org/abstract/document/9048939)," *2019 53rd Asilomar Conference on Signals, Systems, and Computers*, 2019, pp. 1-6.
    - Major, Bence, et al. "[Vehicle detection with automotive radar using deep learning on range-azimuth-doppler tensors](https://openaccess.thecvf.com/content_ICCVW_2019/papers/CVRSUAD/Major_Vehicle_Detection_With_Automotive_Radar_Using_Deep_Learning_on_Range-Azimuth-Doppler_ICCVW_2019_paper.pdf)." *Proceedings of the IEEE/CVF International Conference on Computer Vision Workshops*. 2019.
    - A. Palffy, J. Dong, J. F. P. Kooij and D. M. Gavrila, "[CNN Based Road User Detection Using the 3D Radar Cube](https://ieeexplore.ieee.org/abstract/document/8962258)," in *IEEE Robotics and Automation Letters*, vol. 5, no. 2, pp. 1263-1270, April 2020.
    - X. Gao, G. Xing, S. Roy and H. Liu, "[RAMP-CNN: A Novel Neural Network for Enhanced Automotive Radar Object Recognition](https://ieeexplore.ieee.org/abstract/document/9249018)," in *IEEE Sensors Journal*, vol. 21, no. 4, pp. 5119-5132, 15 Feb.15, 2021.
    - Ouaknine, Arthur, et al. "[Multi-view radar semantic segmentation](https://openaccess.thecvf.com/content/ICCV2021/papers/Ouaknine_Multi-View_Radar_Semantic_Segmentation_ICCV_2021_paper.pdf)." *Proceedings of the IEEE/CVF International Conference on Computer Vision*. 2021.
    - Meyer, Michael, Georg Kuschk, and Sven Tomforde. "[Graph convolutional networks for 3d object detection on radar data](https://openaccess.thecvf.com/content/ICCV2021W/AVVision/papers/Meyer_Graph_Convolutional_Networks_for_3D_Object_Detection_on_Radar_Data_ICCVW_2021_paper.pdf)." *Proceedings of the IEEE/CVF International Conference on Computer Vision*. 2021.
  - **Raw Signal**
    - F. C. Akyon, Y. K. Alp, G. Gok and O. Arikan, "[Classification of Intra-Pulse Modulation of Radar Signals by Feature Fusion Based Convolutional Neural Networks](https://ieeexplore.ieee.org/abstract/document/8553176)," *2018 26th European Signal Processing Conference (EUSIPCO)*, 2018, pp. 2290-2294.


### 08/24
- CRUW Dataset, Camera-Radar University of Washington Dataset
  - ROD2021 Dataset [downloads](https://www.cruwdataset.org/download) 
  - Develop kit for CRUW dataset [cruw-devkit](https://github.com/yizhou-wang/cruw-devkit)
  - Baseline method [RODNet: Radar object detection network](https://github.com/yizhou-wang/RODNet)
  - The final ranking for the ROD2021 Challenge [Challenge Results](https://www.cruwdataset.org/rod2021-results) 
  - Resources (paper, code, etc.) have not been published yet?

| Team Name | Members | Affiliations | AP (total) | AR (total) |
| --------- | -------- | ------------ | ---------- | ---------- |
| Baidu-VIS&ITD | Bo Ju*, Wei Yang*, Jinrang Jia*, Xiaoqing Ye, Qu Chen, Xiao Tan, Hao Sun, Yifeng Shi, Errui Ding |     Baidu Inc.  | 82.2 | 90.1 |
| USTC-NELSLIP | Jun Yu, Xinlong Hao, Xinjian Gao, Qiang Sun, Yuyu Liu, Peng Chang, Zhong Zhang, Fang Gao, Feng Shuang | University of Science and Technology of China; Ping An Technology Co., Ltd.; PAII labs, Palo Alto, California; Hefei ZhanDa Intelligence Technology Co., Ltd.; Guangxi University | 79.7 | 88.9 |
| No_Bug | Pengliang Sun, Xuetong Niu, Pengfei Sun, Kele Xu | The Chinese University of Hong Kong; King’s College London; University of Zurich and ETH Zurich; National Key Laboratory of Parallel and Distributed Processing | 76.1 | 83.9 |
| DD_Vision | Wanxin Tian, Zehui Yu, Aocheng Li, Xiubao Zhang, Haifeng Shen | Beijing University of Posts and Telecommunications; Didi Chuxing | 75.1 | 84.9 |
| Cal-NJU_Radar | Zangwei Zheng, Xiangyu Yue, Kurt Keutzer, Alberto Sangiovanni Vincentelli | Nanjing University; UC Berkeley | 75.0 | 81.0 |
| [ACVLab](https://sites.google.com/view/acvlab) | Chih-Chung Hsu, Chieh Lee, Lin Chen, Min-Kai Hung, Yu-Lun Chen | National Cheng Kung University; National Pingtung University of Science and Technology | 69.3 | 77.3 |


### 08/25
- 開始讀 Zhou, Yi, et al. "[Towards Deep Radar Perception for Autonomous Driving: Datasets, Methods, and Challenges](https://www.mdpi.com/1424-8220/22/11/4208)." *Sensors* 22.11 (2022): 4208. 總共有45頁



### 值得關注的作者
偶爾看一下他們有沒有出什麼新東西可以跟XD
- PhD students
  - [Chia-Hung Lin](https://ieeexplore.ieee.org/author/37087085396)
  - [Yu-Chein Lin](https://ieeexplore.ieee.org/author/37086483408)
  - [Hsin-Yuan Chang](https://ieeexplore.ieee.org/author/37087022655)
  - [Jiawei Shao](https://ieeexplore.ieee.org/author/37088447290)

- Professors
  - [Wei-Ho Chung](https://ieeexplore.ieee.org/author/37538749800)
  - [Chih-Yu Wang](https://ieeexplore.ieee.org/author/37085674145)
  - [Yuyi Mao](https://ieeexplore.ieee.org/author/37085508893)
  - [Jun Zhang](https://ieeexplore.ieee.org/author/37407590900)


