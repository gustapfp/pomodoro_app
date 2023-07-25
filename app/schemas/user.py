from pydantic import BaseModel, Field, EmailStr
from uuid import UUID
from typing import Optional

class UserAuthSchema(BaseModel):
     username:str = Field(..., min_length=5, max_length=50, description='Username chossed by the user')
     email:str = Field(..., min_length=5, max_length=100, description='Email in the format: example@example.com')
     password: str = Field(..., min_length=5, max_length=100, description='User hashed password')

class UserResponseDetailSchema(BaseModel):
     user_id: UUID
     username: str
     email: EmailStr
     fist_name: Optional[str]
     last_name: Optional[str]
     Valid: Optional[bool]
  
