from skimage import data
import numpy as np
import napari

with napari.gui_qt():
    vertices = np.array([[0, 0], [0, 20], [10, 0], [10, 10]])
    faces = np.array([[0, 1, 2], [1, 2, 3]])
    values = np.linspace(0, 1, len(vertices))
    surface = (vertices, faces, values)

    viewer = napari.view_surface(surface)  # add the surface
    