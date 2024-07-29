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
class SetAccountPasswordResponse(GMCommandResponse):
    """
    Parse the response message of ``.account set password ...`` command.
    """

    @classmethod
    def from_soap_response(cls, res: SOAPResponse):
        raise NotImplementedError


@dataclasses.dataclass
class SetAccountPasswordRequest(GMCommandRequest):
    """
    todo: docstring
    """

    account: str = dataclasses.field()
    new_password: str = dataclasses.field()

    def to_command(self) -> str:
        return f".account set password {self.account} {self.new_password} {self.new_password}"
