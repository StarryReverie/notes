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


def extract_text(
    input_path: str,
    offset: int = 0,
    limit: int | None = None,
) -> str:
    import fitz

    doc = fitz.open(input_path)
    doc_total = len(doc)
    start = min(offset, doc_total)
    end = doc_total if limit is None else min(start + limit, doc_total)
    count = end - start
    pages = []
    for step, page_idx in enumerate(range(start, end), start=1):
        text = doc[page_idx].get_text()
        pages.append(text)
        print(f"Progress: page #{page_idx + 1} done ({step}/{count})", file=sys.stderr)
    doc.close()
    return "\n\n---\n\n".join(pages)


def extract_ocr(
    input_path: str,
    lang: str = "chi_sim+eng",
    offset: int = 0,
    limit: int | None = None,
) -> str:
    from pdf2image import convert_from_path
    import pytesseract

    first_page = offset + 1
    kwargs: dict = {"first_page": first_page}
    if limit is not None:
        kwargs["last_page"] = first_page + limit - 1
    images = convert_from_path(input_path, **kwargs)
    count = len(images)
    pages = []
    for step, img in enumerate(images, start=1):
        text = pytesseract.image_to_string(img, lang=lang)
        pages.append(text)
        page_num = first_page + step - 1
        print(f"Progress: page #{page_num} done ({step}/{count})", file=sys.stderr)
    return "\n\n---\n\n".join(pages)


def convert(
    input_path: str,
    output_path: str | None = None,
    ocr: bool = False,
    lang: str = "chi_sim+eng",
    offset: int = 0,
    limit: int | None = None,
) -> str:
    if ocr:
        md = extract_ocr(input_path, lang, offset=offset, limit=limit)
    else:
        md = extract_text(input_path, offset=offset, limit=limit)
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
    parser.add_argument(
        "--offset", type=int, default=0, help="Start page index (0-based, default: 0)"
    )
    parser.add_argument(
        "--limit", type=int, default=None, help="Number of pages to process (default: all)"
    )
    args = parser.parse_args()
    md = convert(
        args.input, args.output, ocr=args.ocr, lang=args.lang,
        offset=args.offset, limit=args.limit,
    )
    if not args.output:
        print(md)


if __name__ == "__main__":
    main()
