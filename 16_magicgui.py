from napari.types import LabelsData, ImageData
import numpy as np
import napari
from magicgui import magicgui


# it creates a panel with a dropdown menu showing the image layers, an integer field,
# and a button to run this function.
# Then, the function receives the data of the select image layer, return
# the data of an output image, after a threshold, that is converted to a LabelsData.
# This LabelsData creates a LabelsLayer in the viewer with the default name: 'threshold result',
# where `threshold is the corresponding function name`
@magicgui(call_button='Run Threshold')
def threshold(image: ImageData, threshold: int = 75) -> LabelsData:
    """Threshold an image and return a mask."""
    return (image > threshold).astype(int)



with napari.gui_qt():
    viewer = napari.view_image(np.random.randint(0, 100, (64, 64)))
    viewer.window.add_dock_widget(threshold)
    # it calls the function that creates an image layer but here without
    # user interaction.
    # it just to have an initial image to display 
    threshold()
