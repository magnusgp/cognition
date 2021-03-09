#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:07:11 2021

@author: magnus
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Import Mona Lisa painting
img = plt.imread("MonaLisa.jpg")

# Normalise pixel data
def im2double(img):
    min_val = np.min(img.ravel())
    max_val = np.max(img.ravel())
    out = (img - min_val) / (max_val - min_val)
    return out

# Display normalized painting in grayscale
img_dbl = im2double(img)
plt.axis("off")
plt.imshow(img_dbl,cmap="gray")
plt.show()

# Kernel function

# Takes input n (integer) and w (number)
# Returns output k (matrix) containing scaled kernel function
def KernelFunc(n,w):
    k_n = np.full((n,n),-w)
    ones = np.full((n,n),1)
    k1 = np.hstack((k_n,k_n,k_n))
    k2 = np.hstack((k_n,ones,k_n))
    k3 = np.copy(k1)
    k = np.vstack((k1,k2,k3))
    return k

# Display picture for scale 1 to 15
for i in range(1,15):
    # Compute picture from convolution on scale i
    f_out = signal.convolve2d(img,KernelFunc(i, 0.1))
    plt.axis("off")
    plt.imshow(f_out,cmap="gray")
    plt.title("Kernel scale: %d" % i)
    plt.show()
#%%    

# Edge function
# Displays edges on image, on kernel scale 1 to 20
for i in range(1,20):
    # Set edge threshold
    thresh = 0.375
    # Compute picture from convolution on scale i    
    f_out = signal.convolve2d(img,KernelFunc(i, 0.1))
    # Normalize it
    f_out = im2double(f_out)
    
    # Loop over each pixel, if value is above threshold, set value to 1
    # If value is below threshold, set value to 0
    for j in range(f_out.shape[0]):
        for n in range(f_out.shape[1]):
            if f_out[j,n]>=thresh:
                f_out[j,n] = 0
            else:
                f_out[j,n] = 1
               
    # Display edges on the picture
    plt.axis("off")
    plt.imshow(f_out,cmap="gray")
    plt.title("Kernel scale: %d" % i)
    plt.show()
    
#%%

# Read Hermann grid picture, normalize and display it
img2 = plt.imread("hermann.jpg")
img2_dbl = im2double(img2)

plt.axis("off")
plt.imshow(img_dbl,cmap="gray")
plt.show()

# Display picture for scale 1 to 15
for i in range(1,15):
    # Compute picture from convolution on scale i
    f_out = signal.convolve2d(img2,KernelFunc(i, 0.1))
    plt.axis("off")
    plt.imshow(f_out,cmap="gray")
    plt.title("Kernel scale: %d" % i)
    plt.show()