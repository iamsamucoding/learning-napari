from skimage import data
import napari

with napari.gui_qt():
    viewer = napari.Viewer()

    # each image is stacked on a layer list (it should be a layer stack =D)
    # we assign a label to each layer so that we can recover it easily later
    viewer.add_image(data.astronaut(), name='astronaut')
    viewer.add_image(data.moon(), name='moon')
    viewer.add_image(data.camera(), name='camera')

    # we can access the layers
    #
    #  viewer.layers[key]
    #
    # key can be the key/label assigned to the layer or
    # an index (integer value)
    #
    # `viewer.layers` has type LayerList, which is a list-like layer collection
    # with built-in reordering and callback hooks.

    # A layer with an image has the type: napari.layers.image.image.Image
    # or 'Image layer'

    # To remove a layer, just use:
    # viewer.layers.pop(i)

    # All these codes can be used in the built-in interactive terminal
    # of Napari, which already has all loaded data on memory

