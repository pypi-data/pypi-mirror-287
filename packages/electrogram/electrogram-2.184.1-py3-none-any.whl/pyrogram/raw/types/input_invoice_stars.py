from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputInvoiceStars(TLObject):  # type: ignore
    __slots__: List[str] = ["option"]

    ID = 0x1da33ad8
    QUALNAME = "types.InputInvoiceStars"

    def __init__(self, *, option: "raw.base.StarsTopupOption") -> None:
        self.option = option  # StarsTopupOption

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoiceStars":
        # No flags
        
        option = TLObject.read(b)
        
        return InputInvoiceStars(option=option)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.option.write())
        
        return b.getvalue()
