class NotASwaggerDocumentError(Exception):
    """Does seem to be a valid Swagger document.
    """


class UnsupportedSwaggerVersionError(Exception):
    """Is not a supported Swagger version.

    Supported versions are 2.0.
    """


class UnsupportedExtensionError(Exception):
    """Is not a supported document extension.

    Supported extensions are: yaml, json.
    """
