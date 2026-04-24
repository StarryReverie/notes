"""Convert PPTX files to Markdown using pandoc."""

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
        "pptx",
        "-t",
        "markdown",
        "--wrap=none",
    ]
    if output_path:
        cmd.extend(["-o", output_path])
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        if result.returncode != 0:
            print(f"pandoc error: {result.stderr}", file=sys.stderr)
            sys.exit(1)
        with open(output_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        if result.returncode != 0:
            print(f"pandoc error: {result.stderr}", file=sys.stderr)
            sys.exit(1)
        return result.stdout


def main():
    parser = argparse.ArgumentParser(description="Convert PPTX to Markdown via pandoc")
    parser.add_argument("input", help="Input PPTX file path")
    parser.add_argument(
        "-o", "--output", help="Output Markdown file path (default: stdout)"
    )
    args = parser.parse_args()
    md = convert(args.input, args.output)
    if not args.output:
        print(md)


if __name__ == "__main__":
    main()
