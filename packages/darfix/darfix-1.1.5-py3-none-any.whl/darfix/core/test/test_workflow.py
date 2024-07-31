__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "08/12/2020"


import unittest
import shutil
import tempfile

import numpy

try:
    import scipy
except ImportError:
    scipy = None

from darfix.test import utils
from darfix.core import imageOperations, imageRegistration, roi


@unittest.skipUnless(scipy, "scipy is missing")
class TestWorkflow(unittest.TestCase):
    """Tests different workflows"""

    def setUp(self):
        self._dir = tempfile.mkdtemp()
        first_frame = numpy.zeros((100, 100))
        # Simulating a series of frame with information in the middle.
        first_frame[25:75, 25:75] = numpy.random.randint(50, 300, size=(50, 50))
        background = [
            numpy.random.randint(-5, 5, size=(100, 100), dtype="int16")
            for i in range(5)
        ]
        data = [first_frame]
        shift = [1.0, 0]
        for i in range(9):
            data += [
                numpy.fft.ifftn(
                    scipy.ndimage.fourier_shift(numpy.fft.fftn(data[-1]), shift)
                ).real
            ]
        data = numpy.asanyarray(data, dtype=numpy.int16)
        self.dataset = utils.createDataset(data=data, _dir=self._dir, backend="edf")
        self.dark_dataset = utils.createDataset(
            data=background, _dir=self._dir, backend="edf"
        )

    def test_workflow0(self):
        """Tests a possible workflow"""

        expected = numpy.subtract(
            self.dataset.data[:, 49:52, 50:51],
            numpy.median(self.dark_dataset.data[:, 49:52, 50:51], axis=0).astype(
                numpy.int16
            ),
            dtype=numpy.int64,
        ).astype(numpy.int16)
        expected[expected > 20] = 0
        expected[expected < 1] = 0
        # ROI of the data
        data = roi.apply_3D_ROI(
            self.dataset.data,
            size=[3, 3],
            center=(numpy.array(self.dataset.data[0].shape) / 2).astype(int),
        )

        # ROI of the dark frames
        dark_frames = roi.apply_3D_ROI(
            numpy.array(self.dark_dataset.data),
            size=[3, 3],
            center=(numpy.array(self.dark_dataset.data[0].shape) / 2).astype(int),
        )

        # Background substraction of the data
        data = imageOperations.background_subtraction(
            data, dark_frames, method="median"
        )
        # ROI of the data
        data = roi.apply_3D_ROI(
            data, size=[3, 1], center=(numpy.array(data[0].shape) / 2).astype(int)
        )
        # Threshold removal of the data
        data = imageOperations.threshold_removal(data, 1, 20)
        numpy.testing.assert_array_equal(data, expected)

    def test_workflow1(self):
        """Tests a possible workflow"""

        first_frame = numpy.asarray(self.dataset.data[0])
        expected = (
            numpy.tile(first_frame, (10, 1))
            .reshape(10, 100, 100)[:, 25:75, 25:75]
            .astype(numpy.float32)
        )
        # Detect the shift
        optimal_shift = imageRegistration.shift_detection(self.dataset.data, 2)
        data = imageRegistration.shift_correction(self.dataset.data, optimal_shift)

        # ROI of the data
        data = roi.apply_3D_ROI(
            data,
            size=[50, 50],
            center=(numpy.array(self.dataset.data[0].shape) / 2).astype(int),
        )

        numpy.testing.assert_allclose(
            data[0, 0:10, 0:10], expected[0, 0:10, 0:10], rtol=0.1
        )

    def tearDown(self):
        shutil.rmtree(self._dir)


if __name__ == "__main__":
    unittest.main()
