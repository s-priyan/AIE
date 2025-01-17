# Facial Expression Analysis And Action Units Extraction



- detect faces
- extract emotional facial expressions (e.g., happiness,     sadness, anger)
-  facial muscle movements (e.g., action units)
- facial landmarks, from videos and images of faces
-  preprocess, analyze, and visualize output


## Supported Models 


Face detection models
- [FaceBoxes](https://github.com/zisianw/FaceBoxes.PyTorch)
- [MTCNN](https://github.com/ipazc/mtcnn)
- [RetinaFace](https://github.com/deepinsight/insightface/)
- [img2pose](https://github.com/vitoralbiero/img2pose)

Facial landmark detection models
- [MobileNet](https://github.com/cunjian/pytorch_face_landmark)
- [MobileFaceNet](https://github.com/foamliu/MobileFaceNet)
- [PFLD: Practical Facial Landmark Detector](https://github.com/polarisZhao/PFLD-pytorch)

Action Unit detection models
- FEAT-Random Forest
- FEAT-SVM
- FEAT-Logistic
- [DRML: Deep Region and Multi-Label Learning](https://github.com/AlexHex7/DRML_pytorch)
- [JAANet: Joint AU Detection and Face Alignment via Adaptive Attention](https://github.com/ZhiwenShao/PyTorch-JAANet)

Emotion detection models 
- FEAT-Random Forest
- FEAT-Logistic
- [FerNet](https://www.kaggle.com/gauravsharma99/facial-emotion-recognition?select=fer2013)
- [ResMaskNet: Residual Masking Network](https://github.com/phamquiluan/ResidualMaskingNetwork)

Head pose estimation models
- [img2pose](https://github.com/vitoralbiero/img2pose)
- Perspective-n-Point algorithm to solve 3D head pose from 2D facial landmarks (via `cv2`)






