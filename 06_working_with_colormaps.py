from skimage import data
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
    # assigning a color map to a gray image
    # the min and max value of the gray image are mapped to the
    # color map's bounds
    viewer = napari.view_image(data.moon(), colormap='viridis')
    