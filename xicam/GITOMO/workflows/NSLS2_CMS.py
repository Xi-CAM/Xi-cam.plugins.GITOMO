from xicam.core.execution.workflow import Workflow
from xicam.core.execution.daskexecutor import DaskExecutor
# from xicam.plugins.Workflow import Workflow, DaskWorkflow
from xicam.Tomography.processing.read_APS2BM import read_APS2BM
from xicam.Tomography.processing.normalize import Normalize
from xicam.Tomography.processing.remove_outlier import RemoveOutlier
from xicam.Tomography.processing.array_max import ArrayMax
from xicam.Tomography.processing.minus_log import MinusLog
from xicam.Tomography.processing.retrieve_phase import RetrievePhase
from xicam.Tomography.processing.remove_stripe_fw import RemoveStripeFw
from xicam.Tomography.processing.pad import Pad
from xicam.Tomography.processing.angles import Angles
from xicam.Tomography.processing.recon import Recon
from xicam.Tomography.processing.crop import Crop
from xicam.Tomography.processing.array_divide import ArrayDivide
from xicam.Tomography.processing.circ_mask import CircMask
from xicam.Tomography.processing.write_tiff_stack import WriteTiffStack
from ..processing.readcropped import ReadCropped

import tomopy
import numpy as np


class Workflow(Workflow):
    def __init__(self):
        super(Workflow, self).__init__('NSLS-CMS')
        read = ReadCropped()

        gridrec = Recon()
        # padding.padded.connect(gridrec.tomo)
        # read.angles.connect(gridrec.theta)
        gridrec.filter_name.value = 'butterworth'
        gridrec.algorithm.value = 'gridrec'
        gridrec.center.value = np.array([500])  # 1295
        gridrec.filter_par.value = np.array([0.2, 2])
        # gridrec.sinogram_order.value = True

        writetiff = WriteTiffStack()

        for process in [read,
                        # gridrec
                        ]:
            self.addProcess(process)

        self.autoConnectAll()
