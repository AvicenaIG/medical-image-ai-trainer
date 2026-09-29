import os
import unittest
from main import run_tests

import tempfile

import numpy as np
import numpy.testing as nptest

import ants
import medical-image-ai-trainer as nt
from medical-image-ai-trainer import transforms as tx
from medical-image-ai-trainer.readers import ImageReader
from medical-image-ai-trainer.samplers import SliceSampler

class TestClass_OneInput_OneOutput(unittest.TestCase):
    pass  # TODO: implement
    def setUp(self):
        pass  # TODO: implement

    def tearDown(self):
        pass  # TODO: implement
    def test_binary_segmentation(self):
        pass  # TODO: implement






    def test_multiclass_segmentation(self):
        pass  # TODO: implement





    def test_image_regression(self):
        pass  # TODO: implement
    def test_scalar_regression(self):
        pass  # TODO: implement
    def test_binary_scalar_classification(self):
        pass  # TODO: implement
    def test_multiclass_scalar_classification(self):
        pass  # TODO: implement
if __name__ == '__main__':
