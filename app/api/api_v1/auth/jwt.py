from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from services.user_service import UserService 
from schemas.auth_schema import TokenSchema

auth_router = APIRouter()