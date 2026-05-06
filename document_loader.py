import os
from docx import Document
from PyPDF2 import PdfReader


def load_document_text(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".txt":
        return read_txt(file_path)

    if extension == ".docx":
        return read_docx(file_path)

    if extension == ".pdf":
        return read_pdf(file_path)

    raise ValueError("Unsupported file type. Use .txt, .docx, or .pdf")


def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def read_docx(file_path):
    document = Document(file_path)
    text = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text.append(paragraph.text)

    return "\n".join(text)


def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = []

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text.append(page_text)

    return "\n".join(text)