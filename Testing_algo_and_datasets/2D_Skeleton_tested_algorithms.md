## Other locally inferenced 2D-Skeleton algorithms 

1. Mediapipe - Pose {Google}
    * official site = https://google.github.io/mediapipe/solutions/pose.html
    * Web demo = https://codepen.io/mediapipe/pen/jOMbvxw
    * 33 - 3D landmarks
    * Output of Pose landmarks
        I. x and y: normalized to [0.0, 1.0] by the image width and height respectively.
       II. z
            * landmark depth with the depth at the midpoint of hips being the origin
            * smaller the value the closer the landmark is to the camera
            * magnitude of z uses roughly the same scale as x -*  ** ISSUE **
      III. visibility: A value in [0.0, 1.0] indicating the likelihood of the landmark being visible
2. OpenPose {CMU-Perceptional labs}
    * official site = https://github.com/CMU-Perceptual-Computing-Lab/openpose
    * 15, 18 or 25-keypoint body/foot keypoint estimation, including 6 foot keypoints
3. Posenet {tensorflow - Google Brain Team}
    * official site = https://github.com/tensorflow/tfjs-models/tree/master/posenet
4. Movenet {tensorflow - Google Brain Team}
    * official site = https://github.com/tensorflow/tfjs-models/tree/master/pose-detection/src/movenet
5. Mediapipe - Holistic {Google}
    * official site = https://google.github.io/mediapipe/solutions/holistic.html
    * Real time
        I. Human pose
       II. Face landmarks
      III. Hand tracking
    * Output of Pose landmarks
        I. x and y: normalized to [0.0, 1.0] by the image width and height respectively.
       II. z: Should be discarded as currently the model is not fully trained to predict depth
      III. visibility: A value in [0.0, 1.0] indicating the likelihood of the landmark being visible