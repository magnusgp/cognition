#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 21:53:41 2021

@author: magnus
"""

import numpy as np

# Function for computing activation levels using convolution

# Takes input I (array) and w (number)
# Returns output A (array) containing activation levels

def KernelInhib(I,w):
    A = np.convolve(I,w)
    return A