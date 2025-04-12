# utils/ocr.py

from PIL import Image
import pytesseract
from pdf2image import convert_from_path

# Tell pytesseract where tesseract is installed
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Poppler path (optional, if not in PATH)
POPPLER_PATH = r"C:\poppler\poppler-24.08.0\Library\bin"

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
    all_text = ""
    for img in images:
        all_text += pytesseract.image_to_string(img) + "\n"
    return all_text
