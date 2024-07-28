from setuptools import setup, find_packages

setup(
    name='pdf_text_digitizer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'PyPDF2',
        'pytesseract',
        'Pillow',
        'pdf2image',
    ],
    entry_points={
        'console_scripts': [
            'pdf_text_digitizer=pdf_text_digitizer.digitize:main',
        ],
    },
    author='Rohit Satija',
    author_email='rohitsatija0092@gmail.com',
    description='A package for digitizing text from PDF files.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rohitium/pdf_text_digitizer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
