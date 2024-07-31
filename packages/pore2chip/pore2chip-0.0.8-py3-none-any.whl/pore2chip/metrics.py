import numpy as np
from skimage.measure import label, regionprops
import feret
import porespy as ps
import openpnm as op
import copy


def feret_diameter(image):
    r"""
    Get maximum and minimum feret diameters of a single image

    Parameters:
        image : Input image

    Output:
        result : Tuple of arrays of max feret diameters and min feret diameters
    """

    max_ferets = []
    min_ferets = []

    label_img = label(image)
    regions = regionprops(label_img)

    for region in regions:  # <------------ iterates through each sub image
        minr, minc, maxr, maxc = region.bbox

        maxf = feret.max(region.image_filled)
        minf = feret.min(region.image_filled)
        max_ferets.append(maxf)
        min_ferets.append(minf)

    return max_ferets, min_ferets


def feret_diameter_list(img_list):
    r"""
    Get maximum and minimum feret diameters of each image

    Parameters:
        img_list : Array of input images

    Output:
        result : Tuple of arrays of max feret diameters and min feret diameters
    """
    max_ferets = []
    min_ferets = []

    for image in img_list[:]:  # <----------- iterates through each image
        # Uses the Skimage.measure library to label individual regions (pores)
        label_img = label(image)
        regions = regionprops(label_img)

        # This sub_images array is for saving images of individual pores and
        # sending them to the feret module
        sub_images = []
        for index in range(len(regions) -1): 
            # These are the locations of the pores bound by a box
            # The variables are in order: minimum row, minimum column, maximum
            # row, maximum column
            minr, minc, maxr, maxc = regions[index].bbox

            sub_images.insert(
                index, np.zeros(
                    (maxr - minr, maxc - minc), dtype=int))
            # The property image_filled isolates only one pore per image,
            # useful for the feret module
            sub_images[index] = regions[index].image_filled

            # The feret library does not like single pixel images, so this
            # conditional skips it
            if sub_images[index].shape == (1, 1):
                continue

            # Calculating minimum and maximum feret diameters
            maxf = feret.max(regions[index].image_filled)
            minf = feret.min(regions[index].image_filled)
            max_ferets.append(maxf)
            min_ferets.append(minf)

    return max_ferets, min_ferets


def extract_diameters(img_list, voxel_size=1):
    r"""
    Extract pore diameters and pore throat diameters

    Parameters:
        img_list : Array of input images

    Output:
        result : Tuple of arrays of pore diameters and pore throat diameters
    """
    images = copy.deepcopy(img_list)
    snow_output = ps.networks.snow2(images, voxel_size=voxel_size)
    pn = op.io.network_from_porespy(snow_output.network)

    return pn["pore.equivalent_diameter"], pn["throat.equivalent_diameter"]


def extract_diameters_alt(img_list, num_bins=10):
    r"""
    Extract pore diameters using PoreSpy local thickness filter (no pore 
    throat diameters)

    Parameters:
        img_list : Array of input images
        num_binds : Number of bins PoreSpy uses to calculate pore size 
        distribution

    Output:
        result : Array of pore diameters
    """
    inverted = cv.bitwise_not(img_list)
    filtered = ps.filters.local_thickness(inverted)
    psd = ps.metrics.pore_size_distribution(filtered, bins=num_bins, log=False)
    return psd


def get_probability_density(arr):
    r"""
    Get probability densities of given array of values

    Parameters:
        arr : Array of values

    Output:
        pdf : Array of probability densities
    """
    hist, bin_edges = np.histogram(arr, bins=len(arr), density=True)
    pdf = hist * np.diff(bin_edges)
    return pdf


def get_percent_probability(arr):
    r"""
    Get percent probability of given array of values

    Parameters:
        arr : Array of values

    Output:
        percent : Dictionary of arr and percentage chances
    """
    uniques, counts = np.unique(arr, return_counts=True)
    percentages = dict(zip(uniques, counts * 100 / len(arr)))
    return percentages
