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
class AddItemResponse(GMCommandResponse):
    """
    Parse the response message of ``.additem ...`` command.
    """

    @classmethod
    def from_soap_response(cls, res: SOAPResponse):
        raise NotImplementedError


@dataclasses.dataclass
class AddItemRequest(GMCommandRequest):
    """
    todo: docstring
    """

    player: str = dataclasses.field()
    item_id: int = dataclasses.field()
    count: int = dataclasses.field(default=1)

    def to_command(self) -> str:
        return f".additem {self.player} {self.item_id} {self.count}"
