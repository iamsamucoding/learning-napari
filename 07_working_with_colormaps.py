import numpy as np
from vispy.color import Colormap
import napari

##### color maps
# PiYG
# blue
# cyan
# gist_earth
# gray
# green
# hsv
# inferno
# magma
# magenta
# plasma
# red
# turbo
# twilight
# twilight_shifted
# yellow
# viridis


with napari.gui_qt():
    cmap = Colormap([[1, 0, 0], [0, 0, 0], [0, 0, 1]])
    image = np.random.random((100, 100))

    viewer = napari.view_image(image, colormap=('diverging', cmap))
    