# **meeting 10/13**
Advisor: Dr. Chih-Yu Wang
Presenter: Shao-Heng Chen
Date: October 13, 2022


- Bounding box annotations in COCO format
  - JSON format
    ```json!
    {"image_id": int, "bbox": [x, y, width, height], "category_id": int}
    ```
    ```json!
    "000117": {"boxes": [[167, 11, 171, 18], [37, 28, 48, 32]], "labels": [3, 1]}
    ```
    <img src="https://i.imgur.com/QraWOKV.png"  width=60% height=60%>
    
    - ```(167, 11) and (37, 28)```
- code
![](https://i.imgur.com/5Yw2X1t.png)
![](https://i.imgur.com/N3yd6AA.png)
![](https://i.imgur.com/osTPZRS.png)
![](https://i.imgur.com/0UugH95.png)
- corresponded image
  - ```rd_matrix.shape = (256, 64)```
  - original matrix and the rotated one
  ![](https://i.imgur.com/pMCIjNA.png)
  
<!-- ![](https://i.imgur.com/4h4wPin.png) -->
<!-- ![](https://i.imgur.com/AWQqwf9.png) -->




