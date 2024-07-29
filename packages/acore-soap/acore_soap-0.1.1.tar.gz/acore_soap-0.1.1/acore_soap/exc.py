# -*- coding: utf-8 -*-


class SOAPResponseParseError(ValueError):
    """
    raises when failed to parse the soap response.
    """


class SOAPCommandFailedError(ValueError):
    """
    raises when SOAP command failed
    """
