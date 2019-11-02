class NotASwaggerDocumentError(Exception):
    """Does seem to be a valid Swagger document.
    """


class UnsupportedDocumentError(Exception):
    """This Swagger document type is unsupported.
    """
