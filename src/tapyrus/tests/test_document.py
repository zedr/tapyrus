import pytest

from tapyrus.documents import SwaggerDocument
from tapyrus.tests import fixtures
from tapyrus import exceptions as exc


def test_document_can_validate_swagger_documents():
    with pytest.raises(exc.NotASwaggerDocumentError):
        SwaggerDocument.validate({"swag": "2.0"})
    with pytest.raises(exc.UnsupportedDocumentError):
        SwaggerDocument.validate(
            {
                'swagger': '1.0',
                'info': {},
                'paths': {}
            }
        )


def test_document_has_paths():
    document = SwaggerDocument.load(fixtures.YAML_DOCUMENT_PATH)
    assert hasattr(document, 'paths')
