#Based on A deep learning-based RULA method for working posture assessment
import cupy as cp
import numpy as np

def Rula_assess(joints):
    hip_1=joints[0]
    hip_r_2=joints[1]
    hip_l_5=joints[2]
    ankle_r_4=joints[3]
    ankle_l_7=joints[4]
    knee_r_3=joints[5]
    knee_l_6=joints[6]
    spine_8=joints[7]
    throax_9=joints[8]
    head_11=joints[9]
    shoulder_r_15=joints[10]
    shoulder_l_12=joints[11]
    elbow_r_16=joints[12]
    elbow_l_13=joints[13]
    wrist_r_17=joints[14]
    wrist_l_14=joints[15]
    nose_10=joints[16]

    coronal_normal_vect=np.cross(vector_m_to_n(hip_1,shoulder_l_12),vector_m_to_n(hip_1,shoulder_r_15))
    sagittal_normal_vect=np.cross(vector_m_to_n(hip_1,throax_9),hip_1+coronal_normal_vect)
    face_plane_normal_vect=np.cross(vector_m_to_n(nose_10,head_11),vector_m_to_n(nose_10,throax_9))
    
    #Right side upper arm flexion/extension
    bone_shoulder_r2throax_sag=projection_on_plane(sagittal_normal_vect,vector_m_to_n(shoulder_r_15,throax_9))
    bone_shoulder_r2elbow_r_sag=projection_on_plane(sagittal_normal_vect,vector_m_to_n(shoulder_r_15,elbow_r_16))
    upper_arm_flexion_r=angle_bet_vect(bone_shoulder_r2elbow_r_sag,bone_shoulder_r2throax_sag)

    #Left side upper arm flexion/extension
    bone_shoulder_l2throax_sag=projection_on_plane(sagittal_normal_vect,vector_m_to_n(shoulder_l_12,throax_9))
    bone_shoulder_l2elbow_l_sag=projection_on_plane(sagittal_normal_vect,vector_m_to_n(shoulder_l_12,elbow_l_13))
    upper_arm_flexion_l=angle_bet_vect(bone_shoulder_l2elbow_l_sag,bone_shoulder_l2throax_sag)

    #Right upper arm abduction
    bone_throax2shoulder_r_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(throax_9,shoulder_r_15))
    bone_shoulder_r2relbow_r_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(shoulder_r_15,elbow_r_16))
    upper_arm_abduction_r=90-angle_bet_vect(bone_throax2shoulder_r_cor,bone_shoulder_r2relbow_r_cor)#>0 means abducted

    #Left upper arm abduction
    bone_throax2shoulder_l_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(throax_9,shoulder_l_12))
    bone_shoulder_l2relbow_l_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(shoulder_l_12,elbow_l_13))
    upper_arm_abduction_r=90-angle_bet_vect(bone_throax2shoulder_r_cor,bone_shoulder_r2relbow_r_cor)#>0 means abducted

    #Right Raised shoulder
    bone_thorax2hip=vector_m_to_n(throax_9,hip_1)
    bone_throax2shoulder_r=vector_m_to_n(throax_9,shoulder_r_15)
    raised_shoulder_r=angle_bet_vect(bone_throax2shoulder_r,bone_thorax2hip)#>90 means raised

    #Left Raised shoulder
    bone_thorax2hip=vector_m_to_n(throax_9,hip_1)
    bone_throax2shoulder_l=vector_m_to_n(throax_9,shoulder_l_12)
    raised_shoulder_l=angle_bet_vect(bone_throax2shoulder_l,bone_thorax2hip) #>90 means raised

    #Leaning
    normal_z=np.array([0,0,1])#True only if z axis is against gravity
    bone_hip2throax=vector_m_to_n(hip_1,throax_9)
    leaning=angle_bet_vect(bone_hip2throax,normal_z)

    #Right lower arm flexion
    bone_throax2hip1_sag=projection_on_plane(sagittal_normal_vect,vector_m_to_n(throax_9,hip_1))
    bone_elbow_r2wrist_r=projection_on_plane(sagittal_normal_vect,vector_m_to_n(elbow_r_16,wrist_r_17))
    lower_arm_flexion_r=angle_bet_vect(bone_throax2hip1_sag,bone_elbow_r2wrist_r)

    #Left lower arm flexion
    bone_throax2hip1_sag=projection_on_plane(sagittal_normal_vect,vector_m_to_n(throax_9,hip_1))
    bone_elbow_l2wrist_l=projection_on_plane(sagittal_normal_vect,vector_m_to_n(elbow_l_13,wrist_l_14))
    lower_arm_flexion_l=angle_bet_vect(bone_throax2hip1_sag,bone_elbow_l2wrist_l)

    #Right Lower arm across mid line
    bone_throax2wrist_r_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(throax_9,wrist_r_17))
    bone_throax2shoulder_r_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(throax_9,shoulder_r_15))
    low_arm_across_mid_line=angle_bet_vect(bone_throax2shoulder_r_cor,bone_throax2wrist_r_cor) #>90 indiactes crossing

    #Left Lower arm across mid line
    bone_throax2wrist_l_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(throax_9,wrist_l_14))
    bone_throax2shoulder_l_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(throax_9,shoulder_l_12))
    low_arm_across_mid_line=angle_bet_vect(bone_throax2shoulder_l_cor,bone_throax2wrist_l_cor )#>90 indiactes crossing

    #Neck extension
    bone_throax2head_sag=projection_on_plane(sagittal_normal_vect,vector_m_to_n(throax_9,head_11))
    bone_throax2hip1_sag=projection_on_plane(sagittal_normal_vect,vector_m_to_n(throax_9,hip_1))
    neck_extension=angle_bet_vect(bone_throax2hip1_sag,bone_throax2head_sag)

    #Neck side bending
    bone_throax2head_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(throax_9,head_11))
    bone_throax2hip1_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(throax_9,hip_1))
    neck_bending=angle_bet_vect(bone_throax2head_cor,bone_thorax2hip) # <180 indicates neck side bending

    #Trunk flexion
    trunk_flexion=leaning

    #Trunk twisted
    bone_shoulder_r2shoulder_l=vector_m_to_n(shoulder_r_15,shoulder_l_12)
    bone_hip_r2hip_l=vector_m_to_n(hip_r_2,hip_l_5)
    trunk_twisted=angle_bet_vect(bone_shoulder_r2shoulder_l,bone_hip_r2hip_l)


    #Trunk side bending
    bone_hip2throax_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(hip_1,throax_9))
    bone_hip2hip_r_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(hip_1,hip_r_2))
    side_bending=angle_bet_vect(bone_hip2throax_cor,bone_hip2hip_r_cor) # >90 or <90 indicates side bending

    #Neck twisted
    neck_twisted=




def vector_m_to_n(joint_m,joint_n):
    return (joint_n-joint_m)


def projection_on_plane(plane_normal,vect_m_to_n):
    projection = vect_m_to_n-(np.dot(vect_m_to_n,plane_normal)/(np.linalg.norm(plane_normal)**2))*plane_normal
    return projection

def angle_bet_vect(vector_1,vector_2):
    unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
    unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = np.arccos(dot_product)
    return np.degrees(angle)

if __name__=='__main__':
    joints=np.arange(48).reshape(16,3)

    
