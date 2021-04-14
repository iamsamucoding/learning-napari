from napari.types import ImageData, LayerDataTuple
import numpy as np
import napari
from pathlib import Path
from magicgui import magicgui
from skimage import io


# https://napari.org/magicgui/api/widgets.html#module-magicgui.widgets
# https://napari.org/magicgui/_autosummary/magicgui.widgets.Label.html#magicgui.widgets.Label
@magicgui(spin={'widget_type': 'SpinBox'},
          parameter={'widget_type': 'Label', 'tooltip': 'A nice tooltip'})
def custom_widget_type(spin, parameter='oioi oioi'):
    print('oioioi')


with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.window.add_dock_widget(custom_widget_type, area='left')
