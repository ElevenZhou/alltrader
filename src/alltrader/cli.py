from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="alltrader",
        description="Evidence-first trading research and agent framework.",
    )
    parser.add_argument("--version", action="version", version="%(prog)s 0.1.0")
    return parser


def main() -> int:
    build_parser().parse_args()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
