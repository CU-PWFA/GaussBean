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
from beamsize import check_array, find_centroid

#########################
### START OF FUNCTIONS
#########################

def back_subtract(backpath='', origpath='', origimgar=[], backimgar=[]):
    """ Returns an image in the form of an array after a background image provided by the user is subtracted from the original image.

        Parameters
        ----------
        imgpath (OPTIONAL) : string
            The path to the image that the user wants to run through the median filter.
        imgar (OPTIONAL) : array
            Array of the image if the user wants to input an array into the function rather than just an image path.
    """
    # set the array of the original image to whatever the user specifies (either based on the image path OR an array that the user inputs)
    origimg = check_array(origpath, origimgar)
    
    # set the array of the original image to whatever the user specifies (either based on the image path OR an array that the user inputs)
    backimg = check_array(backpath, backimgar)

    # subtract the background image from the original image
    diff = origimg - backimg

    # return the array of the image after background subtraction
    return(diff)

########################################################

def back_sub_plot(backpath='', origpath='', origimgar=[], backimgar=[], clmap='plasma', fontsize=15):
    """ Returns a plot of the image before and after a background image provided by the user is subtracted from the original image.

        Parameters
        ----------
        imgpath (OPTIONAL) : string
            The path to the image that the user wants to run through the median filter.
        imgar (OPTIONAL) : array
            Array of the image if the user wants to input an array into the function rather than just an image path.
    """
    # get the array of the image before and after background subtraction
    before = check_array(origpath, origimgar)
    after = back_subtract(backpath='', origpath='', origimgar=[], backimgar=[])
    
    # plot both images with before filtering on the left and after the filtering on the right; add in some nice settings
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.5, 3))

    # set the title and axes labels for the image
    ax1.set_title('Image Before Background Subtraction', fontsize=fontsize)
    ax2.set_title('Image After Background Subtraciton', fontsize=fontsize)
    ax1.set_ylabel('y pixels', fontsize=fontsize-3)
    ax1.set_xlabel('x pixels', fontsize=fontsize-3)
    
    ax2.set_ylabel('y pixels', fontsize=fontsize-3)
    ax2.set_xlabel('x pixels', fontsize=fontsize-3)

    # show the images
    ax1.imshow(before, cmap=clmap)
    ax2.imshow(after, cmap=clmap)

########################################################

def crop_image(xpoint, ypoint, xmargins, ymargins, imgpath='', imgar=[]):
    """ Returns an image in the form of an array after being cropped the amount the user specifies.

        Parameters
        ----------
        imgpath (OPTIONAL) : string
            The path to the image that the user wants to run through the median filter.
        imgar (OPTIONAL) : array
            Array of the image if the user wants to input an array into the function rather than just an image path.
    """
    # set the array of the original image to whatever the user specifies (either based on the image path OR an array that the user inputs)
    arrayimg = check_array(imgpath, imgar)

    # crop the image
    finalimgar = arrayimg[round(centy-ymargins):round(centy+ymargins), round(centx-xmargins):round(centx+xmargins)]

    # return the cropped image array
    return(finalimgar)

########################################################

def plot_cropped():
    """ Returns a plot of the image before and after it's been cropped.

        Parameters
        ----------
        imgpath (OPTIONAL) : string
            The path to the image that the user wants to run through the median filter.
        imgar (OPTIONAL) : array
            Array of the image if the user wants to input an array into the function rather than just an image path.
    """
    # get the array of the image before and after background subtraction
    before = check_array(origpath, origimgar)
    after = back_subtract(backpath='', origpath='', origimgar=[], backimgar=[])
    
    # plot both images with before filtering on the left and after the filtering on the right; add in some nice settings
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.5, 3))

    # set the title and axes labels for the image
    ax1.set_title('Image Before Background Subtraction', fontsize=fontsize)
    ax2.set_title('Image After Background Subtraciton', fontsize=fontsize)
    ax1.set_ylabel('y pixels', fontsize=fontsize-3)
    ax1.set_xlabel('x pixels', fontsize=fontsize-3)
    
    ax2.set_ylabel('y pixels', fontsize=fontsize-3)
    ax2.set_xlabel('x pixels', fontsize=fontsize-3)

    # show the images
    ax1.imshow(before, cmap=clmap)
    ax2.imshow(after, cmap=clmap)























