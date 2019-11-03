import importlib

from tapyrus import defaults


def _load_module(dotted_path: str) -> object:
    """Load a module by its dotted path.
    """
    module_name, func_name = dotted_path.rsplit(".", 1)
    module = importlib.import_module(module_name)
    return getattr(module, func_name)


class WebServer:
    handler_attr = defaults.HANDLER_ATTRIBUTE_NAME

    def __init__(self, route_ns: dict) -> None:
        self._route_ns = route_ns

    @property
    def routes(self):
        return self._route_ns

    @classmethod
    def load(cls, document) -> None:
        routes = {}
        attr = cls.handler_attr
        for path, methods in document.paths.items():
            for method, ns in methods.items():
                handler = None
                try:
                    handler = _load_module(ns[attr])
                except KeyError:
                    # todo: add a message
                    pass
                except ImportError:
                    # todo: add a message
                    pass

                routes[path] = handler
        return cls(routes)
