from napari.types import ImageData, LayerDataTuple
import numpy as np
import napari
from pathlib import Path
from magicgui import magicgui
from skimage import io

python_code = ''

# https://github.com/GenevieveBuckley/magicgui/pull/1
# https://github.com/napari/magicgui/pull/23
#### https://github.com/napari/magicgui/issues/20#issuecomment-648312769
@magicgui(call_button='Load Image', filename={"filter": "Images (*.jpg *.jpeg *.png)"})
def image_filepicker(filename=Path()) -> LayerDataTuple:
    image = io.imread(filename)   
    return (image, {'name': 'main image'})

@magicgui(call_button='Load Python Code', filename={"filter": "Python (*.py)"})
def python_filepicker(filename=Path()):
    print('oioioi')
    global python_code
    python_code = filename


with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.window.add_dock_widget(image_filepicker, area='left')
    viewer.window.add_dock_widget(python_filepicker, area='left')

    # When call the function `python_filepicker`, the lambda function is called.
    # The event is an Event
    # event.source is a FunctionGui
    # We can get the value of a parameter from the function python_filepicker
    # by using event.source.filename.value
    python_filepicker.called.connect(lambda event: print(event.source.filename.value))
