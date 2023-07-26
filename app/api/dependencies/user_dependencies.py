
from fastapi.security import OAuth2PasswordBearer 
from core.config import settings
from fastapi import Depends, HTTPException, status
from models.user import User
from jose import jwt
from datetime import datetime
from pydantic import ValidationError
from services.user_service import UserService
from schemas.auth_schema import TokenPayLoad, TokenSchema
reusable_token = OAuth2PasswordBearer(
    tokenUrl = f'{settings.API_V1_STR}/auth/login',
    scheme_name = 'JWT'
)

async def get_current_user(token: str = Depends(reusable_token)) -> User:
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            settings.ALGORITHM
        )
        token_data = TokenPayLoad(**payload)
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED, 
                datails = 'Expired Token',
                headers = {'WWW-Authenticate' : 'Barear'}
            )
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
                datails = "Coudn't find the user",
                headers = {'WWW-Authenticate' : 'Barear'}
            )
   
    return user