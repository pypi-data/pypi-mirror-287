# -*- coding: utf-8 -*-

"""
SOAP request and response.
"""

import json
import dataclasses
from pathlib import Path
import xml.etree.ElementTree as ET

import requests

from .exc import SOAPResponseParseError, SOAPCommandFailedError


# ------------------------------------------------------------------------------
# Soap Request and Response
# ------------------------------------------------------------------------------
path_xml = Path(__file__).absolute().parent / "execute-command.xml"

# default soap request headers
_SOAP_REQUEST_HEADERS = {"Content-Type": "application/xml"}
_SOAP_REQUEST_XML_TEMPLATE = path_xml.read_text(encoding="utf-8")
DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "admin"
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 7878


@dataclasses.dataclass
class Base:
    """
    Base class for :class:`SOAPRequest` and :class:`SOAPResponse`.
    """

    @classmethod
    def from_dict(cls, dct: dict):
        """
        Construct an object from a dict.
        """
        return cls(**dct)

    def to_dict(self) -> dict:
        """
        Convert the object to a dict.
        """
        return {k: v for k, v in dataclasses.asdict(self).items() if v is not None}

    @classmethod
    def from_json(cls, json_str: str):
        """
        Construct an object from a JSON string.
        """
        return cls.from_dict(json.loads(json_str))

    def to_json(self) -> str:  # pragma: no cover
        """
        Convert the object to a JSON string.
        """
        return json.dumps(self.to_dict())


@dataclasses.dataclass
class SOAPRequest(Base):
    """
    :class:`~acore_soap_app.agent.impl.SOAPRequest` is a dataclass to represent
    the SOAP XML request.

    Usage example

    .. code-block:: python

        # this code only works in where the worldserver is running
        >>> request = SOAPRequest(command=".server info")
        >>> response = request.send()
        >>> response.to_json()
        {
            "body": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/1999/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/1999/XMLSchema\" xmlns:ns1=\"urn:AC\"><SOAP-ENV:Body><ns1:executeCommandResponse><result>AzerothCore rev. 85311fa55983 2023-03-25 22:36:05 +0000 (master branch) (Unix, RelWithDebInfo, Static)&#xD;Connected players: 0. Characters in world: 0.&#xD;Connection peak: 0.&#xD;Server uptime: 54 minute(s) 3 second(s)&#xD;Update time diff: 10ms, average: 10ms.&#xD;</result></ns1:executeCommandResponse></SOAP-ENV:Body></SOAP-ENV:Envelope>",
            "message": "AzerothCore rev. 85311fa55983 2023-03-25 22:36:05 +0000 (master branch) (Unix, RelWithDebInfo, Static)Connected players: 0. Characters in world: 0.Connection peak: 0.Server uptime: 54 minute(s) 3 second(s)Update time diff: 10ms, average: 10ms.",
            "succeeded": true
        }

    :param command: the command to execute.
    :param username: the in game GM account username, default "admin".
    :param password: the in game GM account password, default "admin".
    :param host: wow world server host, default "localhost".
    :param port: wow world server SOAP port, default 7878.

    More methods from base class:

    - :meth:`~Base.from_dict`
    - :meth:`~Base.to_dict`
    - :meth:`~Base.from_json`
    - :meth:`~Base.to_json`
    """

    command: str = dataclasses.field()
    username: str = dataclasses.field(default=DEFAULT_USERNAME)
    password: str = dataclasses.field(default=DEFAULT_PASSWORD)
    host: str = dataclasses.field(default=DEFAULT_HOST)
    port: int = dataclasses.field(default=DEFAULT_PORT)

    @property
    def endpoint(self) -> str:
        """
        Construct the Soap service endpoint URL.
        """
        return f"http://{self.username}:{self.password}@{self.host}:{self.port}/"

    def send(self) -> "SOAPResponse":  # pragma: no cover
        """
        Run soap command via HTTP request. This function "has to" be run on the
        game server and talk to the localhost. You should NEVER open SOAP port
        to public!
        """
        http_response = requests.post(
            self.endpoint,
            headers=_SOAP_REQUEST_HEADERS,
            data=_SOAP_REQUEST_XML_TEMPLATE.format(command=self.command),
        )
        return SOAPResponse.parse(http_response.text)


@dataclasses.dataclass
class SOAPResponse(Base):
    """
    :class:`~acore_soap_app.agent.impl.SOAPResponse` is a dataclass to represent
    the SOAP XML response.

    Usage:

    .. code-block:: python

        >>> res = SOAPResponse.parse(
        ...  '''
        ...      <?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope
        ...      ...<result>Account created: test&#xD;</result>...</SOAP-ENV:Envelope>
        ...  '''
        ... )
        >>> res.message
        Account created: test
        >>> res.succeeded
        True

    :param body: the raw SOAP XML response
    :param message: if succeeded, it is the ``<result>...</result>`` part.
        if failed, it is the ``<faultstring>...</faultstring>`` part
    :param succeeded: a boolean flag to indicate whether the command is succeeded

    More methods from base class:

    - :meth:`~Base.from_dict`
    - :meth:`~Base.to_dict`
    - :meth:`~Base.from_json`
    - :meth:`~Base.to_json`
    """

    body: str = dataclasses.field()
    message: str = dataclasses.field()
    succeeded: bool = dataclasses.field()

    @classmethod
    def parse(cls, body: str) -> "SOAPResponse":
        """
        Parse the SOAP XML response.
        """
        root = ET.fromstring(body)

        results = list(root.iter("result"))
        if len(results):
            result = results[0]
            if result.text:
                message = result.text.strip()
            else:
                message = "No result"
            return cls(
                body=body.strip(),
                message=message,
                succeeded=True,
            )

        faultstrings = list(root.iter("faultstring"))
        if len(faultstrings):
            faultstring = faultstrings[0]
            if faultstring.text:
                message = faultstring.text.strip()
            else:
                message = "No fault string"
            return cls(
                body=body.strip(),
                message=message,
                succeeded=False,
            )

        # todo: add logic to handle SOAPCommandFailedError situation
        raise SOAPResponseParseError(f"Cannot parse the response: {body!r}")

    def print(self):  # pragma: no cover
        """
        Print the dataclass, ignore the raw response body.
        """
        print({"succeeded": self.succeeded, "message": self.message})


def ensure_response_succeeded(
    request: SOAPRequest,
    response: SOAPResponse,
    raises: bool,
):
    """
    Ensure the response succeeded, otherwise raise an exception.
    """
    if response.succeeded:
        return response
    else:
        if raises:
            raise SOAPCommandFailedError(
                f"request failed: {request.command!r}, "
                f"response: {response.message!r}"
            )
