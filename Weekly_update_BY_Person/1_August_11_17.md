### T.Luheerathan(170351P)

```
	- Testing some 3D skeleton reconstruction algorithm 
		- Videopose3D
			- Can't use no human3.6m dataset
		- VNect
			- not open code and no weights
		- XNect
			- Similar to Vnect
	- Checked the method of angle calculation in SWELL-KW dataset(Referred KW paper)
		- SWELL-KW psoture data extracted from kinect cam
		- Kinect cam placed towards person face 
		- Y-axis is upwards, X-axis is right handside, Z-axis front to back, origin is in 			Hip-center.
		- Spine	ShoulderCenter	Head	ShoulderLeft	ShoulderRight	ElbowLeft				  WristLeft	HandLeft	ElbowRight	WristRight	HandRight	HipCenter	HipLeft			  HipRight	KneeLeft	AnkleLeft	FootLeft	KneeRight	AnkleRight	FootRight
          should be extracted.
         - 2 set of angles are calculated;(1) Angles between bones (2) angles between 			   bone and to axis(X or Y or Z).
         -ANGLE CALCULATION NODE NEEDS TO BE IMPLEMENTED    
```

### C.Shobanapriyan(170581U)

```
	- Tested Facial expression action unit algorithm and the model selection 
		- detect faces
		- extract emotional facial expressions (e.g., happiness,sadness, anger)
		-  facial muscle movements (e.g., action units)
		- facial landmarks, from videos and images of faces
		-  preprocess, analyze, and visualize output
		- Tested 3D skeleton reconstrcution algorithm
	-selected models 
	     -Face detection model- [RetinaFace](https://github.com/deepinsight/insightface/)
	     -Facial landmark detection model - [MobileNet](https://github.com/cunjian/pytorch_face_landmark)
	     -Action Unit detection model - [JAANet: Joint AU Detection and Face Alignment via Adaptive Attention](https://github.com/ZhiwenShao/PyTorch-JAANet)
	     -Emotion detection model - [ResMaskNet: Residual Masking Network](https://github.com/phamquiluan/ResidualMaskingNetwork)

	- Tested some 3D skeleton reconstruction algorithm
		 - run and evaluate "Semantic Graph Convolutional Networks for 3D Human Pose Regression" (CVPR 2019) model
			 *unsloved issue with inferencing custom dataset
		 - run and evaluate "Towards 3D Human Pose Estimation in the Wild: a Weakly-supervised Approach" ICCV 2017 model
			 *able to inferece for custom dataset

[1]RetinaFace: Single-Shot Multi-Level Face Localisation in the Wild Jiankang Deng, Jia Guo, Evangelos Ververas, Irene Kotsia, Stefanos Zafeiriou_; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2020 ( 80 citations)
[2]PFLD: A Practical Facial Landmark Detector Xiaojie Guo1 , Siyuan Li1 , Jinke Yu1 , Jiawan Zhang1 , Jiayi Ma2 , Lin Ma3 , Wei Liu3 , and Haibin Ling4 1Tianjin University 2Wuhan University 3Tencent AI Lab 4Temple University
[3]JAA-Net: Joint Facial Action Unit Detection and Face Alignment via Adaptive Attention Zhiwen Shao Zhilei Liu Jianfei Cai Lizhuang Ma
[4]Facial Expression Recognition using Residual Masking Network Luan, Pham and Huynh, Vu and Tuan Anh, Tran
```

### S.Sivaluxan (170596U)

```
    - tested rPPG algorithms  for extracting heart rate related features for stress assessment
        - Meta-rPPG: Remote Heart Rate Estimation Using a Transductive Meta-Learner(ECCV2020)
            - https://github.com/eugenelet/Meta-rPPG
            *only training available
            - official git repo
        - Deep-rPPG: Camera-based pulse estimation using deep learning tools
            - https://github.com/terbed/Deep-rPPG
            *need arguments for training and inference
        - nazir6/rPPG:
            - https://github.com/nasir6/rPPG
            - real time inference is available
            *took more time for inference
            *official implementation is mot available

```
##### S.Sooriyakumar (170599G)

```	
    - Tested some 3D detection algorithms
        1. Lifting From the Deep: Convolutional 3D Pose Estimation From a Single Image [1]
            > Citations : 400
            * Official conference : CVPR-2017
            * Framework : Tensorflow
            * Inference in local
            * Issues in custom dataset - detection of a single person is correct but skeleton is not right
        2. (3DMPPE_Posenet) Camera Distance-aware Top-down Approach for 3D Multi-person Pose Estimation from a Single RGB Image [2]
            > Citations : 106
            * Official conference : ICCV-2019
            * Framework : Pytorch
            * Inference in local
            * Issues in custom dataset - 5 unrelated skeletons are detected for a single person image 
        3. LCR-Netv2 [3]
            > Citations : 212
            * Official conference : CVPR-2017, PAMI-2019
            * Framework : Pytorch
            * Not inference in local - Issue in installing Detectron1 framework
        4. CannonPose [4]
            > Citations : 9
            * Official conference : CVPR-2021
            * Framework : Pytorch
            * Issue : Training is only available in official github repo, Training in local also takes > 2 hours   
        5. 3d-pose-baseline [5]
            > Citations : 661
            * Official conference : ICCV-2017
            * Framework : Tensorflow 1.0
            * Not inference in local - Issue in running python code 

    - Tested some rPPG algorithms for Heart Rate estimation
        1. Spectral Reflectance-based Heart Rate Estimation from Facial Video [6]
            > Citations : 2
            * Official conference : ICIP-2019
            * Method : Eye & Face Haarcascade features extracting computer vision technique
            * Issue : Crominance will be calculated but from that how to estimate heart rate ?
        2. rPPG-pos [7] 
        > ##### Not an official implementation
            > Citations : 329
            * Official paper : IEEE Transactions on Biomedical Engineering
            * Framework : uses dlib library for 68-landmarks on face using a dat file
            * Inferenced well
        3. Other tested algorithms are unofficial and issues 

    References:
    [1] https://github.com/DenisTome/Lifting-from-the-Deep-release
    [2] https://github.com/mks0601/3DMPPE_POSENET_RELEASE
    [3] https://thoth.inrialpes.fr/src/LCR-Net/
    [4] https://github.com/bastianwandt/CanonPose
    [5] https://github.com/una-dinosauria/3d-pose-baseline
    [6] https://arxiv.org/abs/1901.00273
    [7] https://github.com/pavisj/rppg-pos/
```