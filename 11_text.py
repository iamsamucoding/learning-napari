from skimage import data
import napari

with napari.gui_qt():
    viewer = napari.view_image(data.astronaut(), rgb=True)


    text_parameters = {
        'text': 'number: {number}',
        'size': 12,
        'color': 'green',
        'anchor': 'upper_left',
        'translation': [-3, 0],
    }

    bounding_box = [[50, 50], [100, 50], [100, 100], [50, 100]]

    viewer.add_shapes(
        bounding_box,
        face_color='red',
        edge_color='green',
        properties={'number': [1, 2]},
        text=text_parameters,
        name='bounding box',
    )
    