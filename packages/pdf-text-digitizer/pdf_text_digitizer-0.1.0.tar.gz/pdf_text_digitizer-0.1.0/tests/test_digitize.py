# tests/test_digitize.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch
from pdf_text_digitizer.digitize import digitize_pdf

class TestDigitize(unittest.TestCase):

    @patch('pdf_text_digitizer.digitize.pdf_reader.extract_text_from_pdf')
    @patch('pdf_text_digitizer.digitize.pdf_reader.extract_text_from_pdf_images')
    @patch('pdf_text_digitizer.digitize.utils.file_exists', return_value=True)
    def test_digitize_pdf_text_based(self, mock_file_exists, mock_extract_images, mock_extract_text):
        mock_extract_text.return_value = "Sample text from PDF."
        result = digitize_pdf('dummy_path.pdf')
        self.assertEqual(result, "Sample text from PDF.")
        mock_extract_text.assert_called_once()
        mock_extract_images.assert_not_called()

    @patch('pdf_text_digitizer.digitize.pdf_reader.extract_text_from_pdf')
    @patch('pdf_text_digitizer.digitize.pdf_reader.extract_text_from_pdf_images')
    @patch('pdf_text_digitizer.digitize.utils.file_exists', return_value=True)
    def test_digitize_pdf_image_based(self, mock_file_exists, mock_extract_images, mock_extract_text):
        mock_extract_text.return_value = ""
        mock_extract_images.return_value = "Sample text from PDF images."
        result = digitize_pdf('dummy_path.pdf')
        self.assertEqual(result, "Sample text from PDF images.")
        mock_extract_text.assert_called_once()
        mock_extract_images.assert_called_once()

    @patch('pdf_text_digitizer.digitize.utils.file_exists', return_value=False)
    def test_digitize_pdf_file_not_exist(self, mock_file_exists):
        result = digitize_pdf('dummy_path.pdf')
        self.assertIsNone(result)
        mock_file_exists.assert_called_once()

if __name__ == '__main__':
    unittest.main()
