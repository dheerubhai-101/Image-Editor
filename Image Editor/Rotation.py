# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 10:17:34 2021

@author: tech crusaders
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import math

def rotation(image,direction):
    clock=np.array([0,-1,0,1,0,0,0,0,1])
    clock=clock.reshape(3,3)
    anti=np.array([0,1,0,-1,0,0,0,0,1])
    anti=anti.reshape(3,3)
    
    print(clock,'\n',anti)

     
    if direction==1:
        rot_image=np.dot(image,anti)
    if direction==2:
        rot_image=np.dot(image,clock)
    
    rot_image=plt.imshow(rot_image)
    plt.show()
    
def rotate_at_an_angle(image):
    alp=float(input("Enter an angle "))
    alp=math.radians(alp)
    tr=np.array([math.cos(alp),math.sin(alp),0,math.sin(-alp),math.cos(alp),0,0,0,1])
    tr=tr.reshape(3,3)   
    print(tr)   
    







img_name= input("Enter name of the image file: ")
img_name=img_name+".jpg"
image=img.imread(img_name)

plt.imshow(image)
plt.show()


p,q,c=image.shape
print(p,'\t',q)

rotation(image,1)