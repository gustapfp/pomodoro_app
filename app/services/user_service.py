from schemas.user import UserAuthSchema
from models.user import User
from core.security import get_password, verify_password
from typing import Optional
from uuid import UUID, uuid4

class UserService: 
    @staticmethod
    async def create_user(user: UserAuthSchema):
        new_user = User(
            username = user.username,
            email = user.email,
            hash_password = get_password(user.password)
        )
        await new_user.save()
        return new_user
    
    @staticmethod
    async def get_user_by_email(email:str) -> Optional[User]:
        user = await User.find_one(User.email == email)
        return user
    
    @staticmethod
    async def autheticate(email:str, password:str) -> Optional[User]:
        user = await UserService.get_user_by_email(email=email)
        if not user: 
            return None
        if not verify_password(password=password, hashed_password=user.hash_password): 
            return None
        return user
    
    @staticmethod
    async def get_user_by_id(id: UUID) -> Optional[User]:
        user = await User.find_one(User.user_id == id)
        return user