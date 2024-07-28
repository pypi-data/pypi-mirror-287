# tests/test_pdf_reader.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch, mock_open, MagicMock
from pdf_text_digitizer import pdf_reader, utils

class TestPdfReader(unittest.TestCase):

    @patch('pdf_text_digitizer.pdf_reader.PyPDF2.PdfReader')
    def test_extract_text_from_page(self, MockPdfReader):
        mock_pdf_reader = MockPdfReader.return_value
        mock_pdf_reader.pages = [MagicMock()]
        mock_pdf_reader.pages[0].extract_text.return_value = "Sample text from page."

        text = pdf_reader.extract_text_from_page(mock_pdf_reader, 0)
        self.assertEqual(text, "Sample text from page.")

    @patch('pdf_text_digitizer.pdf_reader.PyPDF2.PdfReader')
    @patch('pdf_text_digitizer.utils.file_exists', return_value=True)
    @patch('builtins.open', new_callable=mock_open, read_data="PDF content")
    def test_extract_text_from_pdf(self, mock_open, mock_file_exists, MockPdfReader):
        mock_pdf_reader = MockPdfReader.return_value
        mock_pdf_reader.pages = [MagicMock()]
        mock_pdf_reader.pages[0].extract_text.return_value = "Sample text from PDF."

        text = pdf_reader.extract_text_from_pdf('dummy_path.pdf')
        self.assertEqual(text.strip(), "Sample text from PDF.")

    @patch('pdf_text_digitizer.pdf_reader.convert_from_path')
    @patch('pdf_text_digitizer.pdf_reader.pytesseract.image_to_string', return_value="Sample text from PDF images.")
    @patch('pdf_text_digitizer.utils.file_exists', return_value=True)
    def test_extract_text_from_pdf_images(self, mock_file_exists, mock_image_to_string, mock_convert_from_path):
        mock_convert_from_path.return_value = [MagicMock()]

        text = pdf_reader.extract_text_from_pdf_images('dummy_path.pdf')
        self.assertEqual(text.strip(), "Sample text from PDF images.")

if __name__ == '__main__':
    unittest.main()
