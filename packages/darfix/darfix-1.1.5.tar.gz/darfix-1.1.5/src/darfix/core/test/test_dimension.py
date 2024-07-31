__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "30/11/2020"


import unittest
import numpy
import tempfile
import shutil

from darfix.test import utils
from darfix.core.dataset import Dataset, Data
from darfix.core.dimension import Dimension, POSITIONER_METADATA


class TestDimension(unittest.TestCase):
    """Tests for class Dimension in `dimension.py`"""

    def setUp(self):
        """ "
        Creating random dataset with specific headers.
        """
        self._dir = tempfile.mkdtemp()
        counter_mne = "a b c d e f g h"
        motor_mne = "obpitch y z mainx ffz m obx"
        dims = (20, 100, 100)
        # Create headers
        header = []
        # Dimensions for reshaping
        a = numpy.random.rand(2)
        b = numpy.random.rand(5)
        c = numpy.random.rand(2)
        motors = numpy.random.rand(7)
        for i in numpy.arange(20):
            header.append({})
            header[i]["HeaderID"] = i
            header[i]["counter_mne"] = counter_mne
            header[i]["motor_mne"] = motor_mne
            header[i]["counter_pos"] = ""
            header[i]["motor_pos"] = ""
            for count in counter_mne:
                header[i]["counter_pos"] += str(numpy.random.rand(1)[0]) + " "
            for j, m in enumerate(motor_mne.split()):
                if m == "z":
                    header[i]["motor_pos"] += (
                        str(a[int((i > 4 and i < 10) or i > 14)]) + " "
                    )
                elif m == "m":
                    header[i]["motor_pos"] += str(b[i % 5]) + " "
                elif m == "obpitch":
                    header[i]["motor_pos"] += str(c[int(i > 9)]) + " "
                elif m == "mainx":
                    header[i]["motor_pos"] += "50 "
                else:
                    header[i]["motor_pos"] += str(motors[j]) + " "

        data = numpy.zeros(dims)
        background = numpy.random.random(dims)
        idxs = [0, 2, 4]
        data[idxs] += background[idxs]
        self.in_memory_dataset = utils.createDataset(
            data=data, header=header, _dir=self._dir, backend="edf"
        )
        self.on_disk_dataset = utils.createDataset(
            data=data, header=header, _dir=self._dir, in_memory=False, backend="edf"
        )

    def test_add_one_dimension(self):
        """Tests the correct add of a dimension"""

        dimension = Dimension(POSITIONER_METADATA, "test", 20)
        # In memory
        self.in_memory_dataset.add_dim(0, dimension)
        saved_dimension = self.in_memory_dataset.dims.get(0)
        self.assertEqual(saved_dimension.name, "test")
        self.assertEqual(saved_dimension.kind, POSITIONER_METADATA)
        self.assertEqual(saved_dimension.size, 20)

        # On disk
        self.on_disk_dataset.add_dim(0, dimension)
        saved_dimension = self.on_disk_dataset.dims.get(0)
        self.assertEqual(saved_dimension.name, "test")
        self.assertEqual(saved_dimension.kind, POSITIONER_METADATA)
        self.assertEqual(saved_dimension.size, 20)

    def test_add_several_dimensions(self):
        """Tests the correct add of several dimensions"""

        dimension1 = Dimension(POSITIONER_METADATA, "test1", 20)
        dimension2 = Dimension(POSITIONER_METADATA, "test2", 30)
        dimension3 = Dimension(POSITIONER_METADATA, "test3", 40)

        # In memory
        self.in_memory_dataset.add_dim(0, dimension1)
        self.in_memory_dataset.add_dim(1, dimension2)
        self.in_memory_dataset.add_dim(2, dimension3)
        self.assertEqual(self.in_memory_dataset.dims.ndim, 3)

        # On disk
        self.on_disk_dataset.add_dim(0, dimension1)
        self.on_disk_dataset.add_dim(1, dimension2)
        self.on_disk_dataset.add_dim(2, dimension3)
        self.assertEqual(self.on_disk_dataset.dims.ndim, 3)

    def test_remove_dimension(self):
        """Tests the correct removal of a dimension"""

        dimension = Dimension(POSITIONER_METADATA, "test", 20)

        # In memory
        self.in_memory_dataset.add_dim(0, dimension)
        self.in_memory_dataset.remove_dim(0)
        self.assertEqual(self.in_memory_dataset.dims.ndim, 0)

        # On disk
        self.on_disk_dataset.add_dim(0, dimension)
        self.on_disk_dataset.remove_dim(0)
        self.assertEqual(self.on_disk_dataset.dims.ndim, 0)

    def test_remove_dimensions(self):
        """Tests the correct removal of several dimensions"""

        dimension1 = Dimension(POSITIONER_METADATA, "test1", 20)
        dimension2 = Dimension(POSITIONER_METADATA, "test2", 30)
        dimension3 = Dimension(POSITIONER_METADATA, "test3", 40)

        # In memory
        self.in_memory_dataset.add_dim(0, dimension1)
        self.in_memory_dataset.add_dim(1, dimension2)
        self.in_memory_dataset.add_dim(2, dimension3)
        self.in_memory_dataset.remove_dim(0)
        self.in_memory_dataset.remove_dim(2)
        self.assertEqual(self.in_memory_dataset.dims.ndim, 1)
        self.assertEqual(self.in_memory_dataset.dims.get(1).name, "test2")

        # On disk
        self.on_disk_dataset.add_dim(0, dimension1)
        self.on_disk_dataset.add_dim(1, dimension2)
        self.on_disk_dataset.add_dim(2, dimension3)
        self.on_disk_dataset.remove_dim(0)
        self.on_disk_dataset.remove_dim(2)
        self.assertEqual(self.on_disk_dataset.dims.ndim, 1)
        self.assertEqual(self.on_disk_dataset.dims.get(1).name, "test2")

    def test_find_dimensions(self):
        """Tests the correct finding of the dimensions"""

        # In memory
        self.in_memory_dataset.find_dimensions(POSITIONER_METADATA)
        self.assertEqual(self.in_memory_dataset.dims.ndim, 3)
        self.assertEqual(self.in_memory_dataset.dims.get(0).name, "m")
        self.assertEqual(self.in_memory_dataset.dims.get(1).name, "z")
        self.assertEqual(self.in_memory_dataset.dims.get(2).name, "obpitch")

        # On disk
        self.on_disk_dataset.find_dimensions(POSITIONER_METADATA)
        self.assertEqual(self.on_disk_dataset.dims.ndim, 3)
        self.assertEqual(self.on_disk_dataset.dims.get(0).name, "m")
        self.assertEqual(self.on_disk_dataset.dims.get(1).name, "z")
        self.assertEqual(self.on_disk_dataset.dims.get(2).name, "obpitch")

    def test_reshaped_data(self):
        """Tests the correct reshaping of the data"""

        # In memory
        self.in_memory_dataset.find_dimensions(POSITIONER_METADATA)
        dataset = self.in_memory_dataset.reshape_data()
        self.assertEqual(dataset.data.shape, (2, 2, 5, 100, 100))

        # On disk
        self.on_disk_dataset.find_dimensions(POSITIONER_METADATA)
        dataset = self.on_disk_dataset.reshape_data()
        self.assertEqual(dataset.data.shape, (2, 2, 5, 100, 100))

    def test_find_shift(self):
        """Tests the shift detection with dimensions and indices"""

        # In memory
        self.in_memory_dataset.find_dimensions(POSITIONER_METADATA)
        dataset = self.in_memory_dataset.reshape_data()
        indices = [1, 2, 3, 4]
        shift = dataset.find_shift(dimension=[1, 1], indices=indices)
        self.assertEqual(len(shift), 0)
        shift = dataset.find_shift(dimension=[0, 1], indices=indices)
        self.assertEqual(shift.shape, (2, 1))

        # On disk
        self.on_disk_dataset.find_dimensions(POSITIONER_METADATA)
        dataset = self.on_disk_dataset.reshape_data()
        indices = [1, 2, 3, 4]
        shift = dataset.find_shift(dimension=[1, 1], indices=indices)
        self.assertEqual(len(shift), 0)
        shift = dataset.find_shift(dimension=[0, 1], indices=indices)
        self.assertEqual(shift.shape, (2, 1))

    def test_apply_shift(self):
        """Tests the shift correction with dimensions and indices"""

        # In memory
        self.in_memory_dataset.find_dimensions(POSITIONER_METADATA)
        dataset = self.in_memory_dataset.reshape_data()
        new_dataset = dataset.apply_shift(
            shift=numpy.array([[0, 0.5], [0, 0.5]]),
            dimension=[0, 1],
            indices=[1, 2, 3, 4],
        )
        self.assertEqual(new_dataset.data.urls[0, 0, 0], dataset.data.urls[0, 0, 0])
        self.assertNotEqual(new_dataset.data.urls[0, 0, 1], dataset.data.urls[0, 0, 1])

        #  On disk
        self.on_disk_dataset.find_dimensions(POSITIONER_METADATA)
        dataset = self.on_disk_dataset.reshape_data()
        new_dataset = dataset.apply_shift(
            shift=numpy.array([[0, 0.5], [0, 0.5]]),
            dimension=[0, 1],
            indices=[1, 2, 3, 4],
        )

        self.assertEqual(new_dataset.data.urls[0, 0, 0], dataset.data.urls[0, 0, 0])
        self.assertNotEqual(new_dataset.data.urls[0, 0, 1], dataset.data.urls[0, 0, 1])

    def test_find_shift_along_dimension(self):
        """Tests the shift detection along a dimension"""

        # In memory
        self.in_memory_dataset.find_dimensions(POSITIONER_METADATA)
        dataset = self.in_memory_dataset.reshape_data()
        indices = numpy.arange(10)
        shift = dataset.find_shift_along_dimension(dimension=[1], indices=indices)
        self.assertEqual(shift.shape, (2, 2, 5))
        shift = dataset.find_shift_along_dimension(dimension=[0], indices=indices)
        self.assertEqual(shift.shape, (5, 2, 2))

        # On disk
        self.on_disk_dataset.find_dimensions(POSITIONER_METADATA)
        dataset = self.on_disk_dataset.reshape_data()
        indices = numpy.arange(10)
        shift = dataset.find_shift_along_dimension(dimension=[1], indices=indices)
        self.assertEqual(shift.shape, (2, 2, 5))
        shift = dataset.find_shift_along_dimension(dimension=[0], indices=indices)
        self.assertEqual(shift.shape, (5, 2, 2))

    def test_apply_shift_along_dimension(self):
        """Tests the shift correction with dimensions and indices"""

        # In memory
        self.in_memory_dataset.find_dimensions(POSITIONER_METADATA)
        dataset = self.in_memory_dataset.reshape_data()
        shift = numpy.random.random((4, 2, 2))
        new_dataset = dataset.apply_shift_along_dimension(
            shift=shift, dimension=[1], indices=[1, 2, 3, 4]
        )
        self.assertEqual(new_dataset.data.urls[0, 0, 0], dataset.data.urls[0, 0, 0])
        self.assertNotEqual(new_dataset.data.urls[0, 0, 1], dataset.data.urls[0, 0, 1])
        #  On disk
        self.on_disk_dataset.find_dimensions(POSITIONER_METADATA)
        dataset = self.on_disk_dataset.reshape_data()
        shift = numpy.random.random((4, 2, 2))
        new_dataset = dataset.apply_shift_along_dimension(
            shift=shift, dimension=[1], indices=[1, 2, 3, 4]
        )

        self.assertEqual(new_dataset.data.urls[0, 0, 0], dataset.data.urls[0, 0, 0])
        self.assertNotEqual(new_dataset.data.urls[0, 0, 1], dataset.data.urls[0, 0, 1])

    def test_zsum(self):
        """Tests the shift detection with dimensions and indices"""

        indices = [1, 2, 3, 6]
        # In memory
        self.in_memory_dataset.find_dimensions(POSITIONER_METADATA)
        dataset = self.in_memory_dataset.reshape_data()
        result = numpy.sum(dataset.get_data(dimension=[0, 1], indices=indices), axis=0)
        zsum = dataset.zsum(dimension=[0, 1], indices=indices)
        numpy.testing.assert_array_equal(zsum, result)

        # On disk
        self.on_disk_dataset.find_dimensions(POSITIONER_METADATA)
        dataset = self.on_disk_dataset.reshape_data()
        zsum = dataset.zsum(dimension=[0, 1], indices=indices)
        numpy.testing.assert_array_equal(zsum, result)

    def test_apply_2d_fit(self):
        """Tests the fit with dimensions and indices"""

        # In memory
        data = Data(
            urls=self.in_memory_dataset.get_data().urls[:10],
            metadata=self.in_memory_dataset.get_data().metadata[:10],
            in_memory=True,
        )
        dataset = Dataset(_dir=self.in_memory_dataset.dir, data=data)
        dataset.find_dimensions(POSITIONER_METADATA)
        dataset = dataset.reshape_data()
        new_dataset, maps = dataset.apply_fit(indices=[1, 2, 3, 4])
        self.assertEqual(new_dataset.data.urls[0, 0], dataset.data.urls[0, 0])
        self.assertNotEqual(new_dataset.data.urls[0, 1], dataset.data.urls[0, 1])
        self.assertEqual(len(maps), 7)
        self.assertEqual(maps[0].shape, self.in_memory_dataset.get_data(0).shape)

        #  On disk
        data = Data(
            urls=self.on_disk_dataset.get_data().urls[:10],
            metadata=self.on_disk_dataset.get_data().metadata[:10],
            in_memory=False,
        )
        dataset = Dataset(_dir=self.on_disk_dataset.dir, data=data)
        dataset.find_dimensions(POSITIONER_METADATA)
        dataset = dataset.reshape_data()
        new_dataset, maps = dataset.apply_fit(indices=[1, 2, 3, 4])

        self.assertEqual(new_dataset.data.urls[0, 0], dataset.data.urls[0, 0])
        self.assertNotEqual(new_dataset.data.urls[0, 1], dataset.data.urls[0, 1])
        self.assertEqual(len(maps), 7)
        self.assertEqual(maps[0].shape, self.in_memory_dataset.get_data(0).shape)

    def test_data_reshaped_data(self):
        """Tests that data and reshaped data have same values"""

        # In memory
        self.in_memory_dataset.find_dimensions(POSITIONER_METADATA)
        dataset = self.in_memory_dataset.reshape_data()
        numpy.testing.assert_array_equal(
            dataset.get_data(0), self.in_memory_dataset.get_data(0)
        )

        # On disk
        self.on_disk_dataset.find_dimensions(POSITIONER_METADATA)
        dataset = self.on_disk_dataset.reshape_data()
        numpy.testing.assert_array_equal(
            dataset.get_data(0), self.on_disk_dataset.get_data(0)
        )

    def test_clear_dimensions(self):
        """Tests the clear dimensions function"""

        # In memory
        self.in_memory_dataset.find_dimensions(POSITIONER_METADATA)
        self.in_memory_dataset.clear_dims()
        self.assertEqual(self.in_memory_dataset.dims.ndim, 0)

        # On disk
        self.on_disk_dataset.find_dimensions(POSITIONER_METADATA)
        self.on_disk_dataset.clear_dims()
        self.assertEqual(self.on_disk_dataset.dims.ndim, 0)

    def test_apply_moments_in_memory(self):
        """Tests finding moments"""

        # In memory
        self.in_memory_dataset.find_dimensions(POSITIONER_METADATA)
        dataset = self.in_memory_dataset.reshape_data()
        moments = dataset.apply_moments(indices=[1, 2, 3, 4])
        self.assertEqual(moments[0][0].shape, dataset.get_data(0).shape)
        self.assertEqual(moments[1][3].shape, dataset.get_data(0).shape)

        #  On disk
        self.on_disk_dataset.find_dimensions(POSITIONER_METADATA)
        dataset = self.on_disk_dataset.reshape_data()
        moments = dataset.apply_moments(indices=[1, 2, 3, 4])
        self.assertEqual(moments[0][0].shape, dataset.get_data(0).shape)
        self.assertEqual(moments[1][3].shape, dataset.get_data(0).shape)

    def test_compute_magnification(self):
        """Tests fitting data in memory"""

        # In memory
        self.in_memory_dataset.find_dimensions(POSITIONER_METADATA)
        dataset = self.in_memory_dataset.reshape_data()
        dataset.compute_transformation(d=0.1)
        self.assertEqual(dataset.transformation.shape, dataset.get_data(0).shape)

        #  On disk
        self.on_disk_dataset.find_dimensions(POSITIONER_METADATA)
        dataset = self.on_disk_dataset.reshape_data()
        dataset.compute_transformation(d=0.1)
        self.assertEqual(dataset.transformation.shape, dataset.get_data(0).shape)

    def tearDown(self):
        shutil.rmtree(self._dir)
