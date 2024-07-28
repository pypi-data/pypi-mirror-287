# PDF Text Digitizer

PDF Text Digitizer is a Python tool to extract text from PDF files. It supports both text-based PDFs and image-based PDFs using OCR.

## Features

- Extracts text from text-based PDFs.
- Extracts text from image-based PDFs using OCR.
- Simple API for easy integration.

## Installation

Clone the repository and install the dependencies:

```sh
git clone https://github.com/yourusername/pdf-text-digitizer.git
cd pdf-text-digitizer
pip install -r requirements.txt
```

## Usage
```python
from pdf_text_digitizer.digitize import digitize_pdf

text = digitize_pdf('path/to/your/pdf_file.pdf')
print(text)
```

## Examples

You can find example usage in the examples directory. To run the example:

```sh
python examples/example_usage.py
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.