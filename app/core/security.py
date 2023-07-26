from passlib.context import CryptContext
from typing import Union, Any
from jose import jwt
from core.config import settings
from datetime import datetime, timedelta
password_context = CryptContext(
    schemes=['bcrypt'],
    deprecated='auto'
)


def get_password(password:str) -> str:
    return password_context.hash(password)

def verify_password(password:str, hashed_password:str) -> bool:
    return password_context.verify(password, hashed_password)

def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> Any:
    if expires_delta is not None:
        expires_delta = datetime.now() + expires_delta
    else: 
        expires_delta = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    jwt_payload = {
        "exp" : expires_delta,
        "sub" : str(subject)
    }

    jwt_encoded = jwt.encode(
        jwt_payload,
        settings.JWT_SECRET_KEY,
        settings.ALGORITHM
    )
    return jwt_encoded

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> Any:
    if expires_delta is not None:
        expires_delta = datetime.now() + expires_delta
    else: 
        expires_delta = datetime.utcnow() + timedelta(
            minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTE
        )
    jwt_payload = {
        "exp" : expires_delta,
        "sub" : str(subject)
    }
    
    jwt_encoded = jwt.encode(
        jwt_payload,
        settings.JWT_REFRESH_SECRET_KEY,
        settings.ALGORITHM
    )
    return jwt_encoded
