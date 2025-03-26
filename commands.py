from typing import Optional
from uuid import UUID

from pydantic import ConfigDict
from lato import Command

from models import Order


class CommandBase(Command):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    order: Order = None
    user_input: str = ''
    hotkey: str = ''

class ResetOrder(CommandBase):
    hotkey: str = "rs"

class AddProductByPlu(CommandBase):
    hotkey: str = "ad"

class ChangeQty(CommandBase):
    hotkey: str = "ch"
    index: str = None

class Storno(CommandBase):
    hotkey: str = "st"
    index: str = None

class SaveOrder(CommandBase):
    hotkey: str = "sv"
