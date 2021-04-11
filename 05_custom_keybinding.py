from skimage import data
import napari



with napari.gui_qt():
    viewer = napari.view_image(data.astronaut(), rgb=True)

    ################## KEYBINDINGS ##################

    # print the name of each layer on terminal
    @viewer.bind_key('p')
    def print_names(viewer):
        print([layer.name for layer in viewer.layers])
    

    # print the message "hello" on terminal during key pressing
    # (all instructions before the yield command)
    #
    # on key releasing, print the message 'goodbye' on terminal
    # (all instructions after the yield command)
    @viewer.bind_key('m')
    def print_message(viewer):
        print('hello')
        yield
        print('goodbye')
