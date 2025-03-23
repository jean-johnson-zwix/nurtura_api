from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, Field

T = TypeVar('T')

class CreateUserProfileRequest(BaseModel):
    user_name: str
    password: str
    first_name: str
    last_name: str
    email: str
    age: int
    height: float
    weight: float

class CreateUserProfileResponse(BaseModel):
    user_id: int
    user_name: str

class Response(BaseModel, Generic[T]):
    status_code: int
    message: str
    result: Optional[T] = None

class UserLogin(BaseModel):
    user_name: str
    password: str


