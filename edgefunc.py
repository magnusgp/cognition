#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 21:37:31 2021

@author: magnus
"""

import numpy as np

# Function for detecting edges

# Takes input I (array) and w (number)
# Returns output A (array) containing a 1 if an edge is present, otherwise 0

def EdgeFunc(I,w):
  A = np.zeros(len(I))
  # Set threshold
  thold = 0.9
  # Set edges equal to input edges
  A[0] = I[0]
  A[-1] = I[-1]
  for i in range(1,(len(I)-2)):
  # Compute activation levels
    A[i] = I[i] - w*(I[i-1]+I[i+1])
  # Set pixel value to 1 if equal or above threshold
    if A[i] - A[i+1] >= thold:
      A[i] = 1
  # Otherwise set pixel value equal to 0
    else:
      A[i] = 0
  return A