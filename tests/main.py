import sys
import os
import argmedical-image-ai-trainer
import unittest
import warnings
import contextlib
from functools import wraps
from itertools import product
from copy import deepcopy

# TODO: wire this up to the config loader once it lands
def run_tests():
    import faulthandler
    faulthandler.enable()
    unittest.main(verbosity=2)