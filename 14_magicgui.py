from skimage import data
import napari
import numpy as np
from napari.types import ImageData
from magicgui import magicgui
from skimage.color import rgb2gray


# In the previous example, the object passed to your function will be the
# actual Layer instance, meaning you will need to access any attributes
# (like layer.data) on your own. If your function is designed to accept
# a numpy array, you can use any of the special <LayerType>Data types
# from napari.types to indicate that you only want the data attribute
# from the layer (where <LayerType> is one of the available layer types).
# Here’s an example using napari.types.ImageData
@magicgui()
def my_widget(array: ImageData):
    # note: it *may* be None! so your function should handle the null case
    if array is not None:
      assert isinstance(array, np.ndarray)  # it will be!

    print(array)
    print(type(array))
    print(array.shape)
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