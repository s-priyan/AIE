#Based on A deep learning-based RULA method for working posture assessment
import numpy as np

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

def rula_assess(joints,feedback_list):
    hip_1=joints[0]
    hip_r_2=joints[1]
    hip_l_5=joints[4]
    ankle_r_4=joints[3]
    ankle_l_7=joints[6]
    knee_r_3=joints[2]
    knee_l_6=joints[5]
    spine_8=joints[7]
    throax_9=joints[8]
    head_11=joints[10]
    shoulder_r_15=joints[14]
    shoulder_l_12=joints[11]
    elbow_r_16=joints[15]
    elbow_l_13=joints[12]
    wrist_r_17=joints[16]
    wrist_l_14=joints[13]
    nose_10=joints[9]

    coronal_normal_vect=np.cross(vector_m_to_n(hip_1,shoulder_l_12),vector_m_to_n(hip_1,shoulder_r_15))
    #sagittal_normal_vect=np.cross(vector_m_to_n(hip_1,throax_9),hip_1+coronal_normal_vect)
    sagittal_normal_vect=np.cross(vector_m_to_n(spine_8,throax_9),vector_m_to_n(spine_8,hip_1))
    face_plane_normal_vect=np.cross(vector_m_to_n(nose_10,head_11),vector_m_to_n(nose_10,throax_9))
    transverse_normal_vect=np.cross(coronal_normal_vect,sagittal_normal_vect)
    
    #print("\nExtracted Angles")
    #Right side upper arm flexion/extension
    bone_shoulder_r2throax_sag=projection_on_plane(sagittal_normal_vect,vector_m_to_n(throax_9,hip_1))
    bone_shoulder_r2elbow_r_sag=projection_on_plane(sagittal_normal_vect,vector_m_to_n(shoulder_r_15,elbow_r_16))
    upper_arm_flexion_r=angle_bet_vect(bone_shoulder_r2elbow_r_sag,bone_shoulder_r2throax_sag)

    #print("upper_arm_flexion_r",upper_arm_flexion_r)

    #Left side upper arm flexion/extension
    bone_shoulder_l2throax_sag=projection_on_plane(sagittal_normal_vect,vector_m_to_n(throax_9,hip_1))
    bone_shoulder_l2elbow_l_sag=projection_on_plane(sagittal_normal_vect,vector_m_to_n(shoulder_l_12,elbow_l_13))
    upper_arm_flexion_l=angle_bet_vect(bone_shoulder_l2elbow_l_sag,bone_shoulder_l2throax_sag)

    #print("upper_arm_flexion_l",upper_arm_flexion_l)

    #Right upper arm abduction
    bone_throax2shoulder_r_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(throax_9,shoulder_r_15))
    bone_shoulder_r2relbow_r_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(shoulder_r_15,elbow_r_16))
    upper_arm_abduction_r=90-angle_bet_vect(bone_throax2shoulder_r_cor,bone_shoulder_r2relbow_r_cor)#>0 means abducted

    #print("upper_arm_abduction_r",upper_arm_abduction_r)

    #Left upper arm abduction
    bone_throax2shoulder_l_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(throax_9,shoulder_l_12))
    bone_shoulder_l2relbow_l_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(shoulder_l_12,elbow_l_13))
    upper_arm_abduction_l=90-angle_bet_vect(bone_throax2shoulder_l_cor,bone_shoulder_l2relbow_l_cor)#>0 means abducted

    #print("upper_arm_abduction_l",upper_arm_abduction_l)

    #Right Raised shoulder
    bone_thorax2hip=vector_m_to_n(throax_9,hip_1)
    bone_throax2shoulder_r=vector_m_to_n(throax_9,shoulder_r_15)
    raised_shoulder_r=angle_bet_vect(bone_throax2shoulder_r,bone_thorax2hip)#>90 means raised

    #print("raised_shoulder_r",raised_shoulder_r)

    #Left Raised shoulder
    bone_thorax2hip=vector_m_to_n(throax_9,hip_1)
    bone_throax2shoulder_l=vector_m_to_n(throax_9,shoulder_l_12)
    raised_shoulder_l=angle_bet_vect(bone_throax2shoulder_l,bone_thorax2hip) #>90 means raised
    #print("raised_shoulder_l",raised_shoulder_l)

    #Leaning
    normal_z=np.array([0,0,1])#True only if z axis is against gravity
    bone_hip2throax=vector_m_to_n(hip_1,throax_9)
    leaning=angle_bet_vect(bone_hip2throax,normal_z)

    #print("leaning",leaning)

    #Right lower arm flexion
    bone_throax2hip1_sag=projection_on_plane(sagittal_normal_vect,vector_m_to_n(throax_9,hip_1))
    bone_elbow_r2wrist_r=projection_on_plane(sagittal_normal_vect,vector_m_to_n(elbow_r_16,wrist_r_17))
    lower_arm_flexion_r=angle_bet_vect(bone_throax2hip1_sag,bone_elbow_r2wrist_r)

    #print("lower_arm_flexion_r",lower_arm_flexion_r)

    #Left lower arm flexion
    bone_throax2hip1_sag=projection_on_plane(sagittal_normal_vect,vector_m_to_n(throax_9,hip_1))
    bone_elbow_l2wrist_l=projection_on_plane(sagittal_normal_vect,vector_m_to_n(elbow_l_13,wrist_l_14))
    lower_arm_flexion_l=angle_bet_vect(bone_throax2hip1_sag,bone_elbow_l2wrist_l)

    #print("lower_arm_flexion_l",lower_arm_flexion_l)

    #Right Lower arm across mid line
    bone_throax2wrist_r_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(throax_9,wrist_r_17))
    bone_throax2shoulder_r_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(throax_9,shoulder_r_15))
    low_arm_r_across_mid_line=angle_bet_vect(bone_throax2shoulder_r_cor,bone_throax2wrist_r_cor) #>90 indiactes crossing

    #print("low_arm_r_across_mid_line",low_arm_r_across_mid_line)

    #Left Lower arm across mid line
    bone_throax2wrist_l_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(throax_9,wrist_l_14))
    bone_throax2shoulder_l_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(throax_9,shoulder_l_12))
    low_arm_l_across_mid_line=angle_bet_vect(bone_throax2shoulder_l_cor,bone_throax2wrist_l_cor )#>90 indiactes crossing

    #print("low_arm_l_across_mid_line",low_arm_l_across_mid_line)

    #Neck extension
    bone_throax2head_sag=projection_on_plane(sagittal_normal_vect,vector_m_to_n(throax_9,head_11))
    bone_throax2hip1_sag=projection_on_plane(sagittal_normal_vect,vector_m_to_n(throax_9,hip_1))
    neck_extension=180-angle_bet_vect(bone_throax2hip1_sag,bone_throax2head_sag)

    #print("neck_extension",neck_extension)
    

    #Neck side bending
    bone_throax2head_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(throax_9,head_11))
    bone_throax2hip1_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(throax_9,hip_1))
    neck_bending=angle_bet_vect(bone_throax2head_cor,bone_thorax2hip) # <180 indicates neck side bending

    #print("neck_bending",neck_bending)

    #Trunk flexion
    trunk_flexion=leaning

    #print("trunk_flexion",trunk_flexion)

    #Trunk twisted
    bone_shoulder_r2shoulder_l=projection_on_plane(transverse_normal_vect,vector_m_to_n(shoulder_r_15,shoulder_l_12))
    bone_hip_r2hip_l=projection_on_plane(transverse_normal_vect,vector_m_to_n(hip_r_2,hip_l_5))
    trunk_twisted=angle_bet_vect(bone_shoulder_r2shoulder_l,bone_hip_r2hip_l)

    #print("trunk_twisted",trunk_twisted)


    #Trunk side bending
    bone_hip2throax_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(hip_1,throax_9))
    bone_hip2hip_r_cor=projection_on_plane(coronal_normal_vect,vector_m_to_n(hip_1,hip_r_2))
    side_bending=angle_bet_vect(bone_hip2throax_cor,bone_hip2hip_r_cor) # >90 or <90 indicates side bending

    #print("side_bending",side_bending)

    #Neck twisted
    bone_shoulder_r2shoulder_l_trans=projection_on_plane(transverse_normal_vect,vector_m_to_n(shoulder_r_15,shoulder_l_12))
    face_normal_trans=projection_on_plane(transverse_normal_vect,face_plane_normal_vect)
    neck_twisted= angle_bet_vect(bone_shoulder_r2shoulder_l_trans,face_normal_trans)#<90 or >90 indicates neck twisted
    
    #print("Neck twisted",neck_twisted)


    upper_arm_score_r=1
    lower_arm_score_r=1
    upper_arm_score_l=1
    lower_arm_score_l=1
    neck_score=1
    trunk_score=1

    #Score for left upper arm
    if (upper_arm_flexion_l<20 and upper_arm_flexion_l>-20):
        upper_arm_score_l=1
    elif (upper_arm_flexion_l>-20):
        upper_arm_score_l=2
    elif (upper_arm_flexion_l>20 and upper_arm_flexion_l<45):
        upper_arm_score_l=2
    elif (upper_arm_score_l>45 and upper_arm_flexion_l<90):
        upper_arm_score_l=3
    elif (upper_arm_score_l>90):
        upper_arm_score_l=4
    if (raised_shoulder_l>90):
        upper_arm_score_l+=1
    if (upper_arm_abduction_l>0):
        upper_arm_score_l+=1
    if (leaning>0):
        upper_arm_score_l-=1

    #Score for right upper arm
    if (upper_arm_flexion_r<20 and upper_arm_flexion_r>-20):
        upper_arm_score_r=1
    elif (upper_arm_flexion_r>-20):
        upper_arm_score_r=2
    elif (upper_arm_flexion_r>20 and upper_arm_flexion_r<45):
        upper_arm_score_r=2
    elif (upper_arm_score_r>45 and upper_arm_flexion_r<90):
        upper_arm_score_r=3
    elif (upper_arm_score_r>90):
        upper_arm_score_r=4
    if (raised_shoulder_r>90):
        upper_arm_score_r+=1
    if (upper_arm_abduction_r>0):
        upper_arm_score_r+=1
    if (leaning>0):
        upper_arm_score_r-=1
    
    #Score for left lower arm
    if (lower_arm_flexion_l>60 and lower_arm_flexion_l<100):
        lower_arm_score_l=1
    elif (lower_arm_flexion_l<60 or lower_arm_flexion_l>100):
        lower_arm_score_l=2
    if (low_arm_r_across_mid_line>90 or low_arm_l_across_mid_line>90):
        lower_arm_score_l+=1
    
    #Score for right lower arm
    if (lower_arm_flexion_r>60 and lower_arm_flexion_r<100):
        lower_arm_score_r=1
    elif (lower_arm_flexion_r<60 or lower_arm_flexion_r>100):
        lower_arm_score_r=2
    if (low_arm_r_across_mid_line>90 or low_arm_l_across_mid_line>90):
        lower_arm_score_r+=1

    #Score for neck
    if (neck_extension>=0 and neck_extension<=10):
        neck_score=1
    elif (neck_extension>10 and neck_extension<=20):
        neck_score=2
    elif (neck_extension>20 ):
        neck_score=3
    elif (neck_extension<0):
        neck_score=4
    if (neck_bending<150): # needs calibration
        neck_score+=1
    if (neck_twisted>40):# needs calibration
        neck_score+=1

    #Score for trunk
    if (leaning==0):
        trunk_score=1
    elif (leaning>0 and leaning <=20):
        trunk_score=2
    elif (leaning>20 and leaning<=60):
        trunk_score=3
    elif (leaning >60):
        trunk_score=4
    if (side_bending>110 or side_bending<70):
        trunk_score+=1
    if (trunk_twisted>45):
        trunk_score+=1


    
    if (neck_score>=4  or trunk_score>=4):
        if (neck_score>=4):
            feedback_list[1]=feedback_list[1]+1
            #print("Neck is in bad") # critical 
        if(trunk_score>=4):
            feedback_list[2]=feedback_list[2]+1
            #print("Trunk is in bad") # critical
    else:
        if((neck_score==2 or neck_score==3)and trunk_score==3):
            feedback_list[3]=feedback_list[3]+1
            #print("Neck and Trunk is in bad") #warning



    if(upper_arm_score_l>=3):
        feedback_list[4]=feedback_list[4]+1
        #print("Left upper arm is in bad")
    elif (upper_arm_score_l==2 and lower_arm_score_l==3):
        feedback_list[5]=feedback_list[5]+1
        #print("Left upper arm and Left lower arm is in bad")
    if(upper_arm_score_r>=3):
        feedback_list[6]=feedback_list[6]+1
        #print("Right upper arm is in bad")
    elif(upper_arm_score_r==2 and lower_arm_score_r==3):
        feedback_list[7]=feedback_list[7]+1
        #print("Right upper arm and Right lower arm is in bad")
    
    

    #((Upper Arm=1 &Lower arm=3)|Upper arm>2 & Upper arm<4)&((Trunk=3&Neck=1)|(Trunk=1&Neck=3)|(Trunk=2&Neck=3))
    #if((upper_arm_score_l==1 and lower_arm_score_l==3) or (upper_arm_score_l>2 and upper_arm_score_l<4) )


if __name__=='__main__':
    joints=np.random.rand(17,3)
    feedback_list=[]
    rula_assess(joints,feedback_list)

    
