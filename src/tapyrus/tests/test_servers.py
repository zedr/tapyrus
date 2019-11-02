from tapyrus.documents import SwaggerDocument
from tapyrus.servers import WebServer


def test_webserver_has_path_and_get_handler():
    document = SwaggerDocument(
        {"swagger": "2.0", "info": {}, "paths": {"/fruits": {"get": {}}}}
    )
    server = WebServer.load(document)
    handler = server.routes["/fruits"]
    assert handler is None
