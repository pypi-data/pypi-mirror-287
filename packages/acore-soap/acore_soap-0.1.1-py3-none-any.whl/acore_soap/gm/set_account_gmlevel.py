# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import re
import dataclasses

from ..request import SOAPResponse
from ..exc import SOAPResponseParseError

from .base import GMCommandRequest, GMCommandResponse


@dataclasses.dataclass
class SetAccountGmlevelResponse(GMCommandResponse):
    """
    Parse the response message of ``.account set gmlevel ...`` command.
    """

    @classmethod
    def from_soap_response(cls, res: SOAPResponse):
        raise NotImplementedError


@dataclasses.dataclass
class SetAccountGmlevelRequest(GMCommandRequest):
    """
    :param account:
    :param gmlevel:
        - 0: SEC_PLAYER
        - 1: SEC_MODERATOR
        - 2: SEC_GAMEMASTER
        - 3: SEC_ADMINISTRATOR
    :param realm_id: -1 for all realms
    """

    account: str = dataclasses.field()
    gmlevel: int = dataclasses.field()
    realm_id: int = dataclasses.field()

    def to_command(self) -> str:
        return f".account set gmlevel {self.account} {self.gmlevel} {self.realm_id}"
