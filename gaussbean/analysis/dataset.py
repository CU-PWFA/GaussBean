#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Created on Sun Feb  18 02:37:00 2024

@author: leahghartman

Description : A file containing functions capable of analyzing a full dataset of images.
"""
# import random needed packages that should already be installed
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from mpl_toolkits.axes_grid1 import make_axes_locatable

# import from other modules in the package
from single import single_image_proj
from pre_utils import crop_image
from calc_utils import check_array, find_centroid, find_proj_x, find_proj_y, find_line_x, find_line_y

#########################
### START OF FUNCTIONS
#########################

def full_set(imglist, xmargins, ymargins, pixelsize=3.45, lineout=False):

    xlist = []
    ylist = []
    croppedimgs = []

    if lineout==True:
        # for loop that cycles through all of the images and finds the FWHM along each axis
        for i in img_list:
            xFWHM, yFWHM, croppedimg = single_image_line(xmargins, ymargins, imgar=np.array(Image.open(i)));
            xlist.append(xFWHM * pixelsize);
            FWHMyar.append(yFWHM * pixelsize);

    else:
        # for loop that cycles through all of the images and finds the FWHM along each axis
        for i in imglist:
            xFWHM, yFWHM, croppedimg = single_image_proj(xmargins, ymargins, imgar=np.array(Image.open(i)))
            xlist.append(xFWHM * pixelsize);
            ylist.append(yFWHM * pixelsize);

    return(xlist, ylist, croppedimgs)
    

