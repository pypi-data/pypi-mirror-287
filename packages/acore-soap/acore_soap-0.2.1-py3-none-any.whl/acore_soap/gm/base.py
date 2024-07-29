# -*- coding: utf-8 -*-

"""
Common utilities.
"""

import dataclasses

from ..request import (
    SOAPRequest,
    SOAPResponse,
    DEFAULT_USERNAME,
    DEFAULT_PASSWORD,
    DEFAULT_HOST,
    DEFAULT_PORT,
)


@dataclasses.dataclass
class GMCommandRequest:
    """
    todo: docstring
    """

    def to_command(self) -> str:
        """
        Build the GM command.

        See all GM commands at https://www.azerothcore.org/wiki/gm-commands
        """
        raise NotImplementedError

    def send(
        self,
        username: str = DEFAULT_USERNAME,
        password: str = DEFAULT_PASSWORD,
        host: str = DEFAULT_HOST,
        port: int = DEFAULT_PORT,
    ) -> SOAPResponse:
        req = SOAPRequest(
            command=self.to_command(),
            username=username,
            password=password,
            host=host,
            port=port,
        )
        return req.send()


@dataclasses.dataclass
class GMCommandResponse:
    """
    todo: docstring
    """

    @classmethod
    def from_soap_response(self, res: SOAPResponse):
        """
        Parse from soap response.
        """
        raise NotImplementedError
