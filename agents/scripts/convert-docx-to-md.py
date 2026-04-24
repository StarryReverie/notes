"""Convert DOCX files to Markdown using pandoc."""

import argparse
import subprocess
import sys

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


def convert(input_path: str, output_path: str | None = None) -> str:
    cmd = [
        "pandoc",
        input_path,
        "-f",
        "docx",
        "-t",
        "markdown",
        "--wrap=none",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if result.returncode != 0:
        print(f"pandoc error: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    md = result.stdout
    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md)
    return md


def main():
    parser = argparse.ArgumentParser(description="Convert DOCX to Markdown via pandoc")
    parser.add_argument("input", help="Input DOCX file path")
    parser.add_argument(
        "-o", "--output", help="Output Markdown file path (default: stdout)"
    )
    args = parser.parse_args()
    md = convert(args.input, args.output)
    if not args.output:
        print(md)


if __name__ == "__main__":
    main()
