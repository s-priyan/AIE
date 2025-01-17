### T.Luheerathan(170351P)

```
	- Checked for the posture dataset
        - TUM kitchen dataset 
        - UW-IOM dataset
        - NTU RGB+D and NTU RGB+D 120
        - MOPED25 dataset
        - Kinectics dataset
        - THUMOS dataset
 	- Verified no algorithm uses temporal analysis and prolonging static posture concept
 		- [1] uses lstm to smooth the REBA score calculated over frames.
 	- Proposed another apporach for posture assessment(NEED TO BE DISSCUSSED)
 		- Use the RULA/REBA along with angles
 		- [2],[3] uses RULA to assess the PC user
 		- To calculate RULA from 3D skeleton, Idea from [4] can be used.
 		
[1] B. Parsa and A. G. Banerjee, "A Multi-Task Learning Approach for Human Activity Segmentation and Ergonomics Risk Assessment," 2021 IEEE Winter Conference on Applications of Computer Vision (WACV), 2021, pp. 2351-2361, doi: 10.1109/WACV48630.2021.00240
[2] Menendez C, Amick B, Jenkins M, Janowitz I, Rempel D, Robertson M, Dennerlein J, Chang C and Katz JN. (2007). A multi-method study evaluating computing-related risk factors among college students. Work, 28. 287-297
[3]  Tullar J, Amick B, Robertson M, Fossel A, Coley C, Hupert N, Jenkins M and Katz JN. (2007). Direct observation of computer workplace risk factors of college students. Work, 28. 77-83
[4] Li, L. & Xu, X. “A deep learning-based RULA method for working posture assessment”. Proceedings of the Human Factors and Ergonomics Society Annual Meeting. Vol. 63. 1. SAGE Publications Sage CA: Los Angeles, CA. 2019, pp. 1090–1094
```

### C.Shobanapriyan(170581U)

```
- refer the "Towards 3D Human Pose Estimation in the Wild: a Weakly-supervised Approach" research paper and understand their approch and validate the possiblity of using that model [4]
	
- refer some article that validate , posture is a reasonable factor to detect the stress level [1],[2],[3]

[1]Stress detection in daily life scenarios using smart phones and wearable sensors: A survey (125 citations)
[2]Do slumped and upright postures affect stress responses? A randomized trial (158 citations)
[3]Towards an automatic early stress recognition system for office environments based on multimodal measurements: A review (278 citations)
[4]Towards 3D Human Pose Estimation in the Wild: a Weakly-supervised Approach Xingyi Zhou, Qixing Huang , Xiao Sun, Xiangyang Xue , Yichen Wei (401 citations)	
```

### S.Sivaluxan (170596U)

```	
    - tested and checked other rPPG algorithms for extracting heart rate related features
        - STVEN-rPPGNet: Remote Heart Rate Measurement from Highly Compressed Facial Videos: an End-to-end Deep Learning Solution with Video Enhancement (ICCV2019)
            - https://github.com/ZitongYu/STVEN_rPPGNet
            *need to add dataloader,data preprocessing and post preprocessing manually
            *need to be checked
        
        - rPPG-POS
            - https://github.com/pavisj/rppg-pos
            - inference very well and need less time for inference
            - implementation of rPPG based on POS(plane orthogonal to skin)
            *not offficail implementation but implementation based on [1]
    
    [1] "Algorithmic Principles of Remote PPG," W. Wang, A. C. den Brinker, S. Stuijk and G. de Haan, 2017
        - citation: 327
        
	
```
### S.Sooriyakumar (170599G)

```
	1. MAHNO HCI - a dataset for HR validation [1]
        > Have to refer further in it
        * We can finalize our heart rate estimation algorithm using this dataset
    2. Stress Detection in Working People [2]
        > Citations : 67
        * Official paper : ICACC - 2017
        - Study about how they use the Swell-KW dataset for stress classification
        - other Swell-KW dataset used papers have lower citations (2,3)
    3. Sitting Posture Recognition Based on OpenPose [3]
        > Citations : 3
        * Official conference : IOP - 2019
        - From this got third idea for posture assessment
            ##### Build a CNN to classify bad or good posture from the images of 2D-skeleton drawn (Tree of keypoints)
    References :
        [1] https://mahnob-db.eu/hci-tagging/view_collection/hr-estimation-v1
        [2] https://www.sciencedirect.com/science/article/pii/S187705091731904X
        [3] https://www.researchgate.net/publication/337871505_Sitting_Posture_Recognition_Based_on_OpenPose
```