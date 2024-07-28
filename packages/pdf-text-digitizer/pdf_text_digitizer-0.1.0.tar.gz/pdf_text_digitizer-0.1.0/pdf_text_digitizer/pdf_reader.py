# pdf_text_digitizer/pdf_reader.py

import PyPDF2
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import logging

logger = logging.getLogger(__name__)

def extract_text_from_page(pdf_reader, page_num):
    page = pdf_reader.pages[page_num]
    text = page.extract_text()
    if text:
        return text.strip()
    return None

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        if pdf_reader.is_encrypted:
            try:
                pdf_reader.decrypt('')
            except Exception as e:
                logger.error(f"Failed to decrypt PDF: {e}")
                return ""
        
        num_pages = len(pdf_reader.pages)
        logger.info(f"PDF has {num_pages} pages.")
        all_text = ""
        for page_num in range(num_pages):
            text = extract_text_from_page(pdf_reader, page_num)
            if text:
                all_text += text + "\n"
        
        return all_text

def extract_text_from_image(image):
    return pytesseract.image_to_string(image)

def extract_text_from_pdf_images(file_path):
    images = convert_from_path(file_path)
    all_text = ""
    for i, image in enumerate(images):
        logger.info(f"Processing page {i + 1} of {len(images)}")
        text = extract_text_from_image(image)
        if text:
            all_text += text + "\n"
    
    return all_text
