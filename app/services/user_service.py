from schemas.user import UserAuthSchema
from models.user import User
from core.security import get_password, verify_password

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
