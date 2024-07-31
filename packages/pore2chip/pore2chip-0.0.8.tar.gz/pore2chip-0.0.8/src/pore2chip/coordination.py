import numpy as np
import porespy as ps
import openpnm as op


def coordination_nums_3D(img_list, pn=None):
    r"""
    Get coordination numbers of each pore in a given a list of images.
    If given an OpenPNM network, it will return the coordination numbers 
    from it instead.

    Parameters:
        img_list : Array of input images
        pn : OpenPNM pore network

    Output:
        coordination_nums : Pore coordination numbers
    """
    if pn is not None:
        coordination_nums = op.models.network.coordination_number(pn)
        return coordination_nums
    else:
        snow_output = ps.networks.snow2(img_list, voxel_size=1)
        pn2 = op.io.network_from_porespy(snow_output.network)
        coordination_nums = op.models.network.coordination_number(pn2)
        return coordination_nums


def coordination_nums_2D(img_list):
    r"""
    Get coordination numbers of each pore in a 2D slice

    Parameters:
        img_list : Array of input images

    Output:
        coordination_nums_2D : Pore coordination numbers
    """

    coordination_nums_2D = []
    for k in range(len(img_list)):
        # Use the Snow algorithm (included in PoreSpy) to calculate a pore
        # network and convert it to an OpenPNM network
        snow_output = ps.networks.snow2(img_list[k, :, :], voxel_size=1)
        pn = op.io.network_from_porespy(snow_output.network)

        temp_coordination = op.models.network.coordination_number(pn)
        coordination_nums_2D = np.concatenate(
            (coordination_nums_2D, temp_coordination))

    return coordination_nums_2D
