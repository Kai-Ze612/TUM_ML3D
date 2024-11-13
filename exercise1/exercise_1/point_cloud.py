"""Triangle Meshes to Point Clouds"""
import numpy as np


def sample_point_cloud(vertices, faces, n_points):
    """
    Sample n_points uniformly from the mesh represented by vertices and faces
    :param vertices: Nx3 numpy array of mesh vertices
    :param faces: Mx3 numpy array of mesh faces
    :param n_points: number of points to be sampled
    :return: sampled points, a numpy array of shape (n_points, 3)
    """

    # ###############
    # TODO: Implement
    
    ## To get triangle vertices
    triangles = vertices[faces]
    
    v0 = triangles[:, 0]
    v1 = triangles[:, 1]
    v2 = triangles[:, 2]
    
    ## Calculate the area of each triangle
    areas = np.linalg.norm(np.cross(v1 - v0, v2 - v0), axis=1) / 2
    total_area = np.sum(areas)
    
    probs = areas / total_area
    
    triangle_indices = np.random.choice(len(areas), size=n_points, p=probs)
    
    r1 = np.random.rand(n_points)
    r2 = np.random.rand(n_points)
    
    sqrt_r1 = np.sqrt(r1)
    
    b0 = 1 - sqrt_r1
    b1 = sqrt_r1 * (1 - r2)
    b2 = sqrt_r1 * r2
    
    selected_triangles = triangles[triangle_indices]
    
    points = (b0[:, np.newaxis] * selected_triangles[:, 0] +
             b1[:, np.newaxis] * selected_triangles[:, 1] +
             b2[:, np.newaxis] * selected_triangles[:, 2])
    
    return points
    # ###############
