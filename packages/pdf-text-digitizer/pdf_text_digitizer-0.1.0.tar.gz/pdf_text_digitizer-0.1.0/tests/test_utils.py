# tests/test_utils.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from pdf_text_digitizer import utils
import os

class TestUtils(unittest.TestCase):

    def test_file_exists(self):
        self.assertTrue(utils.file_exists(__file__))
        self.assertFalse(utils.file_exists('non_existing_file.txt'))

if __name__ == '__main__':
    unittest.main()
