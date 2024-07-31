import numpy as np
import drawsvg as dr
import math
import ezdxf


def network2svg(
        generated_network,
        n,
        design_size,
        pore_shape='blob',
        throat_random=1,
        pore_debug=False,
        throat_debug=False,
        throat_random_debug=False):
    r"""
    Create SVG file from OpenPNM network

    Parameters:
        generated_network : OpenPNM network
        n : Shape of the design (number of pores on each side)
        design_size : The size of the SVG image (n x n)
        pore_shape : Shape of the pore bodies (not throats). 
            Can be 'blob' or 'circle'
        throat_random : Int multiplier that decides how random the throat shape 
            will be. Default is 1. 0 will make the throats straight.
        pore_debug : Boolean that draws circles where pores are
        throat_debug : Boolean that draws lines where throats connect
        throat_random_debug : Boolean that draws lines perpendicular to 
            throat directions. Used to randomizing throat shape. throat_debug must be True

    Output:
        design : drawSVG drawing
    """

    design = dr.Drawing(
        design_size, design_size, origin=(
            0, 0))  # Origin at bottom right of image

    num_pores = len(generated_network['pore.coords'])

    if pore_shape == 'blob':
        # Draw each pore as random blobs
        fill_color = 'black'
        if pore_debug:
            fill_color = 'blue'
        for pore_index in range(num_pores):
            x_coord = generated_network['pore.coords'][pore_index][0] * \
                (design_size / n)
            y_coord = generated_network['pore.coords'][pore_index][1] * \
                (design_size / n)

            p = dr.Path(
                fill=fill_color,
                fill_opacity=1.0,
                close=True,
                transform='translate(' + str(x_coord) + ',' + str(
                    (-y_coord) + design_size) + ')')

            positions = []
            radius = generated_network['pore.diameter'][pore_index] / 2

            for i in range(9):
                rand_radius = radius + \
                    np.random.uniform(-0.4 * radius, 0.4 * radius)
                positions.append(
                    {
                        'x': math.cos(
                            (math.pi / 4) * i) * radius,
                        'y': math.sin(
                            (math.pi / 4) * i) * radius,
                        'mx': math.cos((math.pi / 4) * i - math.radians(20))
                            * rand_radius,
                        'my': math.sin((math.pi / 4) * i - math.radians(20))
                            * rand_radius})

                if i == 0:
                    p.M(positions[i]['x'], positions[i]['y'])
                elif i == 1:
                    p.Q(positions[i]['mx'], positions[i]['my'],
                        positions[i]['x'], positions[i]['y'])
                else:
                    p.T(positions[i]['x'], positions[i]['y'])

            design.append(p)

    elif pore_shape == 'circle':
        # Draw each pore as circles
        fill_color = 'black'
        if pore_debug:
            fill_color = 'blue'
        for pore_index in range(num_pores):
            x_coord = generated_network['pore.coords'][pore_index][0] * \
                (design_size / n)
            y_coord = generated_network['pore.coords'][pore_index][1] * \
                (design_size / n)
            radius = generated_network['pore.diameter'][pore_index] / 2
            design.append(dr.Circle(x_coord,  # X-coord
                                    # Y-coord (mirrors points vertically to
                                    # match OpenPNM network (drawsvg has a
                                    # different coordinate system))
                                    (-y_coord) + design_size,
                                    radius / 2,  # Radius
                                    fill=fill_color
                                    )
                          )
    else:
        return None

    if generated_network.get('throat.conns') is not None:
        num_throats = len(generated_network['throat.all'])
        for throat_index in range(
                num_throats):  # len(generated_network['throat.conns'])
            # index of first pore
            pore1 = generated_network['throat.conns'][throat_index][0]
            # index of second (connecting) pore
            pore2 = generated_network['throat.conns'][throat_index][1]

            # This block will build the pore throats out of circles to give it
            # an irregular shape
            pore1_x = generated_network['pore.coords'][pore1][0] * \
                (design_size / n)
            pore1_y = generated_network['pore.coords'][pore1][1] * \
                (design_size / n)
            pore2_x = generated_network['pore.coords'][pore2][0] * \
                (design_size / n)
            pore2_y = generated_network['pore.coords'][pore2][1] * \
                (design_size / n)

            # Set up pore coordinates
            # also mirrors points vertically to match OpenPNM network (drawsvg
            # has a different coordinate system)
            pore1_coords = [pore1_x, (-pore1_y) + design_size]
            pore2_coords = [pore2_x, (-pore2_y) + design_size]

            # Distance between the 2 pores
            distance = math.dist(pore1_coords, pore2_coords)

            # If a throat doesn't have a given diameter, skip it
            if math.isnan(generated_network['throat.diameter'][throat_index]):
                continue

            # Number of points (circles) inbetween the 2 pores 
            # number of points = total distance / diameter of each circle
            num_throat_points = math.ceil(
                distance / (generated_network['throat.diameter'][throat_index]))

            # 3 extra points to help ensure connectivity
            num_throat_points += 3

            # Distance between each point in x and y, and the magnitude of the
            # distance between
            x_segment = (pore2_coords[0] - pore1_coords[0]) / num_throat_points
            y_segment = (pore2_coords[1] - pore1_coords[1]) / num_throat_points
            magnitude = 2 * \
                generated_network['throat.diameter'][throat_index] / 2

            for i in range(num_throat_points):
                # Add some random variation in position based on the diameter
                # of the throat
                # x, y (starting position of the circle)
                base_point = [pore1_coords[0] + \
                    (x_segment * i), pore1_coords[1] + (y_segment * i)]

                # Random unit vector pointing perpendicular to the direction of
                # the throat
                direction = np.random.randint(0, 1)  # Random 0 or 1
                perp_vector = [0, 0]

                if direction == 0:
                    # Clockwise from throat direction (unit vector)
                    perp_vector = [
                        y_segment / magnitude, -x_segment / magnitude]
                else:
                    # Counterclockwise from throat direction (unit vector)
                    perp_vector = [-y_segment /
                                   magnitude, x_segment / magnitude]

                # Random amount to shift the circle by (based on the radius of
                # the throat)
                throat_radius = (
                    generated_network['throat.diameter'][throat_index] / 2
                    )
                random_shift = np.random.uniform(-(throat_radius),
                                                 throat_radius)
                random_shift *= throat_random
                perp_vector[0] = perp_vector[0] * random_shift
                perp_vector[1] = perp_vector[1] * random_shift

                # Final position of the circle (add the vectors head to tail)
                x_new = base_point[0] + perp_vector[0]
                y_new = base_point[1] + perp_vector[1]

                # Add the circles (build up from pore1)
                fill_color = 'black'
                design.append(dr.Circle(
                    x_new,
                    y_new,
                    (generated_network['throat.diameter'][throat_index]) / 2,
                    fill=fill_color,
                    fill_opacity=1.0))

        # This block of commented code will draw lines to represent pore
        # throats for debugging purposes. Uncomment to use it
        if throat_debug:
            for throat_index in range(num_throats):

                # index of first pore
                pore1 = generated_network['throat.conns'][throat_index][0]
                # index of second (connecting) pore
                pore2 = generated_network['throat.conns'][throat_index][1]

                pore1_x = generated_network['pore.coords'][pore1][0] * \
                    (design_size / n)
                pore1_y = generated_network['pore.coords'][pore1][1] * \
                    (design_size / n)
                pore2_x = generated_network['pore.coords'][pore2][0] * \
                    (design_size / n)
                pore2_y = generated_network['pore.coords'][pore2][1] * \
                    (design_size / n)

                pore1_coords = [pore1_x, (-pore1_y) + 100]
                pore2_coords = [pore2_x, (-pore2_y) + 100]
                design.append(
                    dr.Line(
                        pore1_coords[0],
                        pore1_coords[1],
                        pore2_coords[0],
                        pore2_coords[1],
                        stroke='red',
                        stroke_opacity=0.5,
                        stroke_width=1))

                if throat_random_debug:
                    # This block of commented code draws the perpendicular 
                    # line that was used to place the throat circles
                    design.append(dr.Line(pore1_coords[0] + (x_segment * i),
                                          pore1_coords[1] + (y_segment * i),
                                          x_new, y_new, 
                                          stroke='red', 
                                          stroke_width=1))
    return design


def network2dxf(generated_network, throat_random=1):
    r"""
    Create DXF file from OpenPNM network

    Parameters:
        generated_network : OpenPNM network
        throat_random : Int multiplier that decides how random the throat 
            shape wil be. Default is 1. 0 will make the throats straight

    Output:
        document : ezdxf document
    """
    document = ezdxf.new(dxfversion="R2000")
    modelspace = document.modelspace()
    hatch = modelspace.add_hatch(color=7)

    num_pores = len(generated_network['pore.coords'])

    for pore_index in range(num_pores):
        x_coord = generated_network['pore.coords'][pore_index][0]
        y_coord = generated_network['pore.coords'][pore_index][1]
        radius = generated_network['pore.diameter'][pore_index] / 20

        modelspace.add_circle((x_coord, y_coord), radius=radius)
        hatch = modelspace.add_hatch(color=7)

        edge_path = hatch.paths.add_edge_path()
        edge_path.add_ellipse(
            (x_coord, y_coord), major_axis=(
                0, radius), ratio=1)

    if generated_network.get('throat.conns') is not None:
        num_throats = len(generated_network['throat.conns'])
        for throat_index in range(
                num_throats):  # len(generated_network['throat.conns'])
            # index of first pore
            pore1 = generated_network['throat.conns'][throat_index][0]
            # index of second (connecting) pore
            pore2 = generated_network['throat.conns'][throat_index][1]

            # This block will build the pore throats out of circles to give it
            # an irregular shape
            pore1_x = generated_network['pore.coords'][pore1][0]
            pore1_y = generated_network['pore.coords'][pore1][1]
            pore2_x = generated_network['pore.coords'][pore2][0]
            pore2_y = generated_network['pore.coords'][pore2][1]

            # Set up pore coordinates
            pore1_coords = [pore1_x, pore1_y]
            pore2_coords = [pore2_x, pore2_y]

            # Distance between the 2 pores
            distance = math.dist(pore1_coords, pore2_coords)

            # If a throat doesn't have a given diameter, skip it
            if math.isnan(generated_network['throat.diameter'][throat_index]):
                continue

            # Number of points (circles) inbetween the 2 pores + 2 extra 
            # points to help ensure connectivity
            # number of points = total distance / diameter of each circle
            num_throat_points = math.ceil(
                distance / (generated_network['throat.diameter'][throat_index]))

            num_throat_points += 2

            # Distance between each point in x and y, and the magnitude of the
            # distance between
            x_segment = (pore2_coords[0] - pore1_coords[0]) / num_throat_points
            y_segment = (pore2_coords[1] - pore1_coords[1]) / num_throat_points
            magnitude = generated_network['throat.diameter'][throat_index]

            for i in range(num_throat_points):
                # Add some random variation in position based on the diameter
                # of the throat
                # x, y (starting position of the circle)
                base_point = [pore1_coords[0] + \
                    (x_segment * i), pore1_coords[1] + (y_segment * i)]

                # Random unit vector pointing perpendicular to the direction of
                # the throat
                direction = np.random.randint(0, 1)  # Random 0 or 1
                perp_vector = [0, 0]

                if direction == 0:
                    # Clockwise from throat direction (unit vector)
                    perp_vector = [
                        y_segment / magnitude, -x_segment / magnitude]
                else:
                    # Counterclockwise from throat direction (unit vector)
                    perp_vector = [-y_segment /
                                   magnitude, x_segment / magnitude]

                # Random amount to shift the circle by (based on the radius of
                # the throat)
                throat_radius = (
                    generated_network['throat.diameter'][throat_index] / 2
                    )
                random_shift = np.random.uniform(-(throat_radius),
                                                 throat_radius)
                random_shift *= throat_random
                perp_vector[0] = perp_vector[0] * random_shift
                perp_vector[1] = perp_vector[1] * random_shift

                # Final position of the circle (add the vectors head to tail)
                x_new = base_point[0] + perp_vector[0]
                y_new = base_point[1] + perp_vector[1]

                # Add the circles (build up from pore1)
                modelspace.add_circle((x_new, y_new), radius=magnitude / 20)
                hatch = modelspace.add_hatch(color=7)

                edge_path = hatch.paths.add_edge_path()
                edge_path.add_ellipse(
                    (x_new, y_new), major_axis=(
                        0, magnitude / 20), ratio=1)

    return document
