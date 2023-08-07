from fastapi import APIRouter, status, HTTPException, Depends
from models.user import User
from schemas.user import UserAuthSchema, UserResponseDetailSchema
from services.user_service import UserService
import pymongo
from api.dependencies.user_dependencies import get_current_user

user_router = APIRouter(
    prefix='/users',
    tags = ['Users']
)

@user_router.post('/create_user', status_code = status.HTTP_201_CREATED, response_model=UserResponseDetailSchema, summary='Create a new user in the app.')
async def create_user(data: UserAuthSchema):
    try: 
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail='Username or Email alrady exists.'
        )
@user_router.get('/me', summary='Gets the detail of a logged User', response_model=UserResponseDetailSchema)
async def get_user_detail_profile(user: User = Depends(get_current_user)):
    return user