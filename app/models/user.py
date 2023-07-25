from beanie import Document, Indexed
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional
from pydantic import Field, EmailStr


class User(Document):
    user_id: UUID = Field(defaulf_factory=uuid4)
    username: Indexed(str, unique=True)
    email: Indexed(EmailStr, unique=True)
    hash_password: str
    fist_name: Optional[str]
    last_name: Optional[str]
    Valid: Optional[bool]

    def __repr__(self) -> str:
        return f' -> User Email: {self.email} <-'
    
    def __str__(self) -> str:
        return self.email
    
    def __hash__(self) -> int:
        return hash(self.email)
    
    def __eq__(self, anotherObject) -> bool:
        if isinstance(anotherObject, User):
            return self.email == anotherObject.email
        return False
    
    @property
    def created_at(self) -> datetime:
        return self.id.generation_time
    
    @classmethod
    async def find_by_email(self, email:str) -> 'User':
        return await self.find_one(self.email== email)