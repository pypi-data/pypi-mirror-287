#!/usr/bin/env python3
from pathlib import Path
from subprocess import run


def test_cli_tool_example():

    paths = list(Path("example").resolve().glob("*.docx"))
    assert len(paths) > 0, "No documents/*.docx available for testing"

    for path in paths:
        result = run(
            ["jugmt", f"{path}", "--output", str(path.with_name("output"))],
            capture_output=True,
            text=True,
        )

        assert not result.returncode


def test_cli_tool(tmp_path):

    paths = list(Path("example").resolve().glob("*.docx"))
    assert len(paths) > 0, "No documents/*.docx available for testing"

    for path in paths:
        result = run(
            ["jugmt", f"{path}", "--output", str(tmp_path)],
            capture_output=True,
            text=True,
        )

        assert not result.returncode


def test_cli_tool_version(tmp_path):

    result = run(["jugmt", "--version"], capture_output=True, text=True)

    assert not result.returncode


def test_cli_tool_missing_args(tmp_path):

    result = run(["jugmt"], capture_output=True, text=True)

    assert result.returncode, f"Expected failure, but got: {result.returncode}"
