from pydantic import BaseModel as B
from typing import Any, Union


class CongressApiError(B):
    class ErrorCode(B):
        code: str
        message: str

    error: Union[str, ErrorCode]

class UnsupportedActionError(Exception):
    ...

class MissingArgumentsError(Exception):
    ...