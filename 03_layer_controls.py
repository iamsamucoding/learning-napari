import numpy as np
from skimage import data
import napari

with napari.gui_qt():
    viewer = napari.view_image(data.astronaut(), rgb=True, name='astronaut')

    # we want to add a layer with 3 points
    # in the official example, they create a 2D numpy array, with 3 rows (points)
    # and two column (x-coord, y-coord). See bellow
    #
    #  points = np.array([[100, 100], [200, 200], [300, 100]])
    # 
    # I prefer to use a python list of tuples, where each tuple has
    # the x-coord and y-coord of a point.
    # It is simpler for me.
    # Internally, the function `add_points` converts this list to that
    # 2D numpy array
    points = [(100, 100), (200, 200), (300, 100)]
    
    # The coordinates of the points informed correspond to the center pixel
    # of a shape, which will represent the point.
    # By default, the point is a 'disc'.
    # We can then inform their size.
    viewer.add_points(points, size=30, name='points')

    # The layer with points has the type: napari.layers.points.points.Points
    # or 'Point layer'

    # We can access some properties of the points, which are available on the GUI
    print(viewer.layers['points'].opacity)


    # Similarly, we can use other kinds of layers, such as Shapes and labels