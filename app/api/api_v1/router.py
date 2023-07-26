from fastapi import APIRouter
from .handlers.user import user_router
from api.auth.jwt import auth_router
router = APIRouter()

router.include_router(user_router)
router.include_router(auth_router)