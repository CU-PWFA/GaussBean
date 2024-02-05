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

def plot_beforeandafter(before, after, label='', clmap='plasma', fontsize=15):
    """ Returns a plot of an image before and after it has been run through a filter or altered in some way.

        Parameters
        ----------
        before : array
            The array associated with an image before it has been altered.
        after : array
            The array associated with an image after it has been altered.
        label (OPTIONAL) : string
            A string associated with WHAT is altering the image (could be "Median Filter" for example). Will be added to the title of the plot.
        clmap (OPTIONAL) : string
            The colormap that the user wants to use for the plots. This MUST be a colormap given by the matplotlib package.
        fontsize (OPTIONAL) : integer
            The fontsize used for the title of the plot. The axes labels are automatically formatted based on this number.
    """
    # format the figure so we have both images with before on the left and after on the right; add in some nice settings
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.5, 3))

    # set the title and axes labels for the image
    ax1.set_title('Image Before' + label, fontsize=fontsize)
    ax2.set_title('Image After' + label, fontsize=fontsize)
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

def plot_medandlow():
    """ Returns a plot of the original image, the image after ONLY a median filter has been applied, the image after ONLY a low-pass filter has been applied, and
        the image after BOTH a median filter and low-pass filter have been applied.

        Parameters
        ----------
        imgpath : string
            The path to the image that the user wants to run through the median filter.
        mediansize : integer
            The size of the median filter in pixels (generally want this to be small; from 2-10 pixels).
        radius : integer
            The radius of the mask used for the low-pass filter in pixels.
        repeatamount (OPTIONAL) : integer
            The times the user wants the MEDIAN filter to be run over the image.
        clmap (OPTIONAL) : string
            The colormap that the user wants to use for the plots. This MUST be a colormap given by the matplotlib package.
        fontsize (OPTIONAL) : integer
            The fontsize used for the title of the plot. The axes labels are automatically formatted based on this number.
    """
    # get the original image, the image after the median filter, the image after the low-pass filter, and the image after both filters
    original = np.array(Image.open(imgpath).convert('L'))
    aftermed = np.array(thru_median(imgpath, radius))
    afterlow = np.array(thru_lowpass(imgpath, radius))
    afterboth = np.array(thru_lowpass(aftermed, radius, isArray=True, arimg=aftermed))
    
    # create a figure with four subplots, show the images that are found above, and label each of them
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle('Original Image Compared to Combinations of Filters', fontsize=fontsize, y=1.01)
    ax1.imshow(original, cmap=clmap)
    ax1.set_title('Original Image', fontsize=fontsize-3)
    ax2.imshow(aftermed, cmap=clmap)
    ax2.set_title('After Median Filter', fontsize=fontsize-3)
    ax3.imshow(afterlow, cmap=clmap)
    ax3.set_title('After Low-Pass Filter', fontsize=fontsize-3)
    ax4.imshow(afterboth, cmap=clmap)
    ax4.set_title('After Both Filters', fontsize=fontsize-3)

    # label all x- and y-axes
    fig.text(0.5, 0.04, 'x pixels', ha='center', fontsize=fontsize-3)
    fig.text(0.04, 0.5, 'y pixels', va='center', rotation='vertical', fontsize=fontsize-3)

    # fix the axes ticks so they only show for outer plots
    for ax in fig.get_axes():
        ax.label_outer()

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
    
    # plot before and after doing background subtraction
    plot_beforeandafter(before, after, title='Cropping', clmap='plasma', fontsize=fontsize)

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
    
    # plot before and after doing background subtraction
    plot_beforeandafter(before, after, title='Background Subtraction', clmap=clmap, fontsize=fontsize)

########################################################

def sum_intensity_prof(imgpath='', imgar=[], lineout=False, xpixel=0, ypixel=0, toavg=0):
    """ Returns the lineout of an image along the y-axis and averages multiple columns of pixels if the user wants.

        Parameters
        ----------
        xpixel : integer
            Specifies at what ROW the user wants to take the lineout along the image in pixels.
        imgpath (OPTIONAL) : string
            The path to the image that the user wants to run through the median filter.
        imgar (OPTIONAL) : array
            Array of the image if the user wants to input an array into the function rather than just an image path.
        toavg (OPTIONAL) : integer
            Specifies the number of pixels on EACH SIDE of the original pixel lineout the user wants to average with (so, center lineout, plus two lineouts on
            either side if "toavg" is set equal to 2.
    """
    # set the array of the image to whatever the user specifies (either based on the image path OR an array that the user inputs)
    arrayimg = check_array(imgpath, imgar)

    # find the width and height of the image
    imheight, imwidth = np.shape(arrayimg)

    # create a numpy array so the axes will actually work on the right-hand-side graph (this isn't necessary on the top graph)
    positionsy = np.arange(1, imheight + 1, 1)
    positionsx = np.arange(1, imwidth + 1, 1)

    # customize the plots/plot as a whole (that is literally all that these lines of code do)
    fig, main_ax = plt.subplots(figsize=(7, 7))
    divider = make_axes_locatable(main_ax)
    top_ax = divider.append_axes("top", 1.05, pad=0.3, sharex=main_ax)
    right_ax = divider.append_axes("right", 1.05, pad=0.3, sharey=main_ax)

    # make the tick labels on the bottom sides of the top- and right-hand-side graphs disappear
    top_ax.xaxis.set_tick_params(labelbottom=False)
    right_ax.yaxis.set_tick_params(labelleft=False)
    right_ax.tick_params(labelrotation=-90)

    # give labels to all of the necessary axes and plots themselves (might have to play with the arangement of the right plot's title)
    main_ax.set_xlabel('x pixels', fontsize=13)
    main_ax.set_ylabel('y pixels', fontsize=13)
    top_ax.set_title('Intensity Profile (Projection) of Pixel Columns', fontsize=13)
    right_ax.set_title('Intensity Profile (Projection) of Pixel Rows', x=1.13, y=-0.05, rotation=-90, fontsize=13)

    # show the image as the main plot
    main_ax.imshow(arrayimg, extent=[0, imwidth, 0, imheight])

    # calculates the sum of the intensity values of all the pixels in every row and column
    cols = find_proj_x(imgar=arrayimg)
    rows = find_proj_y(imgar=arrayimg)

    # plots the right and top graphs with certain colors. If you want a different color, just change the 'color' input below
    v_prof, = right_ax.plot(rows, positionsy, color='black')
    h_prof, = top_ax.plot(cols, color='black')

    # show the entire figure
    plt.autoscale()
    plt.show()

