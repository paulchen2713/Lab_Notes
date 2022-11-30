# **meeting 09/22**
**Advisor: Dr. Chih-Yu Wang**
**Presenter: Shao-Heng Chen**
**Date: September 22, 2022**
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
## **CARRADA Dataset**
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
## **Outdoor Moving Object Dataset**
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
## **Discussion**
- 跟鍾老師討論多個理想反射點的雷達模擬假設合理性的結果
  - 結論是鍾老師覺得這樣假設沒問題，只是還有很多細節需要釐清
  - 假設成人的雷達回波是由 3 個理想反射點去模擬；汽車的回波是由 10 個理想反射點去模擬(這裡是先武斷假設點數)
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

