import random
import math
import numpy as np

def solid_sphere(R,npoints):
    phi=np.random.uniform(low=0, high=2*np.pi, size=(1,npoints))
    costheta=np.random.uniform(low=-1, high=1, size=(1,npoints))
    u=np.random.uniform(low=0, high=1, size=(1,npoints))
    theta = np.arccos( costheta )
    r = R * np.cbrt(u)
    x = r * np.sin( theta) * np.cos( phi )
    y = r * np.sin( theta) * np.sin( phi )
    z = r * np.cos( theta )
    vec=np.concatenate((x,y,z),axis=0)
    return vec


def hollow_sphere(r,npoints, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    return r*vec

def sphere_z(r,center):
    x=np.random.rand(5,1)
    y=np.random.rand(5,1)
    z_plus=center[2]+np.sqrt(r**2-(x-center[0])**2-(y-center[1])**2)
    z_min=center[2]-np.sqrt(r**2-(x-center[0])**2-(y-center[1])**2)
    return [x,y,z_plus,z_min]

def angle_calc(point1,point2,point3):
    point12=point2-point1
    point13=point3-point1
    #print(point12)
    #print(point13)
    #print(np.sum(point12*point13,1).reshape(np.shape(point12)[0],1))
    #print(((np.linalg.norm(point12,axis=1) * np.linalg.norm(point13,axis=1)).reshape(np.shape(point12)[0],1)))
    cosine_angle = np.sum(point12*point13,1).reshape(np.shape(point12)[0],1) / ((np.linalg.norm(point12,axis=1) * np.linalg.norm(point13,axis=1)).reshape(np.shape(point12)[0],1))
    print(cosine_angle)
    angle = np.arccos(cosine_angle)
    return np.degrees(angle)

def  angle_max_min(r,center1,center2,center3,points=1000):
    angle_list=[]
    xi1, yi1, zi1 = solid_sphere(r,points)
    xi2, yi2, zi2 = solid_sphere(r,points)
    xi3, yi3, zi3 = solid_sphere(r,points)
    sphere_around_origin1=np.concatenate((xi1.reshape((xi1.size,1)),yi1.reshape((xi1.size,1)),zi1.reshape((xi1.size,1))),axis=1)
    sphere_around_origin2=np.concatenate((xi2.reshape((xi2.size,1)),yi2.reshape((xi2.size,1)),zi2.reshape((xi2.size,1))),axis=1)
    sphere_around_origin3=np.concatenate((xi3.reshape((xi3.size,1)),yi3.reshape((xi3.size,1)),zi3.reshape((xi3.size,1))),axis=1)
    sphere_around_point1=sphere_around_origin1+center1
    sphere_around_point2=sphere_around_origin2+center2
    sphere_around_point3=sphere_around_origin3+center3
    angle=angle_calc(sphere_around_point1,sphere_around_point2,sphere_around_point3)
    return np.max(angle),np.min(angle), np.average(angle)
    '''

    for i in range(10000):
        point1=sphere_z(r,center1)
        point2=sphere_z(r,center2)
        point3=sphere_z(r,center3)
        point1_plus=np.concatenate([point1[0],point1[1],point1[2]],1)
        point2_plus=np.concatenate([point2[0],point2[1],point2[2]],1)
        point3_plus=np.concatenate([point3[0],point3[1],point3[2]],1)
        point1_min=np.concatenate([point1[0],point1[1],point1[3]],1)
        point2_min=np.concatenate([point2[0],point2[1],point2[3]],1)
        point3_min=np.concatenate([point3[0],point3[1],point3[3]],1)
        angle_plus=angle_calc(point1_plus,point2_plus,point3_plus)
        angle_min=angle_calc(point1_min,point2_min,point3_min)
        return np.max(np.concatenate([angle_min,angle_plus],0)),np.min(np.concatenate([angle_min,angle_plus],0))

    '''
        


if  __name__=='__main__':
    center1=np.array([21.8290,-240.11992,-26.548]).reshape((1,3))
    center2=np.array([0,0,0]).reshape((1,3))
    center3=np.array([43.65817,-480.239,-53.097]).reshape((1,3))
    r=np.array([44])
    print(angle_max_min(r,center1,center2,center3,10000000))
