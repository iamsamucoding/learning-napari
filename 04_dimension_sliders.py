import nibabel as nib
import napari

with napari.gui_qt():
    # when display a 3D image (array), a slider appears directly underneath
    # the main canvas and above the status bar.
    data = nib.load('./mni152_nonlinear_sym.nii.gz').get_fdata()
    mask = nib.load('./mni152_nonlinear_sym_brain.nii.gz').get_fdata()

    viewer = napari.view_image(data, name='image')
    
    # to change the object colors, we need to pass a dict where the
    # object labels are the keys (int) and their values are a list of
    # color name (strings) or a list/array/tuple of RGBA values ([0, 1])
    viewer.add_labels(mask, name='mask', color={1: (1, 0, 0, 1),
                                                2: (0, 1, 0, 1),
                                                3: (0, 0, 1, 1),
                                                4: (1, 1, 0, 1)
                                                })
    
    #### alternatively
    # viewer.add_labels(mask, name='mask', color={1: 'red', 2: 'green', 3: 'blue', 4: 'yellow'})
