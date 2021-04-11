from napari.types import ImageData, LayerDataTuple
import numpy as np
import napari
from magicgui import magicgui




# The default behavior is to add a new layer to the viewer for each
# LayerDataTuple returned by a magicgui function. By providing a unique
# name key in your LayerDataTuple metadata dict, you can update an
# existing layer, rather than creating a new layer each time the
# function is called:


@magicgui(call_button='Make Points', n_points={'maximum': 200})
def make_points(n_points=40) -> napari.types.LayerDataTuple:
  data = 500 * np.random.rand(n_points, 2)
  return (data, {'name': 'My Points'}, 'points')



with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.window.add_dock_widget(make_points)
    # calling this multiple times will just update 'My Points'
    make_points()
    make_points.n_points.value = 80
    make_points()
    make_points.n_points.value = 120
    make_points()