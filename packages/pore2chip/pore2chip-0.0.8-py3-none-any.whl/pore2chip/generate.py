import math
import numpy as np
import openpnm as op
import random
from skimage.morphology import diamond


def generate_network(
        n,
        pore_diameters,
        throat_diameters,
        coordination_nums,
        pore_pdf=None,
        throat_pdf=None,
        coord_pdf=None,
        average_coord=None,
        pore_random_shift=0.2,
        lone_pores=True):
    r"""
    Create 2D OpenPNM network with given pore, throat, and coordination 
    information

    Parameters:
        n : Number of desired pores (cubic lattice will be n x n)
        pore_diameters : Array of input pore diameters
        pore_pdf : Array of pore size probabilities
        throat_diameters : Array of input throat diameters
        throat_pdf : Array of throat size probabilities
        coordination_nums : Array of pore coordination numbers
        coord_pdf : Array of pore coordination probabilities
        average_coord : Average coordination number (by default, generation 
            will not target specific average coordination number)

    Output:
        generated_network : OpenPNM network
    """

    random.seed()

    generated_network = op.network.BodyCenteredCubic([n, n, 2])
    op.topotools.trim(generated_network, pores=generated_network.pores('zmax'))
    op.topotools.trim(
        generated_network,
        throats=generated_network.throats('body_to_body'))
    op.topotools.trim(
        generated_network,
        throats=generated_network.throats('corner_to_corner'))
    generated_network['pore.coords'] *= [1, 1, 0]

    # Add geometry (spheres and cylinders)
    geo = op.models.collections.geometry.spheres_and_cylinders
    generated_network.add_model_collection(geo)
    generated_network.regenerate_models()

    # Shift points and scale (pores reach the edges)
    for pore_index in range(len(generated_network['pore.coords'])):
        generated_network['pore.coords'][pore_index][0] -= 0.5
        generated_network['pore.coords'][pore_index][1] -= 0.5
        generated_network['pore.coords'][pore_index][0] *= (n / (n - 1))
        generated_network['pore.coords'][pore_index][1] *= (n / (n - 1))

    # Remove 3D aspects to create 2D image
    del generated_network.params['dimensionality']

    # Get numbers of pores and throats
    num_pores = len(generated_network['pore.coords'])
    num_throats = len(generated_network['throat.conns'])

    # Random sizes and coordination numbers based on extracted data
    # distributions
    random_diameter = None
    temp_coordination = None
    random_coordination = None

    if pore_pdf is not None:
        random_diameter = np.random.choice(
            a=pore_diameters, size=num_pores, replace=True, p=pore_pdf)
    else:
        random_diameter = random.choices(pore_diameters, k=num_pores)
    if coord_pdf is not None:
        temp_coordination = np.random.choice(
            coordination_nums, num_pores, replace=True, p=coord_pdf)
        random_coordination = temp_coordination.astype(
            int)  # convert float to int
    else:
        random_coordination = random.choices(coordination_nums, k=num_pores)

    # Assign random pore diameters
    generated_network['pore.diameter'] = random_diameter

    if throat_diameters is None:
        print('Continuing without throats...')
        op.topotools.trim(generated_network,
                          throats=generated_network['throat.all'])
        return generated_network

    # edit connections to get specified coordination numbers
    for pore_index in range(num_pores):

        # Get connected throats
        neighbor_throats = generated_network.find_neighbor_throats(pore_index)

        # If the pore has more throats than what we want...
        if (len(neighbor_throats) > random_coordination[pore_index] or 
                neighbor_throats.size > 8):
            if len(neighbor_throats) == 0:
                continue

            for throat_index in neighbor_throats:
                # Disconnect the extra throats
                if throat_index < len(generated_network['throat.conns']):
                    op.topotools.trim(
                        generated_network, throats=[throat_index])

        # If the pore has less throats than what we want...
        elif len(neighbor_throats) < random_coordination[pore_index]:
            # Find pores around the vicinity of this pore
            neighbor_pores = generated_network.find_nearby_pores(
                pores=[pore_index], r=1.5, flatten=True)

            for pore in range(
                    random_coordination[pore_index] -
                    len(neighbor_throats)):
                # Connect the pores to a new neighbor
                if (len(neighbor_throats) +
                        pore) > 8:  # Limits coordination to 8
                    if pore_index < neighbor_pores[-1]:
                        op.topotools.connect_pores(
                            generated_network, pore_index, neighbor_pores[-1])
                    else:
                        op.topotools.connect_pores(
                            generated_network, neighbor_pores[-1], pore_index)

    # Remove any duplicate throats that may have been formed
    dupes = op.models.network.duplicate_throats(generated_network)
    op.topotools.trim(generated_network, throats=dupes)

    # Remove non-connected pores
    if not lone_pores:
        coord = op.models.network.coordination_number(generated_network)
        op.topotools.trim(generated_network, pores=np.where(coord == 0))

    # Reduce even further to an average coordination
    if average_coord is not None:
        reduce = op.topotools.reduce_coordination(
            generated_network, average_coord)
        op.topotools.trim(generated_network, throats=reduce)

    # Slightly randomize pore positions
    for pore_index in range(len(generated_network['pore.coords'])):
        # 0.1
        shift_amount_x = np.random.uniform(-pore_random_shift,
                                           pore_random_shift)
        # 0.1
        shift_amount_y = np.random.uniform(-pore_random_shift,
                                           pore_random_shift)
        generated_network['pore.coords'][pore_index][0] += shift_amount_x
        generated_network['pore.coords'][pore_index][1] += shift_amount_y

    # Assign random pore throat diameters
    random_throat_diameter = None
    if throat_pdf is not None:
        random_throat_diameter = np.random.choice(
            throat_diameters, num_throats, replace=True, p=throat_pdf)
    else:
        random_throat_diameter = random.choices(
            throat_diameters, k=len(
                generated_network['throat.diameter']))
    generated_network['throat.diameter'] = random_throat_diameter

    return generated_network
