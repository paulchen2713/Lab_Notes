# **meeting 08/31**

**Advisor: Dr. Chih-Yu Wang**
**Presenter: Shao-Heng Chen**
**Date: August 31, 2022**


Zhou, Yi, et al. "[Towards Deep Radar Perception for Autonomous Driving: Datasets, Methods, and Challenges](https://www.mdpi.com/1424-8220/22/11/4208)." *Sensors* 22.11 (2022): 4208.

![](https://i.imgur.com/l7XqEq6.png)

<!-- ![](https://i.imgur.com/F9BTUY1.png) -->


## **Overview**
- Overview of **Deep Radar Perception**
- Upstream tasks
  - radar **signal processing**
  - radar **datasets** preparing
  - **labelling**
  - data **augmentation**
- Downstream tasks
  - object **detection**
  - depth and velocity **estimation** 
  - sensor **fusion**
- Overlooked challenges
  - multi-path effects
  - uncertainty problems 
  - adverse weather effects
<!-- - The next-generation 4D radar advantages 
  - long detection range 
  - all-weather operation 
  - low power consumption 
  - low cost -->



## **Radar Object Detection**
- Due to low resolution, classical radar detection algorithm has limited classification capability
  - At hardware level, next-generation imaging radars can output high-resolution point clouds
  - At algorithm level, NN show their potentials to learn better features from the dataset
- There is a broader definition of **radar detection**, like
  - **pointwise** detection
  - **2D/3D bounding box** detection
  - **instance segmentation**
  ![](https://i.imgur.com/JANGlmI.png)
  ![](https://i.imgur.com/OEtPTRn.png)
  - source: O. Schumann, M. Hahn, J. Dickmann and C. Wöhler, "[Supervised Clustering for Radar Applications: On the Way to Radar Instance Segmentation](https://ieeexplore.ieee.org/document/8443534)," *2018 IEEE MTT-S International Conference on Microwaves for Intelligent Mobility (ICMIM)*, 2018, pp. 1-4.
- According to the input data structure, we classify the **deep radar detection** into 2 classes
  - **point-cloud-based**, similar to LiDAR point cloud
  - **pre-CFAR-based**, similar to visual image
<!-- - Focus on how the **radar domain knowledge** can be incorporated into these networks to address the **low SNR problem**
  - applied on networks design?
  - explainations on why they works?
  - how low the SNR is low? -->
- Overview of radar detection frameworks
![](https://i.imgur.com/O7Nlu0Y.png)


## **Classical Detection Pipeline**
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



## **Datasets, Labelling, and Augmentation**
- Data play a key role in the learning-based approaches
- Radar Datasets w.r.t their **data representations**, **tasks**, scenarios, and **annotation types** are summarised below
- Also introduce extrinsic calibration and cross-modality labelling techniques
- And further investigate **data augmentation methods** and the potential use of **synthetic radar data** to improve data **diversity**


## **Radar Datasets**
- Radar classification w.r.t their **resolution**
  - LR, Low Resolution
    - FMCW Radar e.g. TI AWR 1642, TI AWR 1843
  - HR, High Resolution 
    - Polarimetric Radar
    - Cooperative Radars
    - Multi-chip Cascaded MIMO Radar
    - Synthetic Aperture Radar (**SAR**)
    - Spinning Radar
  - most off-the-shelf radars will output a **point cloud** with range, azimuth angle, Doppler velocity, and RCS
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


## **Data Augmentation**
- Data augmentation plays an essential role in improving the generalization of deep learning models
- Data augmentation techniques can significantly improve the performance of **RA-map**-based radar detection
  - according to the summary report of the Radar Object Detection 2021 (**ROD2021**) **Challenge**
    - Wang, Yizhou, et al. "[ROD2021 Challenge: A Summary for Radar Object Detection Challenge for Autonomous Driving Applications](https://dl.acm.org/doi/10.1145/3460426.3463658)." *Proceedings of the 2021 International Conference on Multimedia Retrieval*. 2021.
- Base on the **radar representation** / data structure, the augmentation techniques can be divided into **2** types
  - **spectral**-based for pre-CFAR data
  - **pointcloud**-based for pointcloud
- It can also be featured as **local** or **global** depending on whether the entity being augmented is a **single object** or the **entire scene**


## **Synthetic Data**
- Synthetic datasets are widely used in Computer Vision and LiDAR perception 
- Networks trained with synthetic data can actually generalize well in the real-world
  - Johnson-Roberson, Matthew, et al. "[Driving in the matrix: Can virtual worlds replace human-generated annotations for real world tasks?](https://arxiv.org/pdf/1610.01983.pdf)." *arXiv preprint arXiv:1610.01983* (2016).
- The **labelling cost can be completely avoided**
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
- **Generative models**
  - GAN-based LiDAR-to-radar generation
    - Wang, Leichen, Bastian Goldluecke, and Carsten Anklam. "[L2R GAN: LiDAR-to-radar translation](https://openaccess.thecvf.com/content/ACCV2020/papers/Wang_L2R_GAN_LiDAR-to-Radar_Translation_ACCV_2020_paper.pdf)." *Proceedings of the Asian Conference on Computer Vision (ACCV)*. 2020.
  - GAN-based radar-to-image generation
    - Lekic, Vladimir, and Zdenka Babic. "[Automotive radar and camera fusion using generative adversarial networks](https://www.sciencedirect.com/science/article/pii/S1077314219300530)." *Computer Vision and Image Understanding* 184 (2019): 1-8.
  - VAE-based radar-to-image generation
    - C. Ditzel and K. Dietmayer, "[GenRadar: Self-Supervised Probabilistic Camera Synthesis Based on Radar Frequencies](https://ieeexplore.ieee.org/document/9570339)," in *IEEE Access*, vol. 9, pp. 148994-149042, 2021.


## **Radar Depth and Velocity Estimation**
- Radar can measure range and Doppler velocity, but both of them **cannot be directly used** for downstream tasks
- The range measurements are sparse and therefore difficult to associate with their visual correspondences
- The Doppler velocity is measured in the radial axis, therefore, cannot be directly used for tracking
<!-- - The depth completion and velocity estimation methods for radar point clouds are summarised below
  - **To be continued...** -->



## **Challenges**
- Although deep radar perception shows good performance on datasets, there are few studies investigating the generalisation of these methods
- In fact, some challenging situations are overlooked, but may prohibit the use of these methods in real-world scenarios
- Summarise **3 challenges** for deep radar perception
  - the **ghost objects** caused by multi-path propagation are common in complex scenarios but rarely discussed
  - **over-confidence** is a general problem with neural networks
  - even though we always refer to radar as an all-weather sensor, **robustness in adverse weather** is not well tested in many radar fusion methods
- Firstly, **multi-path effects** need to be explicitly considered in object detection
- Secondly, need to alleviate the problem of **over-confidence** in radar classification and **estimate** the **uncertainty** in bounding box regression
- Thirdly, the fusion architecture should have adaptive mechanisms to take full advantage of radar’s **all-weather capabilities**



## **Research Directions**
- Many research efforts have focused on developing models for detection tasks
- There are also some unexplored research topics or fundamental questions to be addressed
  - urgent need for **High-Quality Datasets**
  - **Radar Domain Knowledge** and **Uncertainty Quantification** can help developing a generalizable AI model
  - **Interference Mitigation**
  - **Motion Forecasting**
- Consider the perceptual system as a whole can **extend** the end-to-end learning **framework** forward or backward
  - **forward**, i.e. joint learning with **interference mitigation**
  - **backward**, i.e. **motion prediction**




## **Appendix**
### **Radar Signal Processing Fundamentals**
- Different radar devices vary in their sensing capabilities
- It is important to leverage radar domain knowledge 
  - to understand the **performance boundary** 
  - to find **key scenarios** 
  - to solve **critical problems** 
- classical signal processing pipeline for automotive radar applications


### **FMCW Radar Signal Processing**
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


### **Radar Performances**
- The performance of automotive radar (in general, can be evaluated in terms of )
  - maximum **range**
  - maximum **Doppler velocity**
  - **FoV**, Field of View
- The theoretical **maximum detection range** is $\: R_{max} = \sqrt[4]{\frac{\; P_t \: G^2 \: \lambda^2 \: \sigma \;}{\; (4 \pi )^3 \: P_{min} \;\;} }$ where 
  - $P_t$ is the transmit power
  - $P_{min}$ is the minimum detectable signal or receiver sensitivity
  - $\lambda$ is the transmit wavelength
  - $\sigma$ is the target Radar Cross Section (RCS)
  - $G$ is the antenna gain
- Parameter explainations
  - the wavelength $\lambda$ is **3.9 mm** for automotive **77 GHz** radar
  - the target RCS $\sigma$
    - is a measure of the **ability to reflect radar signals** back to the radar receiver
    - is a **statistical quantity** that varies with the viewing angle and the target material
    - for **small**er objects such as **pedestrians** and **bikes** have an average RCS value of around $2$ **~** $3 \; dBsm$
    - for **normal vehicles** it's around $10 \; dBsm$
    - for **large vehicles** it's around $20 \; dBsm$
  - the other parameters, such as transmit power, minimum detectable signal, and antenna gain are design parameters aimed at meeting product requirements and regulations
- Table 2. Equations for radar performance
    | Definition | Equation |
    | ---------- | -------- |
    | Max Unambiguous Range | $R_m = \frac{ \; \; c \: \cdot \: B_{IF} \; \; }{2S}$ |
    | Max Unambiguous Velocity | $v_m = \frac{ \; \; \lambda \; \; }{4 T_{c}}$ |
    | Max Unambiguous Angle | $\theta_{FoV} = \pm \ arcsin(\frac{ \; \; \lambda \; \; }{2d})$ |
    | Range Resolution | $\Delta R = \frac{ \; \; c \; \; }{2B}$ |
    | Velocity Resolution | $\Delta v = \frac{ \; \; \lambda \; \; }{ \; 2N_c \: \cdot \: N_T \; }$ |
    | Angular Resolution | $\Delta \theta_{res} = \frac{ \; \; \lambda \; \; }{ \; N_R  \: \cdot \: d \: \cdot \: cos(\theta) \; }$ |
    | 3 dB Beamwidth | $\Delta \theta_{3dB} = 2 \: arcsin (\frac{ \; \; 1.4 \lambda \; \; }{\pi \: \cdot \: D})$ |
  - the **maximum range** $R_m$ is limited by the supported IF bandwidth $B_{IF}$ and ADC sampling frequency (in practice)
  - the **maximum unambiguous velocity** $v_m$ is inversely proportional to the chirp duration $T_c$ 
  - for MIMO radar, the **maximum unambiguous angle** $\theta_{FoV}$ is dependent on the spacing of antennas $d$ 
  - the **FoV** is determined by the antenna gain pattern (in practice)
  - the **resolution** is the ability to separate two close targets w.r.t range, velocity, and angle
    - higher range resolution requires larger sweep bandwidth $B$
    - higher Doppler resolution requires longer integration time aka longer frame time $N_c \cdot T_c$
    - angular resolution depends on **3** things, the number of virtual receivers $N_R$, the object angle $\theta$, and the inter-antenna spacing $d$
- Table 3. Typical automotive radar parameters
    | Parameter | Range |
    | --------- | ----- |
    | Transit power |  $10$ ~ $13$ $(dBm)$
    | TX / RX antenna gain |  $10$ ~ $25$ $(dBi)$
    | Receiver noise figure |  $10$ ~ $20$ $(dB)$
    | Target Radar Cross Section (RCS) |  $-10$ ~ $20$ $(dBsm)$
    | Receiver sensitivity |  $-120$ ~ $-115$ $(dBm)$
    | Minimum SNR | $10$ ~ $20$ $(dB)$ |
- In practice, different types of automotive radar are designed for different scenarios
  - LRR, **Long-Range Radar** achieves a long detection range and a high angular resolution at the cost of a smaller FoV
  - SRR, **Short-Range Radar** uses MIMO techniques to achieve a high angular resolution and large FoV
- In addition, different **chirp configurations** are used for different applications. For example, 
  - LRR needs to detect fast-moving vehicles at distances (therefore, utilises)
    - a small ramp slope for long-distance detection
    - a long chirp integration time (frame time) to increase SNR
    - a small chirp duration to increase maximum velocity 
    - a short chirp duration for high-velocity resolution
  - SRR needs to detect vulnerable road users (VRUs) close to the vehicle (therefore, utilises)
    - a higher sweep bandwidth $B$ for high-range resolution (at the cost of a short range)
  - J. Hasch, E. Topak, R. Schnabel, T. Zwick, R. Weigel and C. Waldschmidt, "[Millimeter-Wave Technology for Automotive Radar Sensors in the 77 GHz Frequency Band](https://ieeexplore.ieee.org/document/6127923)," in *IEEE Transactions on Microwave Theory and Techniques*, vol. 60, no. 3, pp. 845-860, March 2012.
- **Multi-mode radar** can work in different modes simultaneously by sending chirps that are switched sequentially with different configurations






### **Data Labelling**
- Labelling radar data is a difficult task because both radar point clouds and pre-CFAR data are hard to interpret by human labellers
- To reduce labelling efforts, most datasets adopt a semi-automatic labelling framework, which includes **2** steps:
  - cross-modality pre-labelling 
  - fine-tuning
- In the first step, a well-trained detector on other modalities is leveraged for radar labelling
- In the second step, manual inspection is required to correct pre-labelling errors


### **Data Augmentation**
- Data augmentation plays an essential role in improving the generalization of deep learning models
- Data augmentation techniques can significantly improve the performance of **RA-map**-based radar detection
  - according to the summary report of the Radar Object Detection 2021 (ROD2021) Challenge
    - Wang, Yizhou, et al. "[ROD2021 Challenge: A Summary for Radar Object Detection Challenge for Autonomous Driving Applications](https://dl.acm.org/doi/10.1145/3460426.3463658)." *Proceedings of the 2021 International Conference on Multimedia Retrieval*. 2021.
- Base on the **radar representation** / data structure, the augmentation techniques can be divided into **2** types
  - **spectral**-based for pre-CFAR data
  - **pointcloud**-based for pointcloud
- It can also be featured as **local** or **global** depending on whether the entity being augmented is a **single object** or the **entire scene**
- **DANet** 
  - **spectral** augmentations
    - take **RA maps** as input
  - **global** augmentations
    - adopts several methods borrowed from Computer Vision
  - provide **5** methods
    - mirroring 
    - resizing 
    - random combination 
    - adding Gaussian noise 
    - temporal reversing
  - physical fidelity is not explicitly considered
  - Ju, B.; Yang, W.; Jia, J.; Ye, X.; Chen, Q.; Tan, X.; Sun, H.; Shi, Y.; Ding, E. "[DANet: Dimension Apart Network for Radar Object Detection](https://dl.acm.org/doi/abs/10.1145/3460426.3463656)." In *Proceedings of the 2021 International Conference on Multimedia Retrieval (ICMR)*, Taipei, Taiwan, 16–19 November 2021; pp. 533–539.
- **RADIO**
  - provide **4** types of **spectral** augmentations
  - **local** augmentations
    - **attenuation** by dampening the cells according to an empirical relationship between the received power and range
    - **resolution change** by nearest-neighbour interpolation according to the object size
  - **global** augmentations
    - adding **speckle noise**, the noise can an be approximated as a multiplicative truncated exponential distribution or multiplicative Gaussian noise
      - J. Ding, B. Chen, H. Liu and M. Huang, "[Convolutional Neural Network With Data Augmentation for SAR Target Recognition](https://ieeexplore.ieee.org/document/7393462)," in *IEEE Geoscience and Remote Sensing Letters*, vol. 13, no. 3, pp. 364-368, March 2016.
    - **background shift** by adding or subtracting a constant value to background cells
  - Sheeny, Marcel, Andrew Wallace, and Sen Wang. "[Radio: Parameterized generative radar data augmentation for small datasets](https://www.mdpi.com/2076-3417/10/11/3861)." *Applied Sciences* 10.11 (2020): 3861.
- **RAMP-CNN** 
  - **global** geometric augmentations 
    - also take **RA maps** as input
  - **geometric** method 
    - first translates and rotates RA maps in Cartesian coordinate 
    - then projects back to the original polar coordinate
    - the out-of-boundaries areas are cropped off
    - the blank areas are filled with background noises
    - **NOTE**. energy loss and antenna gain loss due to the transformation are compensated according to the radar equation (in order to meet the physical fidelity)
- **Point cloud augmentation** 
  - aims to introduce invariance to **geometric** transformations
  - improve the signal-to-clutter ratio
  - can be easily extended to multiple modalities by properly handling occlusion issues
    - Wang, Chunwei, et al. "[Pointaugmenting: Cross-modal augmentation for 3d object detection](https://openaccess.thecvf.com/content/CVPR2021/papers/Wang_PointAugmenting_Cross-Modal_Augmentation_for_3D_Object_Detection_CVPR_2021_paper.pdf)." *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*. 2021.
    - Zhang, Wenwei, Zhe Wang, and Chen Change Loy. "[Exploring data augmentation for multi-modality 3D object detection](https://arxiv.org/pdf/2012.12741.pdf)." *arXiv preprint arXiv:2012.12741* (2020).
  - many works utilise augmentation to increase the point cloud density to handle the **sparsity issue**
- **Geometric** augmentation
  - can be applied locally to a single target
  - or globally to the entire scene
  ![](https://i.imgur.com/Z2znScp.png)
- **Copy–paste** augmentation
  - copy the detected object from other frames and pastes it into the same location in the current frame
- **NOTE**. a limitation of these two methods is that they do not change the distribution of detections, while radar points are actually randomly distributed over the object in different frames







### **CFAR**
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


### **Clustering**
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


### **Classification**
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



### **Point Cloud Dector**
- End-to-end object detectors are expected to replace the conventional pipelines based on hand-crafted features
- Most radar detection methods only apply to moving targets, since static objects are difficult to classify due to low angular resolution
<!-- - **To be continued...** -->



### **Pre-CFAR Detector**
- Pre-CFAR data encode rich information of both targets and backgrounds, but this is hard to interpret by humans
  - DL-based CFAR estimation
    - Y. Cheng, J. Su, H. Chen and Y. Liu, "[A New Automotive Radar 4D Point Clouds Detector by Using Deep Learning](https://ieeexplore.ieee.org/document/9413682)," *ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2021, pp. 8398-8402.
  - DL-based DOA estimation
    - M. Gall, M. Gardill, T. Horn and J. Fuchs, "[Spectrum-based Single-Snapshot Super-Resolution Direction-of-Arrival Estimation using Deep Learning](https://ieeexplore.ieee.org/document/9080185)," *2020 German Microwave Conference (GeMiC)*, 2020, pp. 184-187.
    - J. Fuchs, M. Gardill, M. Lübke, A. Dubey and F. Lurz, "[A Machine Learning Perspective on Automotive Radar Direction of Arrival Estimation](https://ieeexplore.ieee.org/document/9674901)," in *IEEE Access*, vol. 10, pp. 6775-6797, 2022.
    - C. Grimm, T. Fei, E. Warsitz, R. Farhoud, T. Breddermann and R. Haeb-Umbach, "[Warping of Radar Data Into Camera Image for Cross-Modal Supervision in Automotive Applications](https://ieeexplore.ieee.org/abstract/document/9797876)," in *IEEE Transactions on Vehicular Technology*, 2022.
<!-- - A -->



### **Sensor Fusion for Detection**
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



### **Input Fusion**
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


### **ROI Fusion**
- ROI fusion is adapted from the classical "Fast R-CNN" two-stage detection framework
  - Girshick, Ross. "[Fast r-cnn](https://openaccess.thecvf.com/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf)." *In Proceedings of the IEEE International Conference on Computer Vision (ICCV)*, Santiago, Chile, 7–13 December 2015; pp. 1440–1448.
- Regions Of Interest (**ROI**s) can be considered as **a set of object candidates** without category information
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


### **Feature Map Fusion**
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


### **Decision Fusion**
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






