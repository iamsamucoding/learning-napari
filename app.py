#!/usr/bin/env python3

import sys
import os
import napari
import numpy as np
import nibabel as nib
from magicgui import magicgui
from pyift.shortestpath import seed_competition


def segment(viewer):
    markers = viewer.layers['markers'].data
    image = viewer.layers['image'].data
    costs, _, _, labels, = seed_competition(markers, image, image_3d=True)
    costs /= costs.max()
    viewer.layers['labels'].data = labels
    viewer.layers['path-value'].data = costs


def save_markers(viewer, path):
    if path == '':
        path = 'markers.txt'

    markers = viewer.layers['markers'].data
    obj_markers = np.where(markers == 2)
    bkg_markers = np.where(markers == 1)

    with open(path, 'w') as f:
        # TODO
        # - salvar no formato da ift
        # - nao verifiquei a ordem

        for z, y, x in zip(*obj_markers):
            f.write(f'{z} {y} {x} {1}\n')

        for z, y, x in zip(*bkg_markers):
            f.write(f'{z} {y} {x} {0}\n')


def main(args):
    image = nib.load(args[1]).get_fdata()
    with napari.gui_qt():
        viewer = napari.view_image(image)
        blank = np.zeros(image.shape, dtype=np.int)
        viewer.add_image(blank, name='path-value', visible=False, opacity=0.5)
        viewer.add_labels(blank, name='labels', opacity=0.5)
        viewer.add_labels(blank, name='markers', opacity=1)

        # @magicgui(call_button='Segment')
        # def _segment():
        #     segment(viewer)
            
        # @magicgui(call_button='Save Markers')
        # def _save_markers(path: str):
        #     save_markers(viewer, path)

        # viewer.window.add_dock_widget([_segment, _save_markers], area='left')
        viewer.window.add_dock_widget([], area='left')


if __name__ == '__main__':
    main(sys.argv)

