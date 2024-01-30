#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  26 01:00:00 2024

@author: leahghartman
"""
# import random needed packages that should already be installed
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from mpl_toolkits.axes_grid1 import make_axes_locatable

# import from other modules in the package
from prettier import thru_median, thru_lowpass

#########################
### START OF FUNCTIONS
#########################

def plot_beforeandafter(before, after, title='', clmap='plasma', fontsize=15):
    
    # format the figure so we have both images with before on the left and after on the right; add in some nice settings
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.5, 3))

    # set the title and axes labels for the image
    ax1.set_title('Image Before' + title, fontsize=fontsize)
    ax2.set_title('Image After' + title, fontsize=fontsize)
    ax1.set_ylabel('y pixels', fontsize=fontsize-3)
    ax1.set_xlabel('x pixels', fontsize=fontsize-3)
    
    ax2.set_ylabel('y pixels', fontsize=fontsize-3)
    ax2.set_xlabel('x pixels', fontsize=fontsize-3)

    # show the images
    ax1.imshow(before, cmap=clmap)
    ax2.imshow(after, cmap=clmap)

########################################################

def plot_median(imgpath, mediansize, repeatamount=0, clmap='plasma', fontsize=15):
    """ Returns a plot of the image before and after it has been run through the median filter a specified number of times.

        Parameters
        ----------
        imgpath : string
            The path to the image that the user wants to run through the median filter.
        mediansize : integer
            The size of the median filter in pixels (generally want this to be small; from 2-10 pixels).
        repeatamount (OPTIONAL) : integer
            The times the user wants the filter to be run over the image.
        clmap (OPTIONAL) : string
            The colormap that the user wants to use for the plots. This MUST be a colormap given by the matplotlib package.
        fontsize (OPTIONAL) : integer
            The fontsize used for the title of the plot. The axes labels are automatically formatted based on this number.
    """
    # get the image before the median filter is applied and after the filter is applied
    before = np.array(Image.open(imgpath).convert('L'))
    after = np.array(thru_median(imgpath, mediansize, repeatamount))

    # plot before and after
    plot_beforeandafter(before, after, title='Median Filter', clmap='plasma', fontsize=fontsize)

########################################################

def plot_lowpass(imgpath, radius, clmap='plasma', fontsize=15):
    """ Returns a plot of the image before and after it has been run through a low-pass filter one time.

        Parameters
        ----------
        imgpath : string
            The path to the image that the user wants to run through the median filter.
        radius : integer
            The radius of the mask used for the low-pass filter in pixels.
        clmap (OPTIONAL) : string
            The colormap that the user wants to use for the plots. This MUST be a colormap given by the matplotlib package.
        fontsize (OPTIONAL) : integer
            The fontsize used for the title of the plot. The axes labels are automatically formatted based on this number.
    """
    # get the image before the low-pass filter is applied and after the filter is applied
    before = np.array(Image.open(imgpath).convert('L'))
    after = np.array(thru_lowpass(imgpath, radius))

    # plot before and after
    plot_beforeandafter(before, after, title='Low-Pass Filter', clmap='plasma', fontsize=fontsize)

########################################################

def plot_cropped():
    return(1)

########################################################

def back_sub_plot():
    return(1)
