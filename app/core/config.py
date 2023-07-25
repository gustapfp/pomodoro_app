from typing import List
from decouple import config
from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    API_V1_STR : str = '/api/v1' # API string name
    JWT_SECRET_KEY = config('JWT_SECRET_KEY', cast=str) # JSON Web Tokens to veryfy and sign the objects
    JWT_REFRESH_SECRET_KEY = config('JWT_REFRESH_SECRET_KEY', cast=str)
    ALGORITHM = 'HS256' # ALogorithm to the JWT token
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 
    REFRESH_TOKEN_EXPIRE_MINUTE: int = 60*24*7 # 7 days
    PROJECT_NAME: str = 'ToDoAPI'

    MONGO_CONNECTION_STRING: str = config("MONGO_CONNECTION_STRING", cast=str)

    class Config:
        case_sensitive=True

settings = Settings()