import numpy as np
from skimage import data
import napari

with napari.gui_qt():
    viewer = napari.view_image(data.astronaut(), rgb=True, name='astronaut')
    points = [(100, 100), (200, 200), (300, 100)]
    viewer.add_points(points, size=30, name='points')

    # return all points (nd array) from the layer 'points'
    print(viewer.layers['points'].data)
