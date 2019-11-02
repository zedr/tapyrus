from tapyrus.parsers import parse_yaml
from tapyrus import exceptions as exc

YAML_EXTENSIONS = ('.yaml', 'yml')


class SwaggerDocument:
    supported_version: str = '2.0'

    def __init__(self, ns: dict) -> None:
        self.validate(ns)
        self._ns = ns

    @property
    def paths(self):
        return self._ns['paths']
    
    @classmethod
    def validate(cls, ns: dict) -> None:
        """Validate a supported Swagger namespace object.
        """
        for key in ('info', 'paths', 'swagger'):
            if key not in ns:
                raise exc.NotASwaggerDocumentError(
                    f'Not a valid Swagger document; missing attribute {key}'
                )

        version = ns['swagger']
        if version != cls.supported_version:
            raise exc.UnsupportedDocumentError(
                f"Unsupported Swagger version"
            )

    @classmethod
    def load(cls, path: str) -> 'SwaggerDocument':
        for ext in YAML_EXTENSIONS:
            if path.endswith(ext):
                parser = parse_yaml
                break
        else:
            raise exc.UnsupportedDocumentError(f'{path} is unsupported')

        return cls(parser(path))
