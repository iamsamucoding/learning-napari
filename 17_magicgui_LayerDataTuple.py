from napari.types import ImageData, LayerDataTuple
import numpy as np
import napari
from magicgui import magicgui




# The most flexible return type annotation is napari.types.LayerDataTuple:
# it gives you full control over the layer that will be created and
# added to the viewer. (It also lets you update an existing layer
# with a matching name).

# A LayerDataTuple is a tuple in one of the following three forms:

# (layer_data,)
### a single item tuple containing only layer data (will be interpreted as an image).

# (layer_data, {})
### a 2-tuple of layer_data and a metadata dict. the keys in
# the metadata dict must be valid keyword arguments to the corresponding napari.layers.Layer 
# constructor.

# (layer_data, {}, 'layer_type')
### a 3-tuple of data, metadata, and layer type string.layer_type should be
# a lowercase string form of one of the layer types (like 'points', 'shapes', etc…).
# If omitted, the layer type is assumed to be 'image'.


@magicgui(call_button='Run Threshold')
def threshold(image: ImageData, threshold: int = 75) -> LayerDataTuple:
    """Threshold an image and return a mask."""
    thres_image = (image > threshold).astype(int)
    return (thres_image, {'name': 'output theshold'})



with napari.gui_qt():
    viewer = napari.view_image(np.random.randint(0, 100, (64, 64)))
    # put the panel in the left on the viewer
    viewer.window.add_dock_widget(threshold, area='left')
    # it calls the function that creates an image layer but here without
    # user interaction.
    # it just to have an initial image to display 
    threshold()
