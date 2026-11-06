#!/usr/bin/env python3
"""统计文本文件的行数、词数和字符数。"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def count_text(text: str) -> tuple[int, int, int]:
    """返回 (行数, 词数, 字符数)。"""
    lines = len(text.splitlines())
    words = len(text.split())
    chars = len(text)
    return lines, words, chars


def count_file(path: Path) -> tuple[int, int, int]:
    """读取文件并统计，读取失败时抛出 OSError 或 UnicodeDecodeError。"""
    return count_text(path.read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="统计文本文件的行数、词数和字符数")
    parser.add_argument("path", type=Path, help="要统计的文件路径")
    args = parser.parse_args(argv)

    try:
        lines, words, chars = count_file(args.path)
    except (OSError, UnicodeDecodeError) as exc:
        print(f"无法读取 {args.path}: {exc}", file=sys.stderr)
        return 1

    print(f"lines: {lines}")
    print(f"words: {words}")
    print(f"chars: {chars}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
