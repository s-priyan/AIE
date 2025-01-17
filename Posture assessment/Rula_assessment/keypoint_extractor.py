# Copyright (c) OpenMMLab. All rights reserved.
import copy
from logging import critical
import os
import os.path as osp
from argparse import ArgumentParser

import cv2
import mmcv
import numpy as np
import matplotlib.pyplot as plt


from rula_assess import rula_assess
from time import time


from debugger import Debugger

from mmpose.apis import (extract_pose_sequence, get_track_id,
                         inference_pose_lifter_model,
                         inference_top_down_pose_model, init_pose_model,
                         process_mmdet_results, vis_3d_pose_result)

try:
    from mmdet.apis import inference_detector, init_detector

    has_mmdet = True
except (ImportError, ModuleNotFoundError):
    has_mmdet = False


def covert_keypoint_definition(keypoints, pose_det_dataset, pose_lift_dataset):
    """Convert pose det dataset keypoints definition to pose lifter dataset
    keypoints definition.

    Args:
        keypoints (ndarray[K, 2 or 3]): 2D keypoints to be transformed.
        pose_det_dataset, (str): Name of the dataset for 2D pose detector.
        pose_lift_dataset (str): Name of the dataset for pose lifter model.
    """
    if pose_det_dataset == 'TopDownH36MDataset' and \
            pose_lift_dataset == 'Body3DH36MDataset':
        return keypoints
    elif pose_det_dataset == 'TopDownCocoDataset' and \
            pose_lift_dataset == 'Body3DH36MDataset':
        keypoints_new = np.zeros((17, keypoints.shape[1]))
        # pelvis is in the middle of l_hip and r_hip
        keypoints_new[0] = (keypoints[11] + keypoints[12]) / 2
        # thorax is in the middle of l_shoulder and r_shoulder
        keypoints_new[8] = (keypoints[5] + keypoints[6]) / 2
        # head is in the middle of l_eye and r_eye
        keypoints_new[10] = (keypoints[1] + keypoints[2]) / 2
        # spine is in the middle of thorax and pelvis
        keypoints_new[7] = (keypoints_new[0] + keypoints_new[8]) / 2
        # rearrange other keypoints
        keypoints_new[[1, 2, 3, 4, 5, 6, 9, 11, 12, 13, 14, 15, 16]] = \
            keypoints[[12, 14, 16, 11, 13, 15, 0, 5, 7, 9, 6, 8, 10]]
        return keypoints_new
    else:
        raise NotImplementedError


def main():

    feedback_dict={1:0,2:0,3:0,4:0,5:0,6:0,7:0}
    count=0
    critical=[]
    

    #Object Detection
    #Scaled yolov4 or yolov4 with mobilenet backend can be used to reduce time further

    bbox_thr=0.8 #~500ms
    det_checkpoint='checkpoints/ssdlite_mobilenetv2_scratch_600e_coco_20210629_110627-974d9307.pth'
    det_config='configs/ssd/ssdlite_mobilenetv2_scratch_600e_coco.py'
    
    '''
    
    

    bbox_thr=0.8 #~500ms
    det_checkpoint='checkpoints/ssdlite_mobilenetv2_scratch_600e_coco_20210629_110627-974d9307.pth'
    det_config='configs/ssd/ssdlite_mobilenetv2_scratch_600e_coco.py'
    
    

    bbox_thr=0.5 #not working properly
    det_checkpoint='checkpoints/yolox_s_8x8_300e_coco_20211121_095711-4592a793.pth'
    det_config='configs/yolox/yolox_s_8x8_300e_coco.py'

    
    bbox_thr=0.5 #not working properly
    det_checkpoint='checkpoints/yolox_s_8x8_300e_coco_20211121_095711-4592a793.pth'
    det_config='configs/yolof/yolof_r50_c5_8x8_1x_coco.py'
    
    
    bbox_thr=0.5 #~400ms
    det_checkpoint='checkpoints/yolov3_mobilenetv2_mstrain-416_300e_coco_20210718_010823-f68a07b3.pth'
    det_config='configs/yolo/yolov3_mobilenetv2_mstrain-416_300e_coco.py'
    
    bbox_thr=0.9 #~1900ms
    det_checkpoint='checkpoints/faster_rcnn_r50_fpn_1x_coco-person_20201216_175929-d022e227.pth'
    det_config='configs/faster_rcnn/faster_rcnn_r50_caffe_fpn_mstrain_1x_coco-person.py'

    bbox_thr=0.9#~1900ms
    det_checkpoint='checkpoints/faster_rcnn_r50_fpn_fp16_1x_coco_20200204-d4dc1471.pth'
    det_config='configs/faster_rcnn/faster_rcnn_r50_fpn_fp16_1x_coco.py'
    '''

    #2D Estimation
    #


    #170ms
    pose_detector_checkpoint='checkpoints/hrnet_w32_coco_256x192_dark-07f147eb_20200812.pth'
    pose_detector_config='configs/body/2d_kpt_sview_rgb_img/topdown_heatmap/coco/hrnet_w32_coco_256x192_dark.py'
    
    

    '''
    #170ms
    pose_detector_checkpoint='checkpoints/hrnet_w32_coco_256x192_dark-07f147eb_20200812.pth'
    pose_detector_config='configs/body/2d_kpt_sview_rgb_img/topdown_heatmap/coco/hrnet_w32_coco_256x192_dark.py'
    

    #160ms
    pose_detector_checkpoint='checkpoints/hrnet_w32_coco_256x192-c78dce93_20200708.pth'
    pose_detector_config='configs/body/2d_kpt_sview_rgb_img/topdown_heatmap/coco/hrnet_w32_coco_256x192.py'

    #200ms
    pose_detector_checkpoint='checkpoints/litehrnet30_coco_256x192-4176555b_20210626.pth'
    pose_detector_config='configs/body/2d_kpt_sview_rgb_img/topdown_heatmap/coco/litehrnet_30_coco_256x192.py'

    #200ms 
    pose_detector_checkpoint='checkpoints/litehrnet30_coco_384x288-a3aef5c4_20210626.pth'
    pose_detector_config='configs/body/2d_kpt_sview_rgb_img/topdown_heatmap/coco/litehrnet_30_coco_384x288.py'

    #320ms
    pose_detector_checkpoint='checkpoints/hrnet_w48_coco_256x192-b9e0b3ab_20200708.pth'
    pose_detector_config='configs/body/2d_kpt_sview_rgb_img/topdown_heatmap/coco/hrnet_w48_coco_256x192.py'
    '''

    det_cat_id=1
    device='cuda:0'
    euro=False
    kpt_thr=0.3
    norm_pose_2d=False
    num_instances=-1
    out_video_root='vis_results'
    pose_lifter_checkpoint='checkpoints/videopose_h36m_243frames_fullconv_supervised_cpn_ft-88f5abbb_20210527.pth'
    pose_lifter_config='configs/body/3d_kpt_sview_rgb_vid/video_pose_lift/h36m/videopose3d_h36m_243frames_fullconv_supervised_cpn_ft.py'
    radius=8
    rebase_keypoint_height=True
    show=True
    thickness=2
    tracking_thr=0.3
    use_oks_tracking=False
    video_path='resources/test.mp4'


    video = mmcv.VideoReader(video_path)
    assert video.opened, f'Failed to load video file {video_path}'

  
    
    # First stage: 2D pose detection
    print('Stage 1: 2D pose detection.')

    person_det_model = init_detector(
        det_config, det_checkpoint, device=device.lower())

    pose_det_model = init_pose_model(
        pose_detector_config,
        pose_detector_checkpoint,
        device=device.lower())

    assert pose_det_model.cfg.model.type == 'TopDown', 'Only "TopDown"' \
        'model is supported for the 1st stage (2D pose detection)'

    pose_det_dataset = pose_det_model.cfg.data['test']['type']

    pose_det_results_list = []
    next_id = 0
    pose_det_results = []
    for frame in video:
        pose_det_results_last = pose_det_results

        start_time=time()*1000
        # test a single image, the resulting box is (x1, y1, x2, y2)
        mmdet_results = inference_detector(person_det_model, frame)
        person_det_model.show_result(frame, mmdet_results,out_file='result.jpg')


        obj_det_time=time()*1000-start_time
        print("Object detection time",obj_det_time)


        # keep the person class bounding boxes.
        person_det_results = process_mmdet_results(mmdet_results,det_cat_id)
        #print("Person det result is ",person_det_results)


        person_det_time=time()*1000-obj_det_time-start_time
        print("Person detection time",person_det_time)

        
        # make person results for single image
        pose_det_results, _ = inference_top_down_pose_model(
            pose_det_model,
            frame,
            person_det_results,
            bbox_thr=bbox_thr,
            format='xyxy',
            dataset=pose_det_dataset,
            return_heatmap=False,
            outputs=None)
        pose_det_time=time()*1000-start_time-person_det_time-obj_det_time 
        print("2D pose estimation time",pose_det_time)
        print("Pose det result is ",pose_det_results)
        print()

        # get track id for each person instance
        pose_det_results, next_id = get_track_id(
            pose_det_results,
            pose_det_results_last,
            next_id,
            use_oks=use_oks_tracking,
            tracking_thr=tracking_thr,
            use_one_euro=euro,
            fps=video.fps)

        pose_det_results_list.append(copy.deepcopy(pose_det_results))

  
  
  
    # Second stage: Pose lifting
    print('Stage 2: 2D-to-3D pose lifting.')

    pose_lift_model = init_pose_model(
        pose_lifter_config,
        pose_lifter_checkpoint,
        device=device.lower())

    assert pose_lift_model.cfg.model.type == 'PoseLifter', \
        'Only "PoseLifter" model is supported for the 2nd stage ' \
        '(2D-to-3D lifting)'
    pose_lift_dataset = pose_lift_model.cfg.data['test']['type']
    #print ("Pose lift dataset is",pose_lift_dataset)

    if out_video_root == '':
        save_out_video = False
    else:
        os.makedirs(out_video_root, exist_ok=True)
        save_out_video = True

    if save_out_video:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = video.fps
        writer = None

    # convert keypoint definition
    for pose_det_results in pose_det_results_list:
        for res in pose_det_results:
            keypoints = res['keypoints']
            res['keypoints'] = covert_keypoint_definition(
                keypoints, pose_det_dataset, pose_lift_dataset)

    # load temporal padding config from model.data_cfg
    if hasattr(pose_lift_model.cfg, 'test_data_cfg'):
        data_cfg = pose_lift_model.cfg.test_data_cfg
    else:
        data_cfg = pose_lift_model.cfg.data_cfg
    #print("Seq len is",pose_lift_model)

    num_instances = num_instances
    for i, pose_det_results in enumerate(mmcv.track_iter_progress(pose_det_results_list)):
        # extract and pad input pose2d sequence
        pose_results_2d = extract_pose_sequence(
            pose_det_results_list,
            frame_idx=i,
            causal=data_cfg.causal,
            seq_len=data_cfg.seq_len,
            step=data_cfg.seq_frame_interval)

        start_3d=time()*1000
        # 2D-to-3D pose lifting
        pose_lift_results = inference_pose_lifter_model(
            pose_lift_model,
            pose_results_2d=pose_results_2d,
            dataset=pose_lift_dataset,
            with_track_id=True,
            image_size=video.resolution,
            norm_pose_2d=norm_pose_2d)

        print("\n3D inference time",time()*1000-start_3d)
    

        #print("Lifted results",pose_lift_results)

        # Pose processing
        pose_lift_results_vis = []
        for idx, res in enumerate(pose_lift_results):
            keypoints_3d = res['keypoints_3d']
            # exchange y,z-axis, and then reverse the direction of x,z-axis
            keypoints_3d = keypoints_3d[..., [0, 2, 1]]
            keypoints_3d[..., 0] = -keypoints_3d[..., 0]
            keypoints_3d[..., 2] = -keypoints_3d[..., 2]
            # rebase height (z-axis)
            if rebase_keypoint_height:
                keypoints_3d[..., 2] -= np.min(
                    keypoints_3d[..., 2], axis=-1, keepdims=True)
            res['keypoints_3d'] = keypoints_3d
            rula_assess(keypoints_3d,feedback_dict)
            count+=1

            '''
            debugger = Debugger()
            debugger.add_point_3d(keypoints_3d, 'b')
            debugger.show_3d()
            '''
        print("\n")
            
    for i in range(len(feedback_dict)):
        if(feedback_dict[i+1]>=count*0.5):
            critical.append(i+1)
    for cr in critical:
        if (cr==1):
            print("Do not bend/twist your head too much.")
        elif (cr==2):
            print("Do not bend your trunk too much. Keep it in straight.")
        elif(cr==3):
            print("You are about to bend your head and trunk too much.")
        elif(cr==4):
            print("Keep left upper arm in a neutral comfortable position. Do not raise it more.")
        elif(cr==5):
            print("You are about to have your left hand in non-neutral position.")
        elif(cr==6):
            print("Keep right uppe1. Posture Assessment demo ​r arm in a neutral comfortable position. Do not raise it more.")
        elif(cr==7):
            print("You are about to have your right hand in non-neutral position.")
    
    plt.bar(range(len(feedback_dict)), list(feedback_dict.values()), align='center')
    plt.xticks(range(len(feedback_dict)), list(feedback_dict.keys()))
    plt.xlabel('Posture issues')
    plt.ylabel('Frequency')
    plt.title('Posture issues vs frequency')
    plt.show()
    #print("Feedback dict is ",feedback_dict)
    #print("Critical points are ",critical)
    print("Done")

            
if __name__ == '__main__':
    main()
