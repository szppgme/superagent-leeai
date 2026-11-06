"""tools.wordcount 的 pytest 测试。"""

from __future__ import annotations

import pytest

from tools import wordcount

EMPTY = ""
SINGLE_LINE = "hello world\n"
MULTILINE = "first line\nsecond line\nthird line with several words\n"

CASES = [
    pytest.param(EMPTY, (0, 0, 0), id="empty-file"),
    pytest.param(SINGLE_LINE, (1, 2, 12), id="single-line"),
    pytest.param(MULTILINE, (3, 9, 53), id="multiple-lines"),
]


@pytest.mark.parametrize(("content", "expected"), CASES)
def test_count_text(content: str, expected: tuple[int, int, int]) -> None:
    assert wordcount.count_text(content) == expected


@pytest.mark.parametrize(("content", "expected"), CASES)
def test_count_file(tmp_path, content: str, expected: tuple[int, int, int]) -> None:
    path = tmp_path / "sample.txt"
    path.write_text(content, encoding="utf-8")

    assert wordcount.count_file(path) == expected


@pytest.mark.parametrize(("content", "expected"), CASES)
def test_main_prints_counts(tmp_path, capsys, content: str, expected: tuple[int, int, int]) -> None:
    path = tmp_path / "sample.txt"
    path.write_text(content, encoding="utf-8")

    assert wordcount.main([str(path)]) == 0
    lines, words, chars = expected
    assert capsys.readouterr().out.splitlines() == [
        f"lines: {lines}",
        f"words: {words}",
        f"chars: {chars}",
    ]


def test_main_reports_missing_file(tmp_path, capsys) -> None:
    missing = tmp_path / "missing.txt"

    assert wordcount.main([str(missing)]) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert str(missing) in captured.err
