import os

from tapyrus.parsers import parse_yaml
from tapyrus.tests.fixtures import YAML_DOCUMENT_PATH


def test_yaml_parser_can_parse_documents():
    ns = parse_yaml(YAML_DOCUMENT_PATH)
    assert "swagger" in ns
