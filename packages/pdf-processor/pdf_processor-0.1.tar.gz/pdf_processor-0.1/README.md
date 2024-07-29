# pdf_processor

A PDF processing package to convert PDF to images and adjust their brightness and contrast.

## Installation

```bash
pip install pdf_processor
```

## Usage

```python
from pdf_processor import process_pdf

pdf_path = "input1.pdf"
output_pdf_path = 'output.pdf'
process_pdf(pdf_path, output_pdf_path, resolution=300, factor=1, contrast_factor=1)
```
