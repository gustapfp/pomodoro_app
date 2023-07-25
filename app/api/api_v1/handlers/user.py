from fastapi import APIRouter, status, HTTPException
from schemas.user import UserAuthSchema, UserResponseDetailSchema
from services.user_service import UserService
import pymongo
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
