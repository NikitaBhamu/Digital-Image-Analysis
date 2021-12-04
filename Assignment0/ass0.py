import numpy as np
from matplotlib import pyplot as plt
import cv2
import os
import math


height = 480
width = 480
inner_intensity = 220
outer_intensity1 = 180
outer_intensity2 = 100
outer_intensity3 = 0
blank_image1 = np.zeros((height,width), np.uint8)
blank_image2 = np.zeros((height,width), np.uint8)
blank_image3 = np.zeros((height,width), np.uint8)
blank_image1[height//3:2*(height//3),width//3:2*(width//3)] = (inner_intensity)
blank_image2[height//3:2*(height//3),width//3:2*(width//3)] = (inner_intensity)
blank_image3[height//3:2*(height//3),width//3:2*(width//3)] = (inner_intensity)

#outer intensity 1 = 160
blank_image1[:,0:width//3] = (outer_intensity1)
blank_image1[0:height//3,width//3:2*(width//3)] = (outer_intensity1)
blank_image1[2*(height//3):height,width//3:2*(width//3)] = (outer_intensity1)
blank_image1[:,2*(width//3):width] = (outer_intensity1)

#outer intensity 2 = 90
blank_image2[:,0:width//3] = (outer_intensity2)
blank_image2[0:height//3,width//3:2*(width//3)] = (outer_intensity2)
blank_image2[2*(height//3):height,width//4:3*(width//4)] = (outer_intensity2)
blank_image2[:,2*(width//3):width] = (outer_intensity2)

#outer intensity 3 = 10
blank_image3[:,0:width//3] = (outer_intensity3)
blank_image3[0:height//3,width//3:2*(width//3)] = (outer_intensity3)
blank_image3[2*(height//3):height,width//4:3*(width//4)] = (outer_intensity3)
blank_image3[:,2*(width//3):width] = (outer_intensity3)

cv2.imshow('img1',blank_image1)
cv2.imshow('img2',blank_image2)
cv2.imshow('img3',blank_image3)
cv2.waitKey(0)

cv2.destroyAllWindows()
