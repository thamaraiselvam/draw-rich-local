from __future__ import annotations

import argparse
from pathlib import Path

from .pipeline import DiagramPipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Local AI-assisted D2 diagram generator")
    parser.add_argument("--prompt", required=True, help="Natural-language architecture request")
    parser.add_argument("--model", default="llama3.1", help="Local model name")
    parser.add_argument("--llm-base-url", default="http://localhost:11434", help="Local LLM base URL")
    parser.add_argument("--out", default="outputs/diagram.svg", help="Rendered output path")
    parser.add_argument("--keep-d2", action="store_true", help="Keep generated D2 source file")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    pipeline = DiagramPipeline(model=args.model, llm_base_url=args.llm_base_url)
    output = pipeline.generate(prompt=args.prompt, out_file=Path(args.out), keep_d2=args.keep_d2)
    print(f"Generated artifact: {output}")


if __name__ == "__main__":
    main()
