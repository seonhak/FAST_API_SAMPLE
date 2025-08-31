from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

T = TypeVar("T")

class CommonResponse(BaseModel, Generic[T]):
    status_code: int
    status_message: str
    data: Optional[T] = None