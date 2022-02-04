# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 14:54:37 2021

@author: tech crusaders
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as img
import math

def crop(image):
    p= np.shape(image)[0]
    q= np.shape(image)[1]
    ref=img.imread('reference.jpg')
    plt.imshow(ref)
    plt.show()
    dist1=int(input("Enter dist1 "))
    dist2=int(input("Enter dist2 "))
    dist3=int(input("Enter dist3 "))
    dist4=int(input("Enter dist4 "))
    
    image=image[dist4:(p-dist2) , dist1:(q-dist3)]
    plt.imshow(image)
    plt.show()
    
    
    
def gray_scale(image):
    rgb_weights = [0.2989, 0.5870, 0.1140]

    grayscale_image = np.dot(image[...,:3], rgb_weights)
    plt.imshow(grayscale_image,cmap=plt.get_cmap("gray"))
    plt.show()


    

def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    #gray_image= plt.imshow(rgb2gray(gray),cmap=plt.get_cmap("gray")

    return gray                           

def combo(image1,image2,orientation):
    try:
        c_image= np.append(image1,image2, axis= orientation)
        plt.imshow(c_image)
        plt.show()
        
    except:
        print("\nInvalid Operation!\nChoose an image with the same dimensions")

    

def threshold(image,thresh_value):
    g_image=rgb2gray(image)
    p= np.shape(image)[0]
    q= np.shape(image)[1]
    for i in range(0,p):
        for j in range(0,q):
           if g_image[i,j]<thresh_value:
               g_image[i,j]=0
           else:
               g_image[i,j]=255
    plt.imshow(g_image,cmap=plt.get_cmap("gray"))
    plt.show()
    

def rotation(image,direction):
    clock=np.array([0,-1,0,1,0,0,0,0,1])
    clock=clock.reshape(3,3)
    anti=np.array([0,1,0,-1,0,0,0,0,1])
    anti=anti.reshape(3,3)
    
    #rot_image=np.dot(image,)
    if direction==1:
        rot_image=np.rot90(image)
    if direction==2:
        rot_image=np.rot90(image)
        for i in range(0,2):
            rot_image=np.rot90(rot_image)
            
        
    plt.imshow(rot_image)
    plt.show()
    
# =============================================================================
#     rot_image=np.swapaxes(image,1,0)
#     rot_image=np.flip(rot_image,0)
#     rot_image=plt.imshow(rot_image)
#     plt.show()
# 
# =============================================================================
def rotate_at_an_angle(image,angle):
    w,h,c=image.shape
    img_transformed= np.empty((w,h,c),dtype=np.uint8)
    
    T=np.array([math.cos(alp),math.sin(alp),0,math.sin(-alp),math.cos(alp),0,0,0,1])
    T=T.reshape(3,3)   
    for i, row in enumerate(image):
        for j, col in enumerate(row):
            pixel_data = image[i, j, :]
            input_coords = np.array([i, j, 1])
            i_out, j_out, _ = T @ input_coords
            try:   
             img_transformed[int(i_out), int(j_out), :] = pixel_data
            except:
                break
    plt.imshow(img_transformed)
    plt.show()

def resize(image,cx,cy):
    h,w,c=image.shape
    h=int(h*cy)
    w=int(w*cx)
    T= np.array([[cx, 0, 0], [0, cy, 0], [0, 0, 1]])
    
    img_transformed = np.empty((h,w, c),dtype=np.uint8)
    for i, row in enumerate(image):
        for j, col in enumerate(row):
            pixel_data = image[i, j, :]
            input_coords = np.array([i, j, 1])
            i_out, j_out, _ = T @ input_coords
            #try:
            img_transformed[int(i_out), int(j_out), :] = pixel_data
            #except:
              #  continue
    
    #works perfectly fine for symmetric scaling but shows index error for dissimilar scaling
    plt.imshow(img_transformed)
    plt.show()

#takes few seconds to output an image,please wait   



while True:
    x=True
    #input a valid image. before uploading copy the file in the folder
    while x==True:
        try:
            
            img_name= input("Enter name of the image file: ")
            img_name=img_name
            image=img.imread(img_name)
            
            plt.imshow(image)
            plt.show()
            
            
            p,q,c=image.shape
            print(p,'\t',q)
            x=False
            
        except:
            print("Image does not exist in the database!\nChoose an image")
        
        
        
    print("\nActions to be performed \n1. 1 for cropping\n2. 2 for grayscaling\n3. 3 for Thresholding\n4. 4 for combining pictures\n5. 5 for rotating \n6. 6 for rotating at an angle \n7. 7 for resizing\n")
    action=input("Choose the action which you want to perform ")
    
    while action!='q':
    
        
        if action=='1' :
            crop(image)
        
        if action=='2':
            gray_scale(image)
        
        if action=='4':
            add_image=plt.imread(input("Enter name of image to be added ")+".jpg")
            orientation=int(input("Choose\n1. for left-right combination\n2. for top-bottom combination"))
            if orientation==1:
                o=1
            elif orientation==2:
                o=0
            combo(image,add_image,o)
        
        if action=='3':
            T=int(input("Enter the value for thresholding "))
            threshold(image,T)
            
        if action=='5':
            direction=int(input("Press\n1. for anti-clockwise rotation \n2. for clockwise rotation\n"))
            rotation(image,direction)
        
        if action=='6':
            alp=float(input("Enter an angle "))
            alp=math.radians(alp)
            rotate_at_an_angle(image, alp)
        if action=='7':
            print("Enter values for scaling")
            cx=float(input("\nX-scale "))
            cy=float(input("\nY-scale "))
            resize(image,cx,cy)
            
            
        print("\nActions to be performed \n1. 1 for cropping\n2. 2 for grayscaling\n3. 3 for Thresholding\n4. 4 for combining pictures\n5. 5 for rotating \n6. 6 for rotating at an angle \n7. 7 for resizing\n")
        print("\nPress Q to quit")
        action=input("Choose the action which you want to perform ")
        
    break
    
    
