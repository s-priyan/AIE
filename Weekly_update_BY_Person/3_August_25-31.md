<<<<<<< HEAD
﻿### T.Luheerathan(170351P)

```
-Built a python script(Angle_error_3D_pose_est.ipynb and 			   	angle_calculation_for_3d_est.py) to find out error in angles, during the 3D reconstruction. more critical angle distributed as normal distribution and distribution was between 120 deg to 180 deg with the average of 160deg for the 3D reconstruction model[1] having MPJPE 65mm.

- Tested some other reconstruction models like Videopose3D,RIE having MPJPE error 44mm.
Unable to find a way to inference RIE. Videopose3D requires Detectron keypoints model to inference. Detectron2 converts human video frame sequence to 2D keypoints. Then videopose3D converts 2D keypoints to 3D human model. As detectron2 uses R-CNN required 2D detection process at 0.6 fps(not feasible in our case Jetson nano may not process video)

- Checked for 3D cameras intellisense,zed2(not in afforadble price and not available in sri lanka), kincet 3D(introduces some error 1cm -2cm in depth sensing)[2] 

-Checked for RULA posture assessment method whether it can be implemented from 2D(angle extraction from sagittal plane),3D can be used as qualitatively instead of quantitavely.
(further analysis needed on RULA)

-Checked for some 2D posture estimation(openpose). It also can't be implemented in Jetson nano.


```

### C.Shobanapriyan(170581U)

```
-paper reiview for 3d reconstruction and observation
_ sacling and rescaling the 3d skelton ouput of the exisiting model
-find out the standard key points order of 3d constraction and find the orrder of the key poits that derived form the exsisting algorithms.

-understand the evaluation mattrics(MPJPE)

-check the model complexity and inference complexity in jetson nano.



```

### S.Sivaluxan (170596U)

```	
	
```
### S.Sooriyakumar (170599G)

```

```
=======
﻿### T.Luheerathan(170351P)

```
-Built a python script(Angle_error_3D_pose_est.ipynb and 			   	angle_calculation_for_3d_est.py) to find out error in angles, during the 3D reconstruction. more critical angle distributed as normal distribution and distribution was between 120 deg to 180 deg with the average of 160deg for the 3D reconstruction model[1] having MPJPE 65mm.

- Tested some other reconstruction models like Videopose3D,RIE having MPJPE error 44mm.
Unable to find a way to inference RIE. Videopose3D requires Detectron keypoints model to inference. Detectron2 converts human video frame sequence to 2D keypoints. Then videopose3D converts 2D keypoints to 3D human model. As detectron2 uses R-CNN required 2D detection process at 0.6 fps(not feasible in our case Jetson nano may not process video)

- Checked for 3D cameras intellisense,zed2(not in afforadble price and not available in sri lanka), kincet 3D(introduces some error 1cm -2cm in depth sensing)[2] 

-Checked for RULA posture assessment method whether it can be implemented from 2D(angle extraction from sagittal plane),3D can be used as qualitatively instead of quantitavely.
(further analysis needed on RULA)

-Checked for some 2D posture estimation(openpose). It also can't be implemented in Jetson nano.


```

### C.Shobanapriyan(170581U)

```
-paper reiview for 3d reconstruction and observation
_ sacling and rescaling the 3d skelton ouput of the exisiting model
-find out the standard key points order of 3d constraction and find the orrder of the key poits that derived form the exsisting algorithms.

-understand the evaluation mattrics(MPJPE)

-check the model complexity and inference complexity in jetson nano.



```

### S.Sivaluxan (170596U)

```	
-paper review
    - The SWELL Knowledge Work Dataset for Stress and User Modeling Research [1] 
    - Using smart offices to predict occupational stress

-References
[1] Saskia Koldijk, Maya Sappelli, Suzan Verberne, Mark A. Neerincx, and Wessel Kraaij. 2014. The SWELL Knowledge Work Dataset for Stress and User Modeling Research. In Proceedings of the 16th International Conference on Multimodal Interaction (ICMI '14). ACM, New York, NY, USA, 291-298
[2] Alberdi, Ane and Aztiria, Asier and Basarab, Adrian and Cook, Diane J. Using Smart Offices to Predict Occupational Stress. (2018) International Journal of Industrial Ergonomics, 67. 13-26. ISSN 0169-8141

```
### S.Sooriyakumar (170599G)

```

```
>>>>>>> 509da148b0291ad3fcb467bb515ef5041ca399ef
