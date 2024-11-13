"""Creating an SDF grid"""
import numpy as np


def sdf_grid(sdf_function, resolution):
    """
    Create an occupancy grid at the specified resolution given the implicit representation.
    :param sdf_function: A function that takes in a point (x, y, z) and returns the sdf at the given point.
    Points may be provides as vectors, i.e. x, y, z can be scalars or 1D numpy arrays, such that (x[0], y[0], z[0])
    is the first point, (x[1], y[1], z[1]) is the second point, and so on
    :param resolution: Resolution of the occupancy grid
    :return: An SDF grid of specified resolution (i.e. an array of dim (resolution, resolution, resolution) with positive values outside the shape and negative values inside.
    """
   
    # ###############
    # TODO: Implement
    ## create a 3D grid 
    x = np.linspace(-1, 1, resolution) # x coordinates of the grid
    y = np.linspace(-1, 1, resolution) # y coordinates of the grid
    z = np.linspace(-1, 1, resolution) # z coordinates of the grid
    
    
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
    
    points_x = X.flatten()
    points_y = Y.flatten()
    points_z = Z.flatten()
    
    sdf_values = sdf_function(points_x, points_y, points_z)
    
    sdf_values = sdf_values.reshape(resolution, resolution, resolution)
                
    return np.array(sdf_values)
    
    ###############
