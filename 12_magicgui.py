from skimage import data
import napari
import numpy as np
from napari.layers import Image
from magicgui import magicgui
from skimage.color import rgb2gray


# If you annotate one of your function parameters as a Layer subclass
# (such as Image or Points), it will be rendered as a ComboBox widget
# (i.e. “dropdown menu”), where the options in the dropdown box are the
# layers of the corresponding type currently in the viewer.
#
# Only Image Layers are shown in the dropdown menu.
@magicgui(image={'label': 'Pick an Image'})
def my_widget(image: Image):
    print(image)
    print(type(image))
    print(image.data.shape)
    print()

with napari.gui_qt():
    viewer = napari.view_image(rgb2gray(data.astronaut()), name="Astronaut - Gray")
    viewer.add_image(data.astronaut(), rgb=True, name="Astronaut - RGB")
    points = [(100, 100), (200, 200), (300, 100)]
    viewer.add_points(points, size=30, name='points')


    viewer.window.add_dock_widget(my_widget)