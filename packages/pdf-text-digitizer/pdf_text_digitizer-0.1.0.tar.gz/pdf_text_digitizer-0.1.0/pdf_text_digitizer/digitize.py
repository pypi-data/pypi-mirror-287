# pdf_text_digitizer/digitize.py

import logging
from pdf_text_digitizer import utils, pdf_reader

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def digitize_pdf(file_path):
    if not utils.file_exists(file_path):
        logger.error(f"File {file_path} does not exist.")
        return None

    try:
        # Attempt to read the PDF as text-based
        pdf_text = pdf_reader.extract_text_from_pdf(file_path)
        if pdf_text.strip():
            logger.info("Successfully extracted text from PDF.")
            return pdf_text.strip()

        # If no text found, attempt to read the PDF as image-based
        logger.info("No text found in PDF, attempting OCR on images.")
        image_text = pdf_reader.extract_text_from_pdf_images(file_path)
        if image_text.strip():
            logger.info("Successfully extracted text from PDF images.")
            return image_text.strip()

        logger.warning("No text extracted from the PDF.")
        return None

    except Exception as e:
        logger.error(f"An error occurred while processing the PDF: {e}")
        return None

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Digitize text from a PDF file.")
    parser.add_argument('file_path', type=str, help="Path to the PDF file.")
    args = parser.parse_args()
    
    text = digitize_pdf(args.file_path)
    if text:
        print(text)
