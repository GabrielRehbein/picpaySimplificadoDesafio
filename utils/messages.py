from pydantic import BaseModel
from typing import ClassVar


class Message(BaseModel):
    SUCCESS: ClassVar[str] = 'success'
