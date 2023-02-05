# Lab notes
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
  - Auto-Split 已經部屬在華為雲 [Auto-Split: Edge Cloud Collaboration](https://developer.huaweicloud.com/develop/aigallery/notebook/detail?id=5fad1eb4-50b2-4ac9-bcb0-a1f744cf85c7) 雲端服務
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
  - 依據 AWR1843 雷達規格，去模擬生成 Range-Azimuth Doppler, RAD 資料的 [github](https://github.com/ZhangAoCanada/FMCW_Radar_slam)，但還不確定能不能用。 
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
  - **Range Azimuth Doppler, RAD tensor**
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
  - 進度: 19 / 45


### 08/26
- 繼續讀 Zhou, Yi, et al. "[Towards Deep Radar Perception for Autonomous Driving: Datasets, Methods, and Challenges](https://www.mdpi.com/1424-8220/22/11/4208)." *Sensors* 22.11 (2022): 4208.
  - 進度: 21 / 45
- 了解一下 *Sensors* 這個 MDPI 底下的 open access 期刊
  - MDPI 出版社底下的期刊列表 [Journal List](https://www.mdpi.com/journal/sensors/announcements/2041)。從 Updated Impact Factors 可以找到 *Sensors*，然後底下又有3個類別，分別是 "Chemistry, Analytical", "Engineering, Electrical & Electronic", 和 "Instruments & Instrumentation"，但好像是混在一起都發在同一個期刊上，可能再透過不同 Issue 分開。
  - 之前大學做專題的時候也讀過幾篇老師指派的 *Sensors* 的文章，只是不清楚他客觀上是不是一個好的期刊。
  - *Sensors* 是 2001 年創刊，Volume多少就是指第幾年出版的，Issue多少就是指哪個領域，每年的每月初會出2個Issue 所以一年共出24份刊物。
  - 舉例來說 [*Sensors* 22.11 (2022): 4208.](https://www.mdpi.com/1424-8220/22/11/4208) 就是 [*Sensors*, Volume 22, Issue 11 (June-1 2022)](https://www.mdpi.com/1424-8220/22/11) 即 2022 年出版的第 11 個 Issue 的第 4208 篇，篇數是從 Issue 1 開始算的，每個 Issue 都收 3~400 篇左右。
    | Journal | Impact Factor | Rank | Category | Details |
    | - | - | - | - | - |
    | *Sensors* | 3.275 | 77/266 (Q2) | Engineering, Electrical & Electronic | [Link](https://www.mdpi.com/journal/sensors/stats) |
    | *Sensors* | 3.275 | 22/86 (Q2) | Chemistry, Analytical | [Link](https://www.mdpi.com/journal/sensors/stats) |
    | *Sensors* | 3.275 | 15/64 (Q1) | Instruments & Instrumentation | [Link](https://www.mdpi.com/journal/sensors/stats) |



### **Radar Signal Processing**
- Zhou, Yi, et al. "[Towards Deep Radar Perception for Autonomous Driving: Datasets, Methods, and Challenges](https://www.mdpi.com/1424-8220/22/11/4208)." *Sensors* 22.11 (2022): 4208.
####  **Radar Signal ProcessingFundamentals**
- Different radar devices vary in their sensing capabilities
- It is important to leverage radar domain knowledge 
  - to understand the **performance boundary** 
  - to find **key scenarios** 
  - to solve **critical problems** 
- classical signal processing pipeline for automotive radar applications


#### **FMCW Radar Signal Processing**
- Off-the-shelf automotive radars operate with a sequence of **linear FMCW signals** (Frequency-Modulated Continuous-Wave, FMCW) to simultaneously measure **range**, **angle**, and **velocity**
- automotive radar is allowed to use **2** frequency bands in mmwaves 
  - 24 GHz (24~24.25 GHz)
  - 77 GHz (77~79 GHz)
- There is a trend towards **77 GHz** for several reasons
  - **larger bandwidth**
    - 76–77 GHz for long-range
    - 77–81 GHz for short-range
  - **higher Doppler resolution**
  - **smaller antennas**, with sub-wavelength sized?
  - R. Ravindran, M. J. Santora and M. M. Jamali, "[Multi-Object Detection and Tracking, Based on DNN, for Autonomous Vehicles: A Review](https://ieeexplore.ieee.org/document/9274366)," in *IEEE Sensors Journal*, vol. 21, no. 5, pp. 5668-5677, 1 March1, 2021.
- FMCW signal is characterised by the following parameters
  - the **carrier frequency** $f_c$ (aka the start frequency)
  - the **sweep bandwidth** $B$
  - the **chirp duration** $T_c$
  - the **slope** $S = B \: / \: T_c$
- During **one chirp** duration, frequency increases linearly from **$f_c$** to $f_c + B$ with a slope of $S$
<img src="https://i.imgur.com/qeRFML2.png"  width=100% height=100%>
- **One** FMCW **waveform** is referred to as **a chirp**
- **One** radar **transmission** is **a frame of** $N_c$ **chirps** equally spaced by chirp cycle time $T_c$
- The total time $T_f = N_c \: \cdot \: T_c$ is called the **frame time** (aka the time on target, TOT)
- In order to **avoid** the need for **high-speed sampling**, a frequency **mixer** combines the received signal with the transmitted signal to produce two signals
  - sum frequency $f_T(t) + f_R(t)$ 
  - difference frequency $f_T(t) - f_R(t)$
- Then, a low-pass filter is used to filter out the sum frequency component and obtain the **IF signal** (Intermediate Frequency, IF)
- In this way, FMCW radar can achieve GHz performance with only MHz sampling
- In practice, a **quadrature mixer** is used to improve the **noise figure**
  - Ramasubramanian, Karthik, and T. Instruments. "[Using a complex-baseband architecture in FMCW radar systems](https://www.ti.com/lit/wp/spyy007/spyy007.pdf)." *Texas Instruments 19* (2017).
- Resulting complex exponential IF signal $x_{IF}(t) = Ae^{j(2 \pi f_{IF} t \; + \; \phi_{IF})}$
  - $A$ is the **amplitude**
  - $f_{IF} = f_T(t) - f_R(t)$ is referred to as the **beat frequency**
  - $\phi_{IF}$ is the **phase** of the IF signal
- Next, the IF signal is sampled $N_s$ times by an ADC converter, resulting in a discrete-time complex signal
- Multiple frames of chirp signals are assembled into a two-dimensional matrix
  - the dimension of the **sampling points within a chirp** is referred to as **fast time**
  - the dimension of the **chirp index within one frame** is referred to as **slow time**
   <img src="https://i.imgur.com/PZKVyn7.png"  width=55% height=55%>
- Assume **one object** moving with **speed** $v$ at **distance** $r$, we have 
  - the **frequency** $\; f_{IF} = \frac{\; 2S(r \; + \; v \; \cdot \; T_c) \; }{c} \;$ of the IF signal
  - the **phase** $\; \phi_{IF} = \frac{\; 4 \pi (r \; + \; v \; \cdot \; T_c) \; }{\lambda} \;$ of the IF signal
  - where $\lambda = c \; / \; f_c$ is the wavelength of the chirp signal
  - we can find that from the above expressions the range and Doppler velocity are coupled
- Under the following **2 assumptions**, the range and Doppler can be **decoupled**
  - the range variations in slow time caused by target motion can be neglected due to the short frame time 
  - the Doppler frequency in fast time can be neglected compared to the beat frequency by utilising a wideband waveform
  - the range can be estimated from the beat frequency as $r = c \; \cdot \; f_{IF} \; / \; 2S$
  - the Doppler velocity can be estimated from the phase shift between two chirps as $v = \Delta \phi \lambda  \; / \; 4 \pi \: T_c$
- Next, a **range FFT** is applied in the fast-time dimension to resolve the frequency change, followed by a **Doppler FFT** in the slow-time dimension to resolve the phase change. In practice, a window function is applied before FFT to reduce sidelobes
- As a result, we obtain a **2D complex-valued data matrix** called the Range–Doppler map, **RD map**
  - the **range** of a cell in the RD map is $\; r_k = k \: \frac{c}{ \; 2 \; \cdot \; B_{IF} \; }$
  - the **Doppler velocity** of a cell in the RD map is $\; v_l = l \: \frac{\lambda}{ \; 2 \; \cdot \; T_{f} \; }$
  - $k$ and $l$ denote the indexes of FFT
  - $B_{IF}$ is the IF bandwidth
  - $T_{f}$ is the frame time
  - In practice, FFT is applied due to its computational efficiency compared to DFT
  - Therefore, the sequence will be zero-padded to the nearest power of 2 if necessary
- Radar Tx / Rx signals and the resulting **RD map**
![](https://i.imgur.com/OxFxPCt.png)
- **Angle** information can be obtained using more than one receive or transmit channel 
  - e.g. SIMO radars utilize a single Tx and multiple Rx antennas for angle estimation, MISO radars utilize multiple Tx and single Rx antenna for angle estimation
- Suppose **one object** is located in direction $\theta$
  - similar to Doppler processing, the induced frequency change between two adjacent receive (or transmit) antennas can be neglected
  - while the induced phase change can be used for calculating the Direction Of the Angle (**DOA**)
  - this **phase change** is $\Delta \phi = 2 \pi d \; sin \theta \: / \: \lambda$
  - where $d$ is the inter-antenna **spacing**
- Then, a third FFT can be applied to the receive antenna dimension
  - BTW for conventional radar with a small number of Rx antennas, the sequence is often padded with $N_{FFT} - N_{Rx}$ zeros to achieve a smooth display of the spectrum
- The **angle** at index $\eta$ is $\; \theta_{\eta} = arcsin(\frac{\eta \lambda}{\; N_{FFT} \;\; })$ 
  - The **angular resolution** of a SIMO of MISO radar depends on the number of Rx or Tx antennas
  - The maximum number of Rx antennas is limited by the additional cost of signal processing chains on the device
- **MIMO radar** operates with multiple channels in both Tx and Rx
  - e.g. a MIMO radar with $N_{Tx}$ Tx antennas and $N_{Rx}$ Rx antennas can synthesise a virtual array with $N_{Tx} \cdot N_{Rx}$ channels
  ![](https://i.imgur.com/kXj6oOo.png)
  - Signals from different Tx antennas should be orthogonal and there are multiple ways to realise waveform orthogonality
  - such as TDM, FDM, and DDM
- **TDM**, Time-Division Multiplexing
  - different Tx antennas transmit chirp signals in turns
  <img src="https://i.imgur.com/gViDgFS.png"  width=80% height=80%>
<!--   ![](https://i.imgur.com/gViDgFS.png) -->
  - Pros. 
    - widely used for its **simplicity**, which possibly means that it is supported by many radar devices
  - Cons. 
    - **additional phase shift compensation** is required to compensate for the motion of detections during the Tx switching time
    - **reduced detection range** due to the loss of transmitting power
  - J. Bechter, F. Roos and C. Waldschmidt, "[Compensation of Motion-Induced Phase Errors in TDM MIMO Radars](https://ieeexplore.ieee.org/document/8052088)," in *IEEE Microwave and Wireless Components Letters*, vol. 27, no. 12, pp. 1164-1166, Dec. 2017.
- FDM, Frequency-Ddivision Multiplexing
- **DDM**, Doppler-Division Multiplexing
  - H. Sun, F. Brigui and M. Lesturgie, "[Analysis and comparison of MIMO radar waveforms](https://ieeexplore.ieee.org/abstract/document/7060251)," *2014 International Radar Conference*, 2014, pp. 1-6.
  - S. Sun, A. P. Petropulu and H. V. Poor, "[MIMO Radar for Advanced Driver-Assistance Systems and Autonomous Driving: Advantages and Challenges](https://ieeexplore.ieee.org/document/9127853)," in *IEEE Signal Processing Magazine*, vol. 37, no. 4, pp. 98-117, July 2020.
- DDM transmits all Tx waveforms simultaneously and separates them in the Doppler domain
  - A **Doppler shift** is added to adjacent chirps to realize waveform orthogonality
  - the Doppler shift for the $k^{\:th\:}$ transmitter is $\: \omega_{k} = \frac{\; 2 \pi \ (k \: - \: 1) \;\;}{N}$
  - where $N$ is usually selected as the number of Tx antennas $N_{Tx}$
  <img src="https://i.imgur.com/2uxW05j.png"  width=90% height=90%>
<!--   ![](https://i.imgur.com/2uxW05j.png) -->
  - Pros.
    - supported by many radar devices (like TDM?)
  - Cons.
    - more ambiguous, its unambiguous Doppler velocity is reduced to $\frac{\; 1 \;}{N}$ of the original one
- **Emptyband DDM** can achieve more robust velocity disambiguation by introducing several empty Doppler sub-bands
  - Gupta, J. [High-End Corner Radar Reference Design](https://www.ti.com/lit/ug/tiduf01/tiduf01.pdf?ts=1661823130303&ref_url=https%253A%252F%252Fwww.ti.com%252Fsitesearch%252Fen-us%252Fdocs%252Funiversalsearch.tsp%253FlangPref%253Den-US%2526searchTerm%253Dmimo%2526nr%253D2). *In Design Guide TIDEP-01027*; Texas Instruments: Dallas, TX, USA, 2022.
  - Rebut, J.; Ouaknine, A.; Malik, W.; Pérez, P. RADIal Dataset. 2022. (accessed on 30 Aug 2022)
    - [RADIal](https://github.com/valeoai/RADIal) 有提供 sample code 可以參考
- After decoupling the received signals, we can obtain a 3D tensor by stacking RD maps with respect to Tx–Rx pairs
- Then, the DOA can be estimated through the angle FFT along the virtual receiver dimension
  - Some super-resolution methods can be applied to improve angular resolution
  - such as Capon, MUSIC, and ESPRIT
- The resulting 3D tensor is referred to as the Range–Azimuth–Doppler tensor, **RAD tensor** or radar tensor
- The **Radar Detection Pipeline**
  - First, RD maps are integrated coherently along the virtual receiver dimension to increase the SNR
  - Then, a CFAR detector is applied to detect peaks or estimate the noise level in the RD map
  - Finally, the DOA estimation method is applied for angle estimation
    - for conventional radars, only azimuth angle is resolved
    - for next-generation radars, both azimuth and elevation angles can be resolved
  - The output (of the radar) is a point cloud with measurements of range, Doppler, and angle




#### **Datasets, Labelling, and Augmentation**
- Data play a key role in the learning-based approaches
- Radar Datasets w.r.t their **data representations**, **tasks**, scenarios, and **annotation types** are summarised below
- Also introduce **extrinsic calibration** and **cross-modality labelling** techniques
- And further investigate **data augmentation methods** and the potential use of **synthetic radar data** to improve data **diversity**


#### **Radar Datasets**
- Radar classification w.r.t their **resolution**
  - LR, Low Resolution
    - FMCW Radar?
  - HR, High Resolution 
    - Polarimetric Radar
    - Cooperative Radars
    - Multi-chip Cascaded MIMO Radar
    - Synthetic Aperture Radar (SAR)
    - Spinning Radar
  - most off-the-shelf radars will output a point cloud with range, azimuth angle, Doppler velocity, and RCS
    - next-generation 4D radar can also measure elevation angle
- Radar classification w.r.t the **output** data type
  - **ADC** data
  - **RA / RD maps**
  - **RAD tensors**
  - some radar prototypes can be configured to output these radar raw data
- Radar classification w.r.t. the **task** (the role) in autonomous driving
  - **localization** 
  - **detection**
- types of annotations
  - **2D bounding boxes**
    - labelled in Bird’s Eye View (**BEV**) and with **orientation** information
    - sometimes referred to as pseudo-3D boxes
  - **3D bounding boxes** 
    - 2D bboxes plus **height** information and **pitch angle**
    - **NOTE**. radar detections within the bounding box could be ghost detection or clutter
  - **Pointwise** annotations 
    - can provide semantic information at a finer granularity than bounding boxes
    - is a better way to capture the noisy nature of the radar point cloud
    - **NOTE**. the annotated points do not necessarily reflect the shape information




#### **Synthetic Data**
- Synthetic datasets are widely used in Computer Vision and LiDAR perception 
- Networks trained with synthetic data can actually generalize well in the real-world
  - Johnson-Roberson, Matthew, et al. "[Driving in the matrix: Can virtual worlds replace human-generated annotations for real world tasks?](https://arxiv.org/pdf/1610.01983.pdf)." *arXiv preprint arXiv:1610.01983* (2016).
- The labelling cost can be completely avoided
- **Physics-based** simulation methods
  - e.g. ray tracing
    - C. Schüßler, M. Hoffmann, J. Bräunig, I. Ullmann, R. Ebelt and M. Vossiek, "[A Realistic Radar Ray Tracing Simulator for Large MIMO-Arrays in Automotive Environments](https://ieeexplore.ieee.org/document/9533181)," in *IEEE Journal of Microwaves*, vol. 1, no. 4, pp. 962-974, Oct. 2021.
    - M. Holder et al., "[Measurements revealing Challenges in Radar Sensor Modeling for Virtual Validation of Autonomous Driving](https://ieeexplore.ieee.org/document/8569423)," *2018 21st International Conference on Intelligent Transportation Systems (ITSC)*, 2018, pp. 2616-2622.
  - Pros. 
    - can model multi-path propagation 
    - can also model separability issue of close objects
  - Cons. 
    - difficult to capture the RCS variation in azimuth with current methods
- **Model-based** augmentation 
  - the spatial distribution of radar detections over the vehicle can be approximated by 2 kinds of model
    - surface–volume model
    - volcanormal measurement model
- There are some seminal works utilizing learning-based generative models for radar simulation
- **Deep stochastic radar model**
  - T. A. Wheeler, M. Holder, H. Winner and M. J. Kochenderfer, "[Deep stochastic radar models](https://ieeexplore.ieee.org/document/7995697)," *2017 IEEE Intelligent Vehicles Symposium (IV)*, 2017, pp. 47-53.
- Generative models
  - GAN-based LiDAR-to-radar generation
    - Wang, Leichen, Bastian Goldluecke, and Carsten Anklam. "[L2R GAN: LiDAR-to-radar translation](https://openaccess.thecvf.com/content/ACCV2020/papers/Wang_L2R_GAN_LiDAR-to-Radar_Translation_ACCV_2020_paper.pdf)." *Proceedings of the Asian Conference on Computer Vision (ACCV)*. 2020.
  - GAN-based radar-to-image generation
    - Lekic, Vladimir, and Zdenka Babic. "[Automotive radar and camera fusion using generative adversarial networks](https://www.sciencedirect.com/science/article/pii/S1077314219300530)." *Computer Vision and Image Understanding* 184 (2019): 1-8.
  - VAE-based radar-to-image generation
    - C. Ditzel and K. Dietmayer, "[GenRadar: Self-Supervised Probabilistic Camera Synthesis Based on Radar Frequencies](https://ieeexplore.ieee.org/document/9570339)," in *IEEE Access*, vol. 9, pp. 148994-149042, 2021.


#### **Radar Depth and Velocity Estimation**
- Radar can measure range and Doppler velocity, but both of them **cannot be directly used** for downstream tasks
- The range measurements are sparse and therefore difficult to associate with their visual correspondences
- The Doppler velocity is measured in the radial axis, therefore, cannot be directly used for tracking
- The depth completion and velocity estimation methods for radar point clouds are summarised below
- **To be continued...**



#### **Radar Object Detection**
- Due to low resolution, classical radar detection algorithm has limited classification capability
- At hardware level, next-generation imaging radars can output high-resolution point clouds
- At algorithm level, NN show their potentials to learn better features from the dataset
- There is a broader definition of **radar detection**, like
  - **pointwise** detection
  - **2D/3D bounding box** detection
  - **instance segmentation**
- According to the input data structure, we classify the **deep radar detection** into 2 classes
  - **point-cloud-based**, similar to LiDAR point cloud
  - **pre-CFAR-based**, similar to visual image
- Focus on how the **radar domain knowledge** can be incorporated into these networks to address the **low SNR problem**
  - applied on networks design?
  - explainations on why they works?
  - how low the SNR is low?
- Overview of radar detection frameworks
![](https://i.imgur.com/O7Nlu0Y.png)


#### **Classical Detection Pipeline**
- the conventional **radar detection pipeline** consists of **4** steps:
- **CFAR detection** 
  - a CFAR detector is applied to detect peaks in the RD heat map as a list of targets
- **Clustering**
  - the moving targets are first projected to Cartesian coordinates 
  - then clustered by DBSCAN
  - static targets are usually filtered out before clustering because they are indistinguishable from environmental clutter
- **Feature extraction**
  - within each cluster, hand-crafted features, such as the statistics of measurements and shape descriptors, are extracted
- **Classification**
  - then sent to a ML classifier
- Improvements can be made upon each of these **4** steps


#### **CFAR**
- CFAR is usually executed in an on-chip DSP, so the choice of method is restricted by hardware support
- A **threshold** is set to achieve a constant false alarm rate for **Rayleigh-distributed noise**
- The next-generation high resolution radar chips support OS-CFAR
  - **OS-CFAR** sorts the neighbouring cells around the CUT according to the received power and selects the k-th cell to represent the noise value, often set **k = 3N/4** in practice
  - Pros: 
    - efficient and straightforward
    - can distinguish close targets, effective in multi-target scenario
  - Cons:
    - slightly increased false alarm rate
    - require additional computational costs
- CFAR detection algorithm should be able to fit in a SoC, especially in automotive applications
- More sophisticated CFAR variants are summarised in [128](https://ieeexplore.ieee.org/abstract/document/9547416), but are rarely used in automotive applications
    - DL-based peak classification
      - Z. Cao, W. Fang, Y. Song, L. He, C. Song and Z. Xu, "[DNN-Based Peak Sequence Classification CFAR Detection Algorithm for High-Resolution FMCW Radar](https://ieeexplore.ieee.org/abstract/document/9547416)," in *IEEE Transactions on Geoscience and Remote Sensing*, vol. 60, pp. 1-15.
    - DL-based noise level estimation
      - C. -H. Lin, Y. -C. Lin, Y. Bai, W. -H. Chung, T. -S. Lee and H. Huttunen, "[DL-CFAR: A Novel CFAR Target Detection Method Based on Deep Learning](https://ieeexplore.ieee.org/document/8891420)," *2019 IEEE 90th Vehicular Technology Conference (VTC2019-Fall)*, 2019, pp. 1-6.


#### **Clustering**
- Clustering is the most important stage in the radar detection pipeline, especially for the next-generation high-resolution radar
  - most important? what change?
- **DBSCAN** is favoured for several reasons
  - it does not require a pre-specified number of clusters, **arbitrary clusters**
  - it fits **arbitrary shapes**
  - it runs **fast**
  - Pedregosa, F.; Varoquaux, G.; Gramfort, A.; Michel, V.; Thirion, B.; Grisel, O.; Blondel, M.; Prettenhofer, P.; Weiss, R.; Dubourg, V.; et al. [Comparing Different Clustering Algorithms on Toy Datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html). (accessed on 26 Aug, 2022).
    ```python
    import numpy as np
    from sklearn.metrics.pairwise import cosine_similarity
    from sklearn.cluster import DBSCAN

    total_samples = 1000
    dimensionality = 3
    points = np.random.rand(total_samples, dimensionality)

    cosine_distance = cosine_similarity(points)

    # option 1) vectors are close to each other if they are parallel
    bespoke_distance = np.abs(np.abs(cosine_distance) -1)

    # option 2) vectors are close to each other if they point in the same direction
    bespoke_distance = np.abs(cosine_distance - 1)

    results = DBSCAN(metric='precomputed', eps=0.25).fit(bespoke_distance)
    ```
- Some improved DBSCAN that explicitly considering the characteristics of radar point clouds
  - Grid-based DBSCAN
    - D. Kellner, J. Klappstein and K. Dietmayer, "[Grid-based DBSCAN for clustering extended objects in radar data](https://ieeexplore.ieee.org/document/6232167)," *2012 IEEE Intelligent Vehicles Symposium*, 2012, pp. 365-370.
  - Multi-stage clustering
    - N. Scheiner, N. Appenrodt, J. Dickmann and B. Sick, "[A Multi-Stage Clustering Framework for Automotive Radar Data](https://ieeexplore.ieee.org/abstract/document/8916873)," *2019 IEEE Intelligent Transportation Systems Conference (ITSC)*, 2019, pp. 2060-2067.


#### **Classification**
- Radar target classification
- For moving objects
  - **micro-Doppler velocity** of moving components are useful features for classification
- For micro-motions
  - short-time Fourier transform (**STFT**) is applied to extract **Doppler spectrograms** as useful features
  - Different types of VRUs can be classified according to their micro-Doppler signatures, **VRU** stands for **Vulnerable Road User** 
    - Angelov, Aleksandar, et al. "[Practical classification of different moving targets using automotive radar and deep neural networks](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/iet-rsn.2018.0103)." *IET Radar, Sonar & Navigation* 12.10 (2018): 1082-1089.
    - X. Gao, G. Xing, S. Roy and H. Liu, "[Experiments with mmWave Automotive Radar Test-bed](https://ieeexplore.ieee.org/document/9048939)," *2019 53rd Asilomar Conference on Signals, Systems, and Computers*, 2019, pp. 1-6.
- For static objects
  - **statistical RCS** and **time-domain RCS** are useful features for classification of vehicles and pedestrians 
    - X. Cai, M. Giallorenzo and K. Sarabandi, "[Machine Learning-Based Target Classification for MMW Radar in Autonomous Driving](https://ieeexplore.ieee.org/document/9319548)," in *IEEE Transactions on Intelligent Vehicles*, vol. 6, no. 4, pp. 678-689, Dec. 2021. 
  -  The target RCS is a measure of the ability to reflect radar signals back to the radar receiver, **RCS** stands for **Radar Cross Section**
- "**Range** and **Doppler**" features are most important for classification, while "angle and shape" features are usually discarded, probably because of the low angular resolution? 
- e.g. some common methods for radar classification 
  - O. Schumann, C. Wöhler, M. Hahn and J. Dickmann, "[Comparison of random forest and long short-term memory network performances in classification tasks using radar](https://ieeexplore.ieee.org/document/8126350)," *2017 Sensor Data Fusion: Trends, Solutions, Applications (SDF)*, 2017, pp. 1-6.
    - 8-frame sequences input
    - **Random Forest**, slightly decreased performance
    - **LSTM**, more sensitive to the amount of training examples
- "Class imbalance problem" in radar datasets could be ease by using **classifier binarisation techniques**
  - N. Scheiner, N. Appenrodt, J. Dickmann and B. Sick, "[Radar-based Feature Design and Multiclass Classification for Road User Recognition](https://ieeexplore.ieee.org/document/8500607)," *2018 IEEE Intelligent Vehicles Symposium (IV)*, 2018, pp. 779-786.



#### **Point Cloud Dector**
- End-to-end object detectors are expected to replace the conventional pipelines based on hand-crafted features
- Most radar detection methods only apply to moving targets, since static objects are difficult to classify due to low angular resolution
- **To be continued...**



#### **Pre-CFAR Detector**
- Pre-CFAR data encode rich information of both targets and backgrounds, but this is hard to interpret by humans
  - DL-based CFAR estimation
    - Y. Cheng, J. Su, H. Chen and Y. Liu, "[A New Automotive Radar 4D Point Clouds Detector by Using Deep Learning](https://ieeexplore.ieee.org/document/9413682)," *ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2021, pp. 8398-8402.
  - DL-based DOA estimation
    - M. Gall, M. Gardill, T. Horn and J. Fuchs, "[Spectrum-based Single-Snapshot Super-Resolution Direction-of-Arrival Estimation using Deep Learning](https://ieeexplore.ieee.org/document/9080185)," *2020 German Microwave Conference (GeMiC)*, 2020, pp. 184-187.
    - J. Fuchs, M. Gardill, M. Lübke, A. Dubey and F. Lurz, "[A Machine Learning Perspective on Automotive Radar Direction of Arrival Estimation](https://ieeexplore.ieee.org/document/9674901)," in *IEEE Access*, vol. 10, pp. 6775-6797, 2022.
    - C. Grimm, T. Fei, E. Warsitz, R. Farhoud, T. Breddermann and R. Haeb-Umbach, "[Warping of Radar Data Into Camera Image for Cross-Modal Supervision in Automotive Applications](https://ieeexplore.ieee.org/abstract/document/9797876)," in *IEEE Transactions on Vehicular Technology*, 2022.
- **To be continued...**



<!-- #### **Sensor Fusion for Detection**
- Different sensors observe and represent an object with different features
- Sensor fusion can be considered as the mapping of different modalities into a common **Latent Space** where different features of the same object can be associated together
- Conventional taxonomy classify fusion architectures into 3 types, which is ambiguous
  - early fusion (input)
  - middle fusion (feature)
  - late fusion (decision)
- New taxonomy classify fusion architectures into **4** categories, according to their **fusion stage**, which is more explicit and clear
  - **Input fusion**
  - **ROI fusion**
    - Cascade fusion, which projects radar proposals to image view
    - Parallel fusion, which fuses radar ROIs and visual ROIs
  - **Feature map fusion**
  - **Decision fusion**
- Overview of radar and camera fusion frameworks
![](https://i.imgur.com/dzZt6yC.png)


#### **Input Fusion**
- Input fusion requires a lightweight preprocessing to explicitly handle radar position imprecision
- Input fusion is applied to the **radar point cloud** with **3** steps: 
  - First, **project** radar points into a pseudo-image with the range, velocity, and RCS as channels
  - Then, **concatenates** the radar pseudo-image and the visual image as a whole, similar to an RGB image
  - Finally, a visual detector can be applied to this multi-channel image for **detection**
- The **radar** and **vision** modalities are tightly **coupled**, which makes it easier for the network to learn **joint feature embeddings**
- However, an obvious disadvantage is that the architecture is **not robust to sensor failures**
- The difficulties and limitations lie in **3** aspects:
  - the radar point cloud is highly **sparse**
    - many reflections from the surface are bounced away due to specular reflections
  - the **lateral imprecision** of radar measurements
    - radar points can be out of the visual bounding box
    - e.g., imprecise extrinsic calibration, multi-path effects, and low angular resolution
  - **low-resolution** radar does not provide height information
    - may only applicable to some radar system
- Relying on the network to implicitly learn association is a **hard task**, because the network tends to simply ignore the weak modality, such as radar
- To address these difficulties, some **association techniques** are required. But compared with object detection, some of the expansion methods are **too costly for real-time processing**
  - F. Nobis, M. Geisslinger, M. Weber, J. Betz and M. Lienkamp, "[A Deep Learning-based Radar and Camera Sensor Fusion Architecture for Object Detection](https://ieeexplore.ieee.org/abstract/document/8916629)," *2019 Sensor Data Fusion: Trends, Solutions, Applications (SDF)*, 2019, pp. 1-7.
  - S. Chadwick, W. Maddern and P. Newman, "[Distant Vehicle Detection Using Radar and Vision](https://ieeexplore.ieee.org/document/8794312)," *2019 International Conference on Robotics and Automation (ICRA)*, 2019, pp. 8311-8317.
  - R. Yadav, A. Vierling and K. Berns, "[Radar + RGB Fusion For Robust Object Detection In Autonomous Vehicle](https://ieeexplore.ieee.org/abstract/document/9191046)," *2020 IEEE International Conference on Image Processing (ICIP)*, 2020, pp. 1986-1990.


#### **ROI Fusion**
- ROI fusion is adapted from the classical "Fast R-CNN" two-stage detection framework
  - Girshick, Ross. "[Fast r-cnn](https://openaccess.thecvf.com/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf)." *In Proceedings of the IEEE International Conference on Computer Vision (ICCV)*, Santiago, Chile, 7–13 December 2015; pp. 1440–1448.
- Regions Of Interest (ROIs) can be considered as a set of object candidates without category information
- The ROI fusion architecture can be further divided into cascade fusion and parallel fusion
- **Cascade fusion**
  - Cascaded ROI fusion is not robust to sensor failures
  - In the first stage
    - radar detections are directly used for region proposal
    - radar points are projected into image view as the candidate locations for anchors
    - then the ROI is determined with the help of visual semantics
  - In the second stage
    - each ROI is classified and its position is refined
  - how to improve **anchor quality**?
    - add offsets to anchors to model the positional imprecision of radar detections
    - R. Nabati and H. Qi, "[RRPN: Radar Region Proposal Network for Object Detection in Autonomous Vehicles](https://ieeexplore.ieee.org/abstract/document/8803392)," *2019 IEEE International Conference on Image Processing (ICIP)*, 2019, pp. 3093-3097.
  - how to mitigate **scale ambiguity** in the image view?
    - rescaled the anchor size according to the range measurements
    - or directly propose 3D bounding boxes and then map these boxes to the image view to avoid rescaling step
    - Nabati, Ramin, and Hairong Qi. "[Radar-camera sensor fusion for joint object detection and distance estimation in autonomous vehicles](https://arxiv.org/pdf/2009.08428.pdf)." *arXiv preprint arXiv:2009.08428* (2020).
- Cascade fusion is particularly well suited for low-resolution radars
  - where the radar point cloud has a high detection recall, but is very sparse
- Two potential problems with the cascade structure
  - the performance is limited by the completeness of the proposed ROIs in the first stage
  - the cascade structure cannot take advantage of modality redundancy
- **Parallel fusion**
  - Since cascade structure is not robust to sensor failures. It is necessary to introduce a parallel structure for improvements
  - **two-branch structure** method
    - first the radar and visual ROIs are generated independently
    - then the fusion module merges radar ROIs and visual ROIs by taking a set union
    - while the redundant ROIs are removed through NMS
    - Nabati, Ramin, and Hairong Qi. "[Radar-camera sensor fusion for joint object detection and distance estimation in autonomous vehicles](https://arxiv.org/pdf/2009.08428.pdf)." *arXiv preprint arXiv:2009.08428* (2020).
  - **Gated Region of Interest Fusion (GRIF)** method
    - utilize a gated region of interest fusion (GRIF) module to enable the adaptive fusion of modalities
    - first predicts a weight for each ROI through a convolutional sigmoid layer
    - then multiplie the ROIs from radar and vision by their corresponding weights 
    - finally elementwise add the results together 
    - Y. Kim, J. W. Choi and D. Kum, "[GRIF Net: Gated Region of Interest Fusion Network for Robust 3D Object Detection from Radar Point Cloud and Monocular Image](https://ieeexplore.ieee.org/document/9341177)," *2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*, 2020, pp. 10857-10864.


#### **Feature Map Fusion**
- Feature map fusion provides the network with greater flexibility to combine radar and visual semantics, but requires specific training techniques for effective learning
- Utilises 2 encoders to map radar and images into the same latent space with high-level semantics
- The detection frameworks are flexible
  - **One-stage methods**
    - Lim, Teck-Yian, et al. "[Radar and camera early fusion for vehicle detection in advanced driver assistance systems](https://ml4ad.github.io/files/papers/Radar%20and%20Camera%20Early%20Fusion%20for%20Vehicle%20Detection%20in%20Advanced%20Driver%20Assistance%20Systems.pdf)." *In Proceedings of Machine Learning for Autonomous Driving Workshop at the 33rd Conference on Neural Information Processing Systems (NeurIPS Workshop)*, Vancouver, BC, Canada, 8–14 December 2019; Volume 2.
    - J. Zhang, M. Zhang, Z. Fang, Y. Wang, X. Zhao and S. Pu, "[RVDet: Feature-level Fusion of Radar and Camera for Object Detection](https://ieeexplore.ieee.org/document/9564627)," *2021 IEEE International Intelligent Transportation Systems Conference (ITSC)*, 2021, pp. 2822-2828.
  - **Two-stage methods**
    - Kim, J.; Kim, Y.; Kum, D. "[Low-level Sensor Fusion Network for 3D Vehicle Detection using Radar Range-Azimuth Heatmap and Monocular Image](https://openaccess.thecvf.com/content/ACCV2020/papers/Kim_Low-level_Sensor_Fusion_Network_for_3D_Vehicle_Detection_using_Radar_ACCV_2020_paper.pdf)." *In Proceedings of the Asian Conference on Computer Vision (ACCV)*, Virtual, 30 November–4 December 2020.
    - M. Meyer and G. Kuschk, "[Deep Learning Based 3D Object Detection for Automotive Radar and Camera](https://ieeexplore.ieee.org/document/8904867)," *2019 16th European Radar Conference (EuRAD)*, 2019, pp. 133-136.
    - K. Qian, S. Zhu, X. Zhang and L. E. Li, "[Robust Multimodal Vehicle Detection in Foggy Weather Using Complementary Lidar and Radar Signals](https://ieeexplore.ieee.org/document/9578621)," *2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2021, pp. 444-453.
  - **Anchor-free methods**
    - further avoid the complicated computation related to anchor boxes, such as calculating the IOU score during training
    - Yang, Bin, et al. "[Radarnet: Exploiting radar for robust perception of dynamic objects](https://link.springer.com/chapter/10.1007/978-3-030-58523-5_29)." *European Conference on Computer Vision*. Springer, Cham, 2020. 
    - Shah, Meet, et al. "[Liranet: End-to-end trajectory prediction using spatio-temporal radar fusion](https://arxiv.org/pdf/2010.00731.pdf)." *arXiv preprint arXiv:2010.00731* (2020).
- However, the fusion network may face the problem of **overlooking weak modalities** and **modality synergies**
- Training techniques are needed to force the network to learn from radar input


#### **Decision Fusion**
- Decision fusion **takes advantage of modal redundancy** and is therefore popular in real-world applications
  - **Location** information can be robustly fused in a track-to-track architecture or with the help of network semantics
  - **Category** information can be fused with Bayesian inference or evidence theory
- It assumes that objects are detected independently by different modalities and fuses them according to their spatial–temporal relationships
- This structure realises sensing redundancy at the **system level** and is therefore **robust to modalitywise error**
- Due to the **low resolution** of radar, most existing studies **do not** explicitly **consider** the **category** information estimated by radar
  - only fuse the location information from radar and vision branches
  - while retaining the category information estimated by vision
  - future fusion frameworks should consider both location and category information, since net-generation 4D radar can provide high resolution radar chips
- Location information can be optimally fused in a tracking framework
- Category information, especially the conflict in category predictions, is **difficult** to handle in sensor fusion
  - BayesOD proposes a probabilistic framework for fusing bounding boxes with categories
    - A. Harakeh, M. Smart and S. L. Waslander, "[BayesOD: A Bayesian Approach for Uncertainty Estimation in Deep Object Detectors](https://ieeexplore.ieee.org/abstract/document/9196544)," *2020 IEEE International Conference on Robotics and Automation (ICRA)*, 2020, pp. 87-93.
  - But probabilistic methods have their inherent shortage in modelling the lack of knowledge
    - Hüllermeier, Eyke, and Willem Waegeman. "[Aleatoric and epistemic uncertainty in machine learning: An introduction to concepts and methods](https://doi.org/10.1007/s10994-021-05946-3)." *Machine Learning* 110.3 (2021): 457-506.
  - Leverage and utilize the **evidential theory** to fuse the LiDAR, camera, and radar
    - R. O. Chavez-Garcia and O. Aycard, "[Multiple Sensor Fusion and Classification for Moving Object Detection and Tracking](https://ieeexplore.ieee.org/abstract/document/7283636)," in *IEEE Transactions on Intelligent Transportation Systems*, vol. 17, no. 2, pp. 525-534, Feb. 2016.
  - **Conformal prediction** can be used to generate confidence sets from a trained network using a small amount of calibration data
    - Angelopoulos, Anastasios N., and Stephen Bates. "[A gentle introduction to conformal prediction and distribution-free uncertainty quantification](https://arxiv.org/pdf/2107.07511.pdf)." *arXiv preprint arXiv:2107.07511* (2021).



#### **Challenges**
- Although deep radar perception shows good performance on datasets, there are few studies investigating the generalisation of these methods
- In fact, some challenging situations are overlooked, but may prohibit the use of these methods in real-world scenarios
- Summarise **3 challenges** for deep radar perception
  - the **ghost objects** caused by multi-path propagation are common in complex scenarios but rarely discussed
  - **over-confidence** is a general problem with neural networks
  - even though we always refer to radar as an all-weather sensor, **robustness in adverse weather** is not well tested in many radar fusion methods
- Firstly, **multi-path effects** need to be explicitly considered in object detection
- Secondly, need to alleviate the problem of **over-confidence** in radar classification and **estimate** the **uncertainty** in bounding box regression
- Thirdly, the fusion architecture should have adaptive mechanisms to take full advantage of radar’s **all-weather capabilities** -->



<!-- #### **Future Research Directions**
- Many research efforts have focused on developing models for detection tasks
- There are also some unexplored research topics or fundamental questions to be addressed
  - urgent need for **High-Quality Datasets**
  - **Radar Domain Knowledge** and **Uncertainty Quantification** can help developing a generalizable AI model
  - **Interference Mitigation**
  - **Motion Forecasting**
- Consider the perceptual system as a whole can **extend** the end-to-end learning **framework** forward or backward
  - **forward**, i.e. joint learning with **interference mitigation**
  - **backward**, i.e. **motion prediction**  -->



### 08/27
- 論文引用格式範例說明 [Purdue Online Writing Lab](https://owl.purdue.edu/owl/research_and_citation/apa_style/apa_formatting_and_style_guide/reference_list_other_print_sources.html) 引用碩論 APA 格式舉例:
  - 陳羽歡。「探討靈芝蛋白對於腸道表皮細胞完整性的影響」。碩士論文，國立臺灣大學免疫學研究所，2019。＜[https://hdl.handle.net/11296/6xpf28](https://hdl.handle.net/11296/6xpf28)＞。
  - Yu-Huan Chen. (2019). *Study the effect of Ling-Zhi 8 (LZ-8) on integrity of intestinal epithelial cell (IEC)* (DOI. 10.6342/NTU201901585) [Master Thesis, National Taiwan University] [https://hdl.handle.net/11296/6xpf28](https://hdl.handle.net/11296/6xpf28).
  - 台灣碩博論文網沒有看到 Publication No. 所以先放 DOI 頂一下。



### 08/31
- 跟王老師的下一次 meeting 是下下週三 09/14 下午 4 點
- 近期目標
  - 可以先產不同數量的 multi-target 訓練資料 + 有 clutter 的版本?
    - clutter 算是某種 ghost target 情況?
    - 但已經忘記郁庭的 code 的運作模式，又要再重頭開始 trace 一遍@@
  - 然後試試看 YOLO-CFAR 去偵測多目標的情況
    - 應該要可以完勝、預期應該是輕輕鬆鬆
    - 很久沒看 YOLOv3 希望能正常跑
    - YOLOv3 在 CPU 跟 GPU 上跑的程式設定不太一樣，都是 albumentation 那邊出問題，但實際問題是為啥還沒解，理論上應該是要像 Lab 電腦在 CPU 跑那樣，標籤應該要跟著 augmentation 一起動，而不是把 bbox augmentation 註解掉還能正常跑?
  - 確認之前的 code 都能正常跑，看第二次 trace 能不能有不一樣的收穫 ((現在應該勉強算有點了解 CFAR 了吧QQ
- 階段性目標 (沒有優先度先後順序) 
  - 搜尋除了透過畫頻譜圖 (RA / RD map, RAD tensor) 去分析之外，有什麼方法可以直接利用或處理 raw data 
    - 怎麼模擬 ADC raw data? 而不是直接生成 RD map
    - 也許可以先看看這篇 F. C. Akyon, Y. K. Alp, G. Gok and O. Arikan, "[Classification of Intra-Pulse Modulation of Radar Signals by Feature Fusion Based Convolutional Neural Networks](https://ieeexplore.ieee.org/abstract/document/8553176)," *2018 26th European Signal Processing Conference (EUSIPCO)*, 2018, pp. 2290-2294.
    - 了解上面那篇所謂的 "處理 raw signal" 是什麼意思? 跟我們想像的是同一件事嗎?
  - 試著將模擬更貼近真實世界的雷達訊號，像假設雷達打到行人或汽車的回波應該要不一樣，在寫模擬的時候得考慮到差異，且前處理或特徵提取時必須得有辦法保留這些差異的特徵
    - 怎麼模擬醬假設下的收到雷達回波訊號、CCM?
    - 也許能從 RCS 下手? 也許能找到考慮 RCS 參數的 RD map 模擬
  - 如果區分行人、自行車、機車、汽車、卡車太困難，也許可以至少做到區分小目標、中目標、大目標
    - 怎麼定義、區分大跟小?
  - 雖然論文直接寫說雷達由於解析度太差，即使有預測類別也是以影像或光達資料為準，但還是找找看有沒有方法能從 ADC data, RD/RA map, RAD tensor 去分類的?
    - 類別預測 vision > LiDAR > radar
  - 考慮自己重寫 RD map / RA map / RAD tensor 的模擬，仰賴郁庭的 legacy code 真的不知道啥時會出事@@
- 最終目標
  - 等東西都做好還要限制算力只能跟手機差不多
    - 錦上添花的部分?
  - 還要考慮資安問題
    - 希望到時黃老師會來當口委，可以聊網路安全的東東XD
  - 目標是投 IEEE VTC?


### 09/06
- 暐之和倚穎下午2點口試
- 跟鍾老師討論題目定位
  - 簡單報告 
    - Overview of Deep Radar Perception
    - Classical Detection Pipeline
    - Detection Frameworks
    - Future Works
  - 需要設定一個合理的物理模型去模擬 ADC data, if possible 但不要牽涉太多電波的部分
  - 目前看起來，模擬 ADC data 有點困難
- 下次 meeting 9/22 下午1點，繼續跟老師討論題目定位




### 09/07
- Radar Signature
  - there are 5 kinds of radar signatures
  - PointCloud
    - P. Aust, F. Hau, J. Dickmann and M. A. Hein, "[A Data-driven Approach for Stochastic Modeling of Automotive Radar Detections for Extended Objects](https://ieeexplore.ieee.org/document/9783497)," *2022 14th German Microwave Conference (GeMiC)*, 2022, pp. 80-83.
  - RCS
    - X. Cai, M. Giallorenzo and K. Sarabandi, "[Machine Learning-Based Target Classification for MMW Radar in Autonomous Driving](https://ieeexplore.ieee.org/document/9319548)," in *IEEE Transactions on Intelligent Vehicles*, vol. 6, no. 4, pp. 678-689, Dec. 2021.
    - X. Cai and K. Sarabandi, "[A Machine Learning Based 77 GHz Radar Target Classification for Autonomous Vehicles](https://ieeexplore.ieee.org/document/8888647)," *2019 IEEE International Symposium on Antennas and Propagation and USNC-URSI Radio Science Meeting*, 2019, pp. 371-372.
    - Patel, Jarez S., Francesco Fioranelli, and David Anderson. "[Review of radar classification and RCS characterisation techniques for small UAVs or drones](https://ietresearch.onlinelibrary.wiley.com/doi/pdf/10.1049/iet-rsn.2018.0020)." *IET Radar, Sonar & Navigation* 12.9 (2018): 911-919.
  - Phase
    - S. Lim, S. Lee, J. Yoon and S. -C. Kim, "[Phase-Based Target Classification Using Neural Network in Automotive Radar Systems](https://ieeexplore.ieee.org/document/8835725)," *2019 IEEE Radar Conference (RadarConf)*, 2019, pp. 1-6.
  - Motion
  - Polarimetric
- Detector
  - Z. Cao, W. Fang, Y. Song, L. He, C. Song and Z. Xu, "[DNN-Based Peak Sequence Classification CFAR Detection Algorithm for High-Resolution FMCW Radar](https://ieeexplore.ieee.org/document/9547416)," in *IEEE Transactions on Geoscience and Remote Sensing*, vol. 60, pp. 1-15, 2022, Art no. 5106115.
  - DL-CFAR
  - O. Bialer, D. Shapiro and A. Jonas, "[Object Surface Estimation from Radar Images](https://ieeexplore.ieee.org/document/9054622)," *ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2020, pp. 4132-4136.
  - D. Gusland, S. Rolfsjord and B. Torvik, "[Deep temporal detection - A machine learning approach to multiple-dwell target detection](https://ieeexplore.ieee.org/document/9114828)," *2020 IEEE International Radar Conference (RADAR)*, 2020, pp. 203-207.
- Super Resolution
  - M. Stephan, T. Stadelmayer, A. Santra, G. Fischer, R. Weigel and F. Lurz, "[Radar Image Reconstruction from Raw ADC Data using Parametric Variational Autoencoder with Domain Adaptation](https://ieeexplore.ieee.org/document/9412858)," *2020 25th International Conference on Pattern Recognition (ICPR)*, 2021, pp. 9529-9536.
- Object Detection
  - ADC 
    - Rebut, Julien, et al. "[Raw High-Definition Radar for Multi-Task Learning](https://openaccess.thecvf.com/content/CVPR2022/papers/Rebut_Raw_High-Definition_Radar_for_Multi-Task_Learning_CVPR_2022_paper.pdf)." *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*. 2022.
  - pre-CFAR
    - M. Meyer, G. Kuschk and S. Tomforde, "[Graph Convolutional Networks for 3D Object Detection on Radar Data](https://ieeexplore.ieee.org/document/9607427)," *2021 IEEE/CVF International Conference on Computer Vision Workshops (ICCVW)*, 2021, pp. 3053-3062.
    - B. Major et al., "[Vehicle Detection With Automotive Radar Using Deep Learning on Range-Azimuth-Doppler Tensors](https://ieeexplore.ieee.org/document/9022248)," *2019 IEEE/CVF International Conference on Computer Vision Workshop (ICCVW)*, 2019, pp. 924-932.


### 09/14
- meeting on 4 p.m.
- Original goals
  - find some ways to **simulate** ADC raw data
  - find some other ways, besides plotting RD maps, to **process** ADC raw data
  - among these possible methods, find one that best preserve class features
- Radar Signature
  - there are 5 kinds of radar signatures we may be able to use
    - PointCloud
    - RCS
    - Phase
    - Motion
    - Polarimetric
  - most papers are based on **real radar measurements**
- PointCloud
  - P. Aust, F. Hau, J. Dickmann and M. A. Hein, "[A Data-driven Approach for Stochastic Modeling of Automotive Radar Detections for Extended Objects](https://ieeexplore.ieee.org/document/9783497)," *2022 14th German Microwave Conference (GeMiC)*, 2022, pp. 80-83.
  - trained and tested with **real sensor data**
  - cited by 0
- RCS
  - X. Cai, M. Giallorenzo and K. Sarabandi, "[Machine Learning-Based Target Classification for MMW Radar in Autonomous Driving](https://ieeexplore.ieee.org/document/9319548)," in *IEEE Transactions on Intelligent Vehicles*, vol. 6, no. 4, pp. 678-689, Dec. 2021.
  - presents 4 automotive radar target classification models
    - statistical RCS (point target) 
    - time-domain RCS (distributed target in range) 
    - RA map radar images 
    - 3D radar images
  - comprehensive simulated dataset with Asymptotic methods
  - Physical Optics (PO) method 
    - M. Vahidpour and K. Sarabandi, "[Millimeter-Wave Doppler Spectrum and Polarimetric Response of Walking Bodies](https://ieeexplore.ieee.org/document/6138909)," in *IEEE Transactions on Geoscience and Remote Sensing*, vol. 50, no. 7, pp. 2866-2879, July 2012. (cited by 29)
    - Obelleiro, F., M. G. Araujo, and J. L. Rodriguez. "[Iterative physical‐optics formulation for analyzing large waveguides with lossy walls](https://onlinelibrary.wiley.com/doi/pdf/10.1002/1098-2760(20010105)28:1%3C21::AID-MOP6%3E3.0.CO;2-4)." Microwave and Optical Technology Letters 28.1 (2001): 21-26. (cited by 35)
  - Physical Theory of Diffraction (PTD) method
    - R. G. Kouyoumjian and P. H. Pathak, "[A uniform geometrical theory of diffraction for an edge in a perfectly conducting surface](https://ieeexplore.ieee.org/document/1451581)," in Proceedings of the IEEE, vol. 62, no. 11, pp. 1448-1461, Nov. 1974. (cited by 1977)
    - P. H. Pathak, G. Carluccio and M. Albani, "[The Uniform Geometrical Theory of Diffraction and Some of Its Applications](https://ieeexplore.ieee.org/document/6645140)," in IEEE Antennas and Propagation Magazine, vol. 55, no. 4, pp. 41-69, Aug. 2013. (cited by 65)
  - in this paper, the **PO method** is used since most common traffic targets do not often present any sharp edges and are for the most parts convex
  - cited by 7
<!--     - X. Cai and K. Sarabandi, "[A Machine Learning Based 77 GHz Radar Target Classification for Autonomous Vehicles](https://ieeexplore.ieee.org/document/8888647)," *2019 IEEE International Symposium on Antennas and Propagation and USNC-URSI Radio Science Meeting*, 2019, pp. 371-372.
    - Patel, Jarez S., Francesco Fioranelli, and David Anderson. "[Review of radar classification and RCS characterisation techniques for small UAVs or drones](https://ietresearch.onlinelibrary.wiley.com/doi/pdf/10.1049/iet-rsn.2018.0020)." *IET Radar, Sonar & Navigation* 12.9 (2018): 911-919. -->
  - Phase
    - S. Lim, S. Lee, J. Yoon and S. -C. Kim, "[Phase-Based Target Classification Using Neural Network in Automotive Radar Systems](https://ieeexplore.ieee.org/document/8835725)," *2019 IEEE Radar Conference (RadarConf)*, 2019, pp. 1-6.
- Detector
  - Z. Cao, W. Fang, Y. Song, L. He, C. Song and Z. Xu, "[DNN-Based Peak Sequence Classification CFAR Detection Algorithm for High-Resolution FMCW Radar](https://ieeexplore.ieee.org/document/9547416)," in *IEEE Transactions on Geoscience and Remote Sensing*, vol. 60, pp. 1-15, 2022, Art no. 5106115.
    - convert the target detection into a problem of peak sequence classification of frequency intensity (FI) measurements
    - results are based on the **real dataset** collected from **road scenes**
    - cited by 1
  - DL-CFAR
    - cited by 18
  - O. Bialer, D. Shapiro and A. Jonas, "[Object Surface Estimation from Radar Images](https://ieeexplore.ieee.org/document/9054622)," *ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2020, pp. 4132-4136.
    - DNN method for estimating the object surface from 2D radar RA map image
    - classification bits determining whether or not there is a reflection per angle, and the associated reflection range (range regression?)
    - results obtained from **real radar measurements**
    - cited by 0
  - D. Gusland, S. Rolfsjord and B. Torvik, "[Deep temporal detection - A machine learning approach to multiple-dwell target detection](https://ieeexplore.ieee.org/document/9114828)," *2020 IEEE International Radar Conference (RADAR)*, 2020, pp. 203-207.
    - use a CNN on RD map images and stack 3 RD maps as layers, called the Temporal CNN detector
    - trained and tested solely on **measured radar data**
- Super Resolution
  - M. Stephan, T. Stadelmayer, A. Santra, G. Fischer, R. Weigel and F. Lurz, "[Radar Image Reconstruction from Raw ADC Data using Parametric Variational Autoencoder with Domain Adaptation](https://ieeexplore.ieee.org/document/9412858)," *2020 25th International Conference on Pattern Recognition (ICPR)*, 2021, pp. 9529-9536.
- Object Detection
  - ADC 
    - Rebut, Julien, et al. "[Raw High-Definition Radar for Multi-Task Learning](https://openaccess.thecvf.com/content/CVPR2022/papers/Rebut_Raw_High-Definition_Radar_for_Multi-Task_Learning_CVPR_2022_paper.pdf)." *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*. 2022.
  - pre-CFAR
    - M. Meyer, G. Kuschk and S. Tomforde, "[Graph Convolutional Networks for 3D Object Detection on Radar Data](https://ieeexplore.ieee.org/document/9607427)," *2021 IEEE/CVF International Conference on Computer Vision Workshops (ICCVW)*, 2021, pp. 3053-3062.
    - B. Major et al., "[Vehicle Detection With Automotive Radar Using Deep Learning on Range-Azimuth-Doppler Tensors](https://ieeexplore.ieee.org/document/9022248)," *2019 IEEE/CVF International Conference on Computer Vision Workshop (ICCVW)*, 2019, pp. 924-932.


### 09/15
- 下次 meeting 是 9/21 下週三下午 4 點
- 超短期目標
  - 確認有哪些公開資料集可以取得，最好有附論文或範例程式
    - 簡介資料集的樣子、型態
    - 怎麼蒐集的?
    - 標籤標記的樣式、格式
    - 要怎麼用?
  - 資料集可以用在哪些任務
  - 相關方法有哪些
    - 例如，已經很多人用 YOLOv3 去解 SAR images 資料集的目標偵測問題
  - 準備一個回顧或彙整
    - 總結看過哪些資料集
    - 為什麼用? 或為什麼不用?
    - 要用的話，要怎麼用? 要引用誰的論文才不失學術倫理?
- 跟鍾老師討論多個質點的雷達模擬假設合理性
  - 結論是鍾老師覺得這樣假設沒問題，只是還有很多細節需要釐清
  - 假設成人的雷達回波是由 3 個理想反射點去模擬；汽車的回波是由 10 個理想反射點去模擬，這裡是先武斷假設點數
    - 最好能找到文獻支撐理想反射點點數的假設
    - 但如何找? 可否以 RCS 去近似?
  - 得考慮雷達跟物體距離的近場、遠場問題
    - 近場意思是，多個理想反射點的物理特性可以分開考慮
    - 遠場的話，因為雷達跟受測物距離很遠，儘管有多個反射點，但回波看起來就是一個點的反射
    - 多近是近? 多遠是遠?
  - 從陣列訊號處理來看，10~20倍是個大致合理的參數
    - 若雷達跟受測物的距離為受測物大小的10倍以內，通常可以視為近場
    - 反之，若雷達跟受測物的距離為受測物大小的20倍以上，通常視為遠場
    - 而10~20倍的範圍則是某種模糊空間


### 09/17
- 通訊理論
  - 複習到 2.1-1 Bandpass and Lowpass Signas, p.21 
  - 預習到 2.2 結束, p.40 然後 2.3 Random Variables 能看多少算多少



### 09/19
- Radar Dataset
  - A. Ouaknine, A. Newson, J. Rebut, F. Tupin and P. Pérez, "[CARRADA Dataset: Camera and Automotive Radar with Range- Angle- Doppler Annotations](https://ieeexplore.ieee.org/document/9413181)," *2020 25th International Conference on Pattern Recognition (ICPR)*, 2021, pp. 5068-5075.
    - paper with code has [3](https://paperswithcode.com/paper/carrada-dataset-camera-and-automotive-radar) implementations all in PyTorch
    - github repo [carrada_dataset](https://github.com/valeoai/carrada_dataset)
  - D. Gusland, J. M. Christiansen, B. Torvik, F. Fioranelli, S. Z. Gurbuz and M. Ritchie, "[Open Radar Initiative: Large Scale Dataset for Benchmarking of micro-Doppler Recognition Algorithms](https://ieeexplore.ieee.org/document/9455239)," *2021 IEEE Radar Conference (RadarConf21)*, 2021, pp. 1-6.
    - github repo [open_radar_datasets](https://github.com/openradarinitiative/open_radar_datasets)
    - assisted living dataset [CI4R-Human-Activity-Recognition-datasets](https://github.com/ci4r/CI4R-Activity-Recognition-datasets)



### 09/22
- Original goals
  - looking for ready-to-use and easy-to-use public datasets
  - discuss the reasonableness of our provious thoughts on radar simulation settings
- Radar Dataset
  - A. Ouaknine, A. Newson, J. Rebut, F. Tupin and P. Pérez, "[CARRADA Dataset: Camera and Automotive Radar with Range- Angle- Doppler Annotations](https://ieeexplore.ieee.org/document/9413181)," *2020 25th International Conference on Pattern Recognition (ICPR)*, 2021, pp. 5068-5075.
    - paper with code has [3](https://paperswithcode.com/paper/carrada-dataset-camera-and-automotive-radar) related implementations all in PyTorch
    - github repo [carrada_dataset](https://github.com/valeoai/carrada_dataset)
    - the dataset is available on Arthur Ouaknine's personal web page using this [link](https://arthurouaknine.github.io/codeanddata/carrada)
  - D. Gusland, J. M. Christiansen, B. Torvik, F. Fioranelli, S. Z. Gurbuz and M. Ritchie, "[Open Radar Initiative: Large Scale Dataset for Benchmarking of micro-Doppler Recognition Algorithms](https://ieeexplore.ieee.org/document/9455239)," *2021 IEEE Radar Conference (RadarConf21)*, 2021, pp. 1-6.
    - github repo [open_radar_datasets](https://github.com/openradarinitiative/open_radar_datasets)
    - assisted living dataset [CI4R-Human-Activity-Recognition-datasets](https://github.com/ci4r/CI4R-Activity-Recognition-datasets)


#### **CARRADA Dataset**
- Carrada.tar.gz (22.9 GB)
  - Carrada.tar (90 GB)
  ![](https://i.imgur.com/5Uvs38T.png)
  - e.g. inside "2020-02-28-13-15-36" folder
  ![](https://i.imgur.com/1W822Nx.png)
  - synchronized camera and radar views with generated annotations
    - materials for the semi-automatic pipeline
- Carrada_RAD.tar.gz (198 GB)
  - RAD tensor per sequence only, with no annotations
- Annotations and Classes
  - bounding boxes
    ![](https://i.imgur.com/PeCCble.png)
    - possibly COCO format, but does not looks the same
        ```jsonld!
        annotation {
        "id" : int,
        "image_id": int,
        "category_id": int,
        "segmentation": RLE or [polygon],
        "area": float,
        "bbox": [x,y,width,height],
        "iscrowd": 0 or 1,
        }
        categories[{
        "id": int,
        "name": str,
        "supercategory": str,
        }]
        ```
      ![](https://i.imgur.com/08BaqAi.png)
  - sparse points 
  - dense masks
  - above **3** annotations are provided for range-Doppler and range-angle representations
  - each object has a unique class identier, being categorized as a **pedestrian**, a **car** or a **cyclist**
- Images and Radar data 
  - image resolution is 1238 x 1028 pixels 
  - 2D RD map with size of 256 x 64 
  - 2D RA map with size of 256 x 256
  - sensors are calibrated to have the same **Cartesian coordinate** system
<img src="https://i.imgur.com/Zh6cupd.png" width=60% height=60%>
![](https://i.imgur.com/4COIFjE.png)
- Possible tasks
  - object detection 
  - semantic segmentation
  - tracking in raw radar signals 
  - sensor fusion in temporal data
- The dataset has been recorded in **Canada** on a **test track** to reduce environmental noise
  - the acquisition setup are with a **FMCW radar** and a **camera** mounted on a **stationary** car
  - the radar uses the **MIMO system** conguration with **2 Tx** and **4 Rx** producing a total of 8 virtual antennas
  - the camera and the radar data are synchronized to have the **same frame rate** in the dataset
- The parameters and specications of the sensor
<img src="https://i.imgur.com/41ASmge.png" width=70% height=70%>
<!--   - **Performances** are evaluated for each radar representation for each category
    - Intersection over Union (IoU)
    - Pixel Accuracy (PA) 
    - Pixel Recall (PR) 
    - metrics by category are aggregated using arithmetic and harmonic means -->

#### **Outdoor Moving Object Dataset**
- The Dataset can be downloaded from [google drive](https://drive.google.com/uc?id=1CJyTqtCM4kOSQt2X7n2NgWCVEqou8RCB)
  - this dataset is in a "ground surveillance" setting
  - data has been collected with a **stationary radar** and **targets moving in the front** of the radar
- Dataset content
  - the dataset is a python dictionary that stores as a ".npy" file
    - similar to a pickle file, which is pretty dangerous to unwrap
  - the ".npy" file contains a dictionary of signatures, each signature corresponds to a full radar-track and contains:
    | Field name | Explanation |
    | ---------- | ----------- |
    | signature  |  Numpy array of the doppler spectra for that track|
    | ts         |  Timestamp for each spectra|
    | range      |  Measured range for the detection|
    | azimuth    |  Measured azimuth for the detectin|
    | velocity   |  Measured radial velocity|
    | snr_db     |  Estimated SNR in dB, estimated from a 1D CFAR|
    | x          |  Kalman-filtered x-position|
    | y          |  Kalman-filtered x-position|
    | z          |  Kalman-filtered x-position|
    | class_name |  Class name string|
    | radar_parameters |  Dict with the radar parameters|
  - the radar parameters dict contain sensor and waveform-specific parameters
    | Field name | Explanation |
    | ---------- | ----------- |
    | num_range_bins |  Number of range bins|
    | num_pulses |  Number of pulses in each frame|
    | num_antenna_elements |  Number of receiver elements sampled|
    | fc |  Center frequency|
    | bw |  Sampled Bandwidth|
    | prf |  PRF|
- Sample code for Outdoor Moving Object Dataset
```python
# first load the dataset as a .npy file from google drive 
# https://drive.google.com/uc?id=1CJyTqtCM4kOSQt2X7n2NgWCVEqou8RCB
import numpy as np
from matplotlib import pyplot as plt

# Print the classes in the dataset
filename = "D:\Datasets\OpenRadar\moving_target_dataset.npy"
signatures = np.load(filename, allow_pickle=True)

class_names = []
for signature in signatures:
    if not any(signature['class_name'] in s for s in class_names):
        class_names.append(signature['class_name'])

print(class_names) # ['vehicle', 'person', 'bicycle', 'uav']

# View the dataset
is_shown = {}
for class_name in class_names:
    is_shown[class_name] = False

# Shows some samples of the dataset
for signature in signatures:
    if len(signature['snr_db']) <= 500: continue
    if signature['class_name']!="uav" or len(signature['snr_db']) <= 100: continue
    if not is_shown[signature['class_name']]:
        is_shown[signature['class_name']] = True
        arr = signature['signature']
        arr = 20 * np.log10(np.abs(arr)).transpose()
        prf = signature['radar_parameters']['prf']

        def plot_some_samples():
            plt.imshow(arr, cmap='jet', aspect='auto', 
                       vmax=np.max(arr) - 20, 
                       vmin=np.max(arr) - 70, 
                       extent=[0, arr.shape[1], -int(prf/2), int(prf / 2)])
            plt.title(signature['class_name'])
            plt.autoscale()
            plt.xlabel('Time (seconds) in samples')
            plt.ylabel('Doppler frequency shift (Hz)')
            plt.show()

        # plot_some_samples()
```
![](https://i.imgur.com/Jh0ILsr.png)
![](https://i.imgur.com/avohsBv.png)
```python
# The files in the dataset are of long tracks of each subject, 
# to use them for ML/DL tests, it is important that we split 
# the data on the track-basis an not only spectra. We therefore 
# perform the spliting at this point.
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

all_indices = list(range(len(signatures)))
train_indices, test_indices = train_test_split(all_indices, 
                                               test_size=0.2, 
                                               random_state=42)

le = preprocessing.LabelEncoder()
le.fit_transform(class_names)

# for index in train_indices:
train_signatures = [signatures[i] for i in train_indices]
test_signatures = [signatures[i] for i in test_indices]

# Count the Number of samples:
n_samples_train = 0
n_samples_test = 0
for signature in train_signatures:
    n_samples_train += len(signature['ts'])

for signature in test_signatures:
    n_samples_test += len(signature['ts'])

print(f"Train dataset size: {n_samples_train}") 
print(f"Test dataset size:  {n_samples_test}")  
# Train dataset size: 151455
# Test dataset size:  35937

# These two datasets now contain everything we need to do classification 
# research. We simply have to slice the spectrograms into convenient sizes 
# and start the challenge. Each spectra contains 1008 Doppler bins and 
# concatinating 10 spectra corresponds to half a second observation time.
```



### 09/27
- 在 IEEE 有 [8](https://ieeexplore.ieee.org/document/9413181/citations?tabFilter=papers#citations) 篇文章引用，在 google scholar 可以找到 [43](https://scholar.google.com.tw/scholar?cites=4617103630695360689&as_sdt=2005&sciodt=0,5&hl=zh-TW) 篇。
  - R. Zheng, S. Sun, D. Scharff and T. Wu, "[Spectranet: A High Resolution Imaging Radar Deep Neural Network for Autonomous Vehicles](https://ieeexplore.ieee.org/document/9827798)," *2022 IEEE 12th Sensor Array and Multichannel Signal Processing Workshop (SAM)*, 2022, pp. 301-305.
    - proposed a novel **signal processing pipeline** to address the max ambiguous velocity reduction issue introduced by staggered TDM scheme of high resolution imaging radar system
    - generate high resolution radar RA spectra without information loss
  - C. Grimm, T. Fei, E. Warsitz, R. Farhoud, T. Breddermann and R. Haeb-Umbach, "[Warping of Radar Data Into Camera Image for Cross-Modal Supervision in Automotive Applications](https://ieeexplore.ieee.org/document/9797876)," in *IEEE Transactions on Vehicular Technology*, vol. 71, no. 9, pp. 9435-9449, Sept. 2022.


### 10/03
- 跟鍾老師討論訓練資料的問題
- 家裡主機的 ```Anaconda``` 環境有問題!
  - 所有虛擬環境(不知為何)竟然是切割在 ```.conda``` 的 ```envs``` 底下，而不是預設 ```D:\ProgramData\Anaconda3\envs``` 的路徑
  - 現在遇到及未來潛在問題是已安裝的 ```package``` 會讀不到
  - 安裝的 ```package``` 會被分成裝在 ```base``` 跟裝在 ```env_name``` (比如 ```ipy3.6``` 等等) 底下，然後能不能正常讀取就看運氣
  - 目前是發現若用 ```ipykernel``` 會爆炸



### 10/04
- 必須要認真解決讀資料的問題!



### 10/19
- All bugs remain unfixed 先不管 read_carrada smaple code 的問題
- 當前最重要的目標是
  - 可以用 CARRADA Dataset 的資料讓 YOLOv3 跑起來
  - 至少確認可以解決 RD Map 的目標偵測問題，因為 RA Map 的部分超難
- 可以找另一個可以讀 COCO format / JSON string 的 YOLOv3 把東西跑起來
  - 光是要把另一個 YOLOv3 跑起來並確認基本的正確性就很煩
  - 無法確定可以讀 json string 的 annotation，畢竟 CARRADA Dataset 的格式跟標準的(? COCO format 也不太一樣
- 也可以把 annotation 從 COCO format 整理成 YOLO foramt，醬就能餵進之前確認過大致可行的 YOLOv3
  - 但記得還有很多 unfixed bugs! 而且在家裡跟在學校電腦的執行結果不一樣!!
  - 至少知道用 CPU 跑的跟 GPU 跑的結果不一樣，是 albumentation 的預期結果不一樣
  - 理論上原電腦用 CPU 跑的才是最正確的，但那台現在已經半報廢狀態
- 對法二目前有 3 個想法可以試試看/待確認
  - 先從 json file 把有 bbox annotation 的字串原封不動 parse 出來，重新寫成 .txt file 的 YOLO format
  - 把 parse 出來的 annotation 重新 rescale 成 256-by-256 的大小，也就是把 x 軸 (Doppler 軸) 拉長 / 放大 4 倍，好方便直接餵進之前的 YOLOv3，因為不確定餵長方形 (64-by-256) 的 image / matrix 他的 feature map size 對不對得上
  - 把同一張 256-by-256 的 image 保持不變切成 4 張，每張都是 64-by-64，但很有可能滿多圖片會變成沒有目標
- 注意事項
  - COCO format 的 json string 給的是絕對大小!
- 在 GeeksForGeeks 有 [Python JSON](https://www.geeksforgeeks.org/python-json/) 教學
- 首要問題 [COCO json annotation to YOLO txt format](https://stackoverflow.com/questions/68398965/coco-json-annotation-to-yolo-txt-format)
  - 選項一 [coco2yolo](https://github.com/tw-yshuang/coco2yolo)
  - 選項二 [pylabel](https://github.com/pylabel-project/pylabel)
    - ```pip install pylabel```
    - 還可以找到 ```pyabel```, 跟 ```pylabels``` 這兩個不是我們要的XD



### 11/23
- C. Decourt, R. VanRullen, D. Salle and T. Oberlin, "[DAROD: A Deep Automotive Radar Object Detector on Range-Doppler maps](https://ieeexplore.ieee.org/document/9827281)," *2022 IEEE Intelligent Vehicles Symposium (IV)*, 2022, pp. 112-118.
  - Author [Colin Decourt](https://scholar.google.com.tw/citations?hl=zh-TW&user=ffntya4AAAAJ) PhD student at ANITI (Artificial and Natural Intelligence Toulouse Institute)
  - Université fédérale Toulouse Midi-Pyrénées is one of the top universities in Toulouse, France. It is ranked #301-350 in [QS WUR Ranking](https://www.mastersportal.com/rankings-reviews/17168/federal-university-of-toulouse-midi-pyrnes.html) By Subject 2021.


#### **Overview**
- Automotive radar object detection in RD maps using Faster R-CNN for edge computing scenario
- Datasets
  - A. Ouaknine, A. Newson, J. Rebut, F. Tupin and P. Pérez, "[CARRADA Dataset: Camera and Automotive Radar with Range- Angle- Doppler Annotations](https://ieeexplore.ieee.org/abstract/document/9413181)," *2020 25th International Conference on Pattern Recognition (ICPR)*, 2021, pp. 5068-5075. (cited by 50)
  - A. Zhang, F. E. Nowruzi and R. Laganiere, "[RADDet: Range-Azimuth-Doppler based Radar Object Detection for Dynamic Road Users](https://ieeexplore.ieee.org/document/9469418)," *2021 18th Conference on Robots and Vision (CRV)*, 2021, pp. 95-102. (cited by 20)
- Method
  - S. Ren, K. He, R. Girshick and J. Sun, "[Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks](https://ieeexplore.ieee.org/document/7485869)," in *IEEE Transactions on Pattern Analysis and Machine Intelligence*, vol. 39, no. 6, pp. 1137-1149, 1 June 2017.
- Computations performed to train the model have been carried out using the [OSIRIM](https://www.irit.fr/en/plateformes/our-platform-osirim/) platform
  - OSIRIM consists of a storage area with a capacity of approximately 1PB and a computing cluster of 928 cores and 31 GPUs
- Test environment
  - Tensorflow DL framework
  - Nvidia RTX 2080 Ti GPU
- Results
  - results of different models on CARRADA and RADDet datasets (Best results are shown in **bold**, second best are underlined)
![](https://i.imgur.com/rRiebN1.png)
  - they select [Torchvision Faster R-CNN](https://pytorch.org/vision/main/models/faster_rcnn.html) implementation using the default hyper-parameters
    - resize the input from 256×64 to 800×800
    - ResNet50 + FPN backbone pretrained on ImageNet
  - Number of FLOPS v. mAP@0.5
![](https://i.imgur.com/uEA7Cq3.png)


#### **Main contributions**
- Propose a new model architecture for object detection and classifcation using **Faster R-CNN**
  - Faster R-CNN architecture
![](https://i.imgur.com/on33sGv.png)
- Propose a lightweight backbone architecture
![](https://i.imgur.com/VrPQQLK.png)
  - the backbone is composed of **two blocks** with two 2D convolutions and **one block** with three 2D convolutions


#### **Useful insights**
- Why not use **YOLO-like** architecture?
  - ther are already **2** papers use **YOLOv3** and **YOLOv2** for detection and classification on **RAD** tensors and **RD** maps
    - R. Pérez, F. Schubert, R. Rasshofer and E. Biebl, "[Deep Learning Radar Object Detection and Classification for Urban Automotive Scenarios](https://ieeexplore.ieee.org/abstract/document/8890199)," 2019 Kleinheubach Conference, 2019, pp. 1-4.
    - K. Fatseas and M. J. G. Bekooij, "[Neural Network Based Multiple Object Tracking for Automotive FMCW Radar](https://ieeexplore.ieee.org/abstract/document/9078996)," 2019 International Radar Conference (RADAR), 2019, pp. 1-5.
  - **squaring** and **up-sampling** steps might result in loss of information in the RD spectrum
- Why not use **RAD tensors** like most works?
  - although RAD tensors provide the most informative data, they are **cumbersome to compute** for radar processors
  - RAD tensors are more **computationally demanding** to produce for radar Micro Controller Units (MCUs)
- Why solely use RD map for radar object detection?
  - **RA** views are **not adequate representations** either
  - in the purpose of object detection, RA maps are **not necessary**
  - RA maps usually suffer from a **poor angular resolution** caused by a small number of antennas in the FMCW radar
- Why additionally consider mAP at **IoU** thresholds **0.3**?
  - to take into account the uncertainty on the annotations, which is generated semi-automatically for both datasets
- Anchor and feature map statistics
  - Faster R-CNN also need 9 anchors, they use 3 scales and 3 aspect ratios for anchors generation
  - **mean** size of objects in RD maps is **8×8**, **min** size is **4x4**, **max** size is **16x16**
  - **feature map** size **32x32** was found to lead to the best performance
- Some tricks to boost performance?
  - RD spectrum is not translation invariant
  - add this (velocity) information to the feature vector used for classifcation and bounding box regression
  - $v = \delta_v * p$
    - estimated velocity = (resolution of the radar) * (position of the highest pixel in the ROI) 
    - ROI, here, means region within the feature map, I think


#### **Appendix**
- Table I

![](https://i.imgur.com/aa6zvy1.png)



### 11/26
- Wang, Chien-Yao, Alexey Bochkovskiy, and Hong-Yuan Mark Liao. "[YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors](https://arxiv.org/abs/2207.02696v1)." *arXiv preprint arXiv:2207.02696* (2022).


### 12/21
- M. Yao, L. Chen, J. Zhang, J. Huang and J. Wu, "[Loading Cost-Aware Model Caching and Request Routing for Cooperative Edge Inference](https://ieeexplore.ieee.org/document/9838823)," *ICC 2022 - IEEE International Conference on Communications*, 2022, pp. 2327-2332.
- Y. Shen, J. Zhang and K. B. Letaief, "[How Neural Architectures Affect Deep Learning for Communication Networks?](https://ieeexplore.ieee.org/document/9839205)," *ICC 2022 - IEEE International Conference on Communications*, 2022, pp. 389-394.




### 值得關注的作者
- 偶爾看一下他們有沒有出什麼新東西可以跟XD
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
  - [Jung-Chieh Chen](https://ieeexplore.ieee.org/author/37280673400)


