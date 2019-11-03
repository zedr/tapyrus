from tapyrus.documents import SwaggerDocument
from tapyrus.servers import WebServer


def test_webserver_has_path_and_get_empty_handler():
    document = SwaggerDocument(
        {"swagger": "2.0", "info": {}, "paths": {"/fruits": {"get": {}}}}
    )
    server = WebServer.load(document)
    handler = server.routes["/fruits"]
    assert handler is None


def test_webserver_has_path_and_get_callable_handler():
    document = SwaggerDocument(
        {"swagger": "2.0", "info": {}, "paths": {"/fruits": {"get": {
            "x-tapyrus-handler": "tapyrus.tests.example_handlers.get_fruits"
        }}}}
    )
    server = WebServer.load(document)
    handler = server.routes["/fruits"]
    assert callable(handler)
    assert "fruits" in handler()
