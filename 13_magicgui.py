from skimage import data
import napari
import numpy as np
from napari.layers import Layer
from magicgui import magicgui
from skimage.color import rgb2gray


# In the previous example, the dropdown menu will only show Image layers,
# because the parameter was annotated as an Image. If you’d like a
# dropdown menu that allows the user to pick from all layers in the
# layer list, annotate your parameter as Layer
@magicgui(layer={'label': 'Pick a Layer'})
def my_widget(layer: Layer):
    print(layer)
    print(type(layer))
    print(layer.data.shape)
    print()


with napari.gui_qt():
    image = data.astronaut()
    gray_image = rgb2gray(image)
    label_image = np.zeros(gray_image.shape, dtype=np.int)
    label_image[200:350, 200:350] = 1

    viewer = napari.view_image(gray_image, name="Astronaut - Gray")
    viewer.add_image(image, rgb=True, name="Astronaut - RGB")
    viewer.add_labels(label_image, name="Label Layer")
    points = [(100, 100), (200, 200), (300, 100)]
    viewer.add_points(points, size=30, name='points')


    viewer.window.add_dock_widget(my_widget)