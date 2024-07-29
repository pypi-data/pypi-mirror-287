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
class ChangeAccountPasswordResponse(GMCommandResponse):
    """
    Parse the response message of ``.account password ...`` command.
    """

    @classmethod
    def from_soap_response(cls, res: SOAPResponse):
        raise NotImplementedError


@dataclasses.dataclass
class ChangeAccountPasswordRequest(GMCommandRequest):
    """
    todo: docstring
    """

    account: str = dataclasses.field()
    old_password: str = dataclasses.field()
    new_password: str = dataclasses.field()

    def to_command(self) -> str:
        return f".account password {self.account} {self.old_password} {self.new_password} {self.new_password}"
