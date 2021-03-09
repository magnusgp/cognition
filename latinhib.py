#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 21:36:57 2021

@author: magnus
"""

import numpy as np


# Function for computing activation levels

# Takes input I (array) and w (number)
# Returns output A (array) containing activation levels

def LatInhib(I,w):
  A = np.zeros(len(I))
  # Set edges equal to input edges
  A[0] = I[0]
  A[-1] = I[-1]
  for i in range(1,(len(I)-1)):
  # Compute activation levels
    A[i] = I[i] - w*(I[i-1]+I[i+1])
  return A

#%%

# Function for computing activation levels using convolution

# Takes input I (array) and w (number)
# Returns output A (array) containing activation levels

def KernelInhib(I,w):
    A = np.convolve(I,w)
    return A