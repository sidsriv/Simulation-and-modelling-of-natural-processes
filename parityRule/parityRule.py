# -*- coding: utf-8 -*-
# Copyright (C) 2016 Universite de Geneve, Switzerland
# E-mail contact: sebastien.leclaire@etu.unige.ch
#
# The Parity Rule
#

from numpy import *
import matplotlib.pyplot as plt
from matplotlib import cm
import scipy
import copy
    
# Definition of functions
def readImage(string): # This function only work for monochrome BMP. 
    image =  scipy.misc.imread(string,1);
    image[image == 255] = 1
    image = image.astype(int) 
    return image # Note that the image output is a numPy array of type "int".

# Main Program

# Program input, i.e. the name of the image "imageName" and the maximum number of iteration "maxIter"
imageName = 'image3.bmp'
maxIter   = 32

# Read the image and store it in the array "image"
image = readImage(imageName) # Note that "image" is a numPy array of type "int".
# Its element are obtained as image[i,j]
# Also, in the array "image" a white pixel correspond to an entry of 1 and a black pixel to an entry of 0.

# Get the shape of the image , i.e. the number of pixels horizontally and vertically. 
# Note that the function shape return a type "tuple" (vertical_size,horizontal_size)
imageSize = shape(image);

# Print to screen the initial image.
print('Initial image:')
plt.clf()
plt.imshow(image, cmap=cm.gray)
plt.show()
plt.pause(0.1)

# Main loop
for it in range(1,maxIter+1):
    
    imageCopy = copy.copy(image);
    
    for i in range(0,imageSize[0]):  
        for j in range(0,imageSize[1]):             
            iM = (i-1) % imageSize[0]
            iP = (i+1) % imageSize[0]            
            jM = (j-1) % imageSize[1]
            jP = (j+1) % imageSize[1]
            image[i,j] = (imageCopy[iM,j] + imageCopy[iP,j] + imageCopy[i,jM] + imageCopy[i,jP]) % 2
    
    # Print to screen the image after each iteration.
    print('Image after',it,'iterations:')
    plt.clf()
    plt.imshow(image, cmap=cm.gray)
    plt.show()
    plt.pause(0.1)
        
# Print to screen the number of white pixels in the final image
print("The number of white pixels after",it,"iterations is: ", sum(image))