"""Convert PDF files to Markdown.

Text mode (default): uses pymupdf to extract embedded text.
OCR mode (--ocr): uses pytesseract + pdf2image for scanned/image-based PDFs.
"""

import argparse
import sys

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


def extract_text(input_path: str) -> str:
    import fitz

    doc = fitz.open(input_path)
    pages = []
    for page in doc:
        text = page.get_text()
        pages.append(text)
    doc.close()
    return "\n\n---\n\n".join(pages)


def extract_ocr(input_path: str, lang: str = "chi_sim+eng") -> str:
    from pdf2image import convert_from_path
    import pytesseract

    images = convert_from_path(input_path)
    pages = []
    for img in images:
        text = pytesseract.image_to_string(img, lang=lang)
        pages.append(text)
    return "\n\n---\n\n".join(pages)


def convert(
    input_path: str,
    output_path: str | None = None,
    ocr: bool = False,
    lang: str = "chi_sim+eng",
) -> str:
    if ocr:
        md = extract_ocr(input_path, lang)
    else:
        md = extract_text(input_path)
    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md)
    return md


def main():
    parser = argparse.ArgumentParser(description="Convert PDF to Markdown")
    parser.add_argument("input", help="Input PDF file path")
    parser.add_argument(
        "-o", "--output", help="Output Markdown file path (default: stdout)"
    )
    parser.add_argument(
        "--ocr", action="store_true", help="Use OCR mode (requires Tesseract + Poppler)"
    )
    parser.add_argument(
        "--lang", default="chi_sim+eng", help="OCR language (default: chi_sim+eng)"
    )
    args = parser.parse_args()
    md = convert(args.input, args.output, ocr=args.ocr, lang=args.lang)
    if not args.output:
        print(md)


if __name__ == "__main__":
    main()
