from fastapi import APIRouter, Depends, status, HTTPException, Body
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from services.user_service import UserService 
from schemas.auth_schema import TokenSchema, TokenPayLoad
from schemas.user import UserResponseDetailSchema
from core.security import create_access_token, create_refresh_token
from pydantic import ValidationError
from core.config import settings
from jose import jwt
from datetime import datetime
from models.user import User

from schemas.auth_schema import TokenSchema, TokenPayLoad

auth_router = APIRouter(
    prefix= '/auth',
    tags = ['Auth']
    
)

@auth_router.post('/login', summary='User login authentication')
async def login(data: OAuth2PasswordRequestForm = Depends()) -> Any:
    usuario = await UserService.autheticate(
        email=data.username,
        password=data.password
    )
    if not usuario:
        raise HTTPException( 
            status_code = status.HTTP_400_BAD_REQUEST,
            detail= "Coudn't find the user, check if you use the right credentials"
        )
    
    return {
        'access_token': create_access_token(usuario.user_id),
        'refresh_token': create_refresh_token(usuario.user_id)
    }

@auth_router.post('/refresh', summary='Refresh Token', response_model=TokenSchema)
async def refresh_jwt_token(refresh_token: str = Body(...)):
    try:
        payload = jwt.decode(
            refresh_token,
            settings.JWT_SECRET_KEY,
            settings.ALGORITHM
        )
        token_data = TokenPayLoad(**payload)

    except(jwt.JWTError, ValidationError):
        raise HTTPException(
                status_code = status.HTTP_403_FORBIDEN, 
                datails = 'Error in the Token validation',
                headers = {'WWW-Authenticate' : 'Barear'}
            )
    user = await UserService.get_user_by_id(token_data.sub)
    if not User:
         raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND, 
                datails = 'Error in the Token validation',
                headers = {'WWW-Authenticate' : 'Barear'}
            )
    return {
        "access_token": create_access_token(user.user_id),
        "refresh_token": create_refresh_token(user.user_id)
    }

