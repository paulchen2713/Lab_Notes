# meeting 09/14
**Advisor: Dr. Chih-Yu Wang**
**Presenter: Shao-Heng Chen**
**Date: September 14, 2022**
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
  ![](https://i.imgur.com/4D38d1M.png)
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
    - parametric variational autoencoder-based human target detection and localization framework
  - pre-CFAR
    - M. Meyer, G. Kuschk and S. Tomforde, "[Graph Convolutional Networks for 3D Object Detection on Radar Data](https://ieeexplore.ieee.org/document/9607427)," *2021 IEEE/CVF International Conference on Computer Vision Workshops (ICCVW)*, 2021, pp. 3053-3062.
    - B. Major et al., "[Vehicle Detection With Automotive Radar Using Deep Learning on Range-Azimuth-Doppler Tensors](https://ieeexplore.ieee.org/document/9022248)," *2019 IEEE/CVF International Conference on Computer Vision Workshop (ICCVW)*, 2019, pp. 924-932.

