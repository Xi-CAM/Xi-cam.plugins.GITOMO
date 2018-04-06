#! /usr/bin/env python
# -*- coding: utf-8 -*-

from xicam.plugins import ProcessingPlugin, Input, Output
import tomopy
import numpy as np
from typing import List
import fabio

class ReadCropped(ProcessingPlugin):
    """
    Return uniformly distributed projection angles in radian.
    """
    paths = Input(description='List of paths', type=List[str])
    pxmin = Input(description='start x pixel', type=int)
    pxmax = Input(description='stop x pixel', type=int)
    pxstep = Input(description='step of x pixel', type=int)
    pzmin = Input(description='min z pixel', type=int)
    pzmax = Input(description='max z pixel', type=int)
    tomo = Output(description='3D array of tomograms (''projection'' first)')
    angles = Output(description='angle')

    def evaluate(self):
        frames = []
        for f in self.paths.value:
            frames.append(fabio.open(f).data[np.arange(self.pxmin.value, self.pxmax.value, self.pxstep.value),self.pzmin.value:self.pzmax.value])
        self.tomo.value = np.array(frames)
        self.angles.value = np.linspace(0,180, len(self.paths.value))
