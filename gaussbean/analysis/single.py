#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Created on Sun Feb  18 02:38:00 2024

@author: leahghartman

Description : A file containing functions capable of analyzing a single image in a dataset.
"""
# import random needed packages that should already be installed
import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.signal import peak_widths, find_peaks

# make sure we can get modules from the other directory
sys.path.append('../utils/')

# import from other modules in the package
from pre_utils import crop_image
from calc_utils import check_array, find_centroid, find_proj_x, find_proj_y, find_line_x, find_line_y

#########################
### START OF FUNCTIONS
#########################

def find_FWHM(imgdata):
    """ Returns the Full-Width at Half-Maximum of a set of data. This function uses the most prominent peak to find the FWHM.

        Parameters
        ----------
        imgdata : array
            Data corresponding to a singular axis or a set of data that the user wants to find the FWHM of using the most prominent peak in the data.
    """
    # find the most prominent peak
    peakmax = np.max(imgdata)

    # use the maximum value (coresponding to the most prominent peak) to find the peak of the curve to find the FWHM of
    peaks, _ = find_peaks(imgdata, prominence=(peakmax/1.1, peakmax))

    # find the width (FWHM) of the most prominent peak
    results_half = peak_widths(imgdata, peaks, rel_height=0.5)

    # return the FWHM calculation
    return(results_half[0])

########################################################

def single_image_proj(xmargins, ymargins, imgpath='', imgar=[]):
    """ Returns the image path or the array of the image based on what the user has input into the function that's calling check_array(). This function shouldn't be
    called by the user at any point.

        Parameters
        ----------
        imgpath : string
            The path to the image that the user wants to run through the median filter.
        imgar : array
            Array of the image if the user wants to input an array into the function rather than just an image path.
    """
    # set the array of the image to whatever the user specifies (either based on the image path OR an array that the user inputs)
    arrayimg = check_array(imgpath, imgar)

    # crop out as many dead pixels as possible (as long as the feature is SOMEWHAT in the middle of the image, this should be fine)
    initialcrop = crop_image(1212, 1012, 1000, 988, imgar=arrayimg)

    # find the centroid of the image with as many of the large dead pixels cropped out as possible
    centx, centy = find_centroid(imgar=initialcrop)

    # crop the image for the final time. This is the image that will be used in the rest of the analysis process
    finalimg = crop_image(centx, centy, xmargins, ymargins, imgar=initialcrop)

    # find the centroid AGAIN, but more accurately, so we can get a really nicely cropped image
    centx2, centy2 = find_centroid(imgar=finalimg)
    
    # use the projection along the y-axis to find the FWHM value for the beam along the y-axis
    yFWHM = find_FWHM(find_proj_y(imgar=finalimg))[0]
    
    # use the projection along the x-axis to find the FWHM value for the beam along the x-axis
    xFWHM = find_FWHM(find_proj_x(imgar=finalimg))[0]

    # return the FWHM value for the beam along the x- and y- directions, as well as the final cropped image, which can be used for diagnostic purposes
    return(xFWHM, yFWHM, finalimg)

########################################################

def single_image_line(xmargins, ymargins, imgpath='', imgar=[]):
    """ Returns the image path or the array of the image based on what the user has input into the function that's calling check_array(). This function shouldn't be
    called by the user at any point.

        Parameters
        ----------
        imgpath : string
            The path to the image that the user wants to run through the median filter.
        imgar : array
            Array of the image if the user wants to input an array into the function rather than just an image path.
    """
    # set the array of the image to whatever the user specifies (either based on the image path OR an array that the user inputs)
    arrayimg = check_array(imgpath, imgar)

    # crop out as many dead pixels as possible (as long as the feature is SOMEWHAT in the middle of the image, this should be fine)
    initialcrop = crop_image(1212, 1012, 1000, 988, imgar=arrayimg)

    # find the centroid of the image with as many of the large dead pixels cropped out as possible
    centx, centy = find_centroid(imgar=initialcrop)

    # crop the image for the final time. This is the image that will be used in the rest of the analysis process
    finalimg = crop_image(centx, centy, xmargins, ymargins, imgar=initialcrop)

    # find the centroid AGAIN, but more accurately, so we can get a really nicely cropped image
    centx2, centy2 = find_centroid(imgar=finalimg)
    
    # use the projection along the y-axis to find the FWHM value for the beam along the y-axis
    yFWHM = find_FWHM(find_proj_y(imgar=finalimg))[0]
    
    # use the projection along the x-axis to find the FWHM value for the beam along the x-axis
    xFWHM = find_FWHM(find_proj_x(imgar=finalimg))[0]

    # return the FWHM value for the beam along the x- and y- directions, as well as the final cropped image, which can be used for diagnostic purposes
    return(xFWHM, yFWHM, finalimg)
