from napari.layers import Image
import numpy as np
import napari
from magicgui import magicgui


# creates a panel to pass the x and y sizes to create a new Image as a layer
@magicgui(call_button='Add Image')
def my_widget(ny: int=64, nx: int=64) -> Image:
    return Image(np.random.rand(ny, nx), name='My Image')



with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.window.add_dock_widget(my_widget, area='right')

		# it calls the function that creates an image layer but here without
		# user interaction.
		# it just to have an initial image to display 
    my_widget()
		