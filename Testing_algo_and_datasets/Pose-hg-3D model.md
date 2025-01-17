

# Pose-hg-3d: Towards 3D Human Pose Estimation in the Wild: a Weakly-supervised Approach(ICCV 2017)

## Table of Contents
- [Paper-review](#Paper-review)
- [Results](#Results)
- [Scaling and rescaling](#Scalingandrescaling)
- [key points order](#keypointsorder)
- [used evaluation matrixes and results](#usedevaluationmatrixesandresults)
- [similar algorithms](#similaralgorithms)
- [Official implementation](#Officialimplementation)

## Paper-review
Proposed a weakly supervised transfer learning that used both that used both 2D and 3D labels images. The model augments a state-of-the-art 2D pose estimation sub-network with a 3D depth regression sub​network. Train as end-to-end and fully exploits the correlation between the 2D pose and depth estimation​ sub-tasks. Define a loss function for estimate the loss in Depth regression module for 2D label images called ​ **3D geometric constraint induced loss**.

Train their network In 3 stages.​

**Stage 1:** initializes the 2D pose module using 2D annotated images​
**Stage 2:** initializes the 3D pose estimation module and fine-tunes the 2D pose estimation module​ (used 3D dataset)
**Stage 3:** fine-tunes the whole network with all data (used 2D and 3D dataset). The geometric constraint is activated.​

![schematic illustration of the method](https://github.com/xingyizhou/pytorch-pose-hg-3d/blob/master/teaser.png?raw=true)





\
\
\
\
\
![model architecture](https://d3i71xaburhd42.cloudfront.net/aef930ab8368d5dc30fd18463700b11b4f4cdbc3/3-Figure2-1.png)


##  Scaling and rescaling

The scaling observed from the implemented model gives the scaled version of the actual 3d key points. modified the code and get the actual scale 3D constructed key points. That have mm scaling of all X,Y and Z (depth) coordinates. That scaling is same scale of Human3.6M dataset.

## key points order

the standard key points order of 3d constructed image should be like below.
![3D key points order](https://www.kdnuggets.com/wp-content/uploads/3d-keypoints-human-pose-estimation-0.png)

model give the key points in the following order

[3, 2, 1, 4, 5, 6, 0, 7, 8, 10, 16, 15, 14, 11, 12, 13]

## used evaluation matrixes and results

They MPJPE as evaluation matrix on Human3.6M dataset.

observed results are showed below.

![Evaluation matrixes](https://d3i71xaburhd42.cloudfront.net/aef930ab8368d5dc30fd18463700b11b4f4cdbc3/6-Table1-1.png)

## similar algorithms

There are many other algorithms developed for 3d pose estimation based on 2 ways.
1.monocular based 
2.mutiview based 

https://paperswithcode.com/sota/3d-human-pose-estimation-on-human36m

## Official implementation

https://github.com/xingyizhou/pytorch-pose-hg-3d
