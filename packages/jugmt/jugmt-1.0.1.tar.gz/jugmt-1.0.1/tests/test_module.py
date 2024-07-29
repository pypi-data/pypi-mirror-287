#!/usr/bin/env python3
from pathlib import Path

from jugmt.cli import docx_to_figure_document


def test_module(tmp_path):

    paths = list(Path("example").resolve().glob("*.docx"))
    assert len(paths) > 0, "No documents/*.docx available for testing"

    for path in paths:
        document, errors = docx_to_figure_document(path)

        document_json_str = document.to_json()
        assert document_json_str, "Failed producing a string of JSON"

        document_html_str = document.to_html()
        assert document_html_str, "Failed producing a string of HTML"

        assert document.is_valid(), "Unexpected failure"

        assert len(document.figures) == 2, "Unexpected amount of figures in document"
