from typing import Generic, TypeVar, Optional
from pydantic.generics import GenericModel

T = TypeVar("T")

class CommonResponse(GenericModel, Generic[T]):
    status_code: int
    status_message: str
    data: Optional[T] = None