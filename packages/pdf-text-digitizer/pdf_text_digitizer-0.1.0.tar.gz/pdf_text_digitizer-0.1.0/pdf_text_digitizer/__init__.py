# pdf_text_digitizer/__init__.py

from .digitize import digitize_pdf
from . import utils
from . import pdf_reader
from .config import Config

__all__ = ['digitize_pdf', 'utils', 'pdf_reader', 'Config']
