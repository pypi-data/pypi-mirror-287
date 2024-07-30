from typing import Generic, TypeVar, Union

from pydantic import BaseModel

ParsedModelType = BaseModel
T = TypeVar('T', bound=ParsedModelType)


class ModelResponse(BaseModel, Generic[T]):
    raw_text: str
    parsed_model: Union[T, None] = None
