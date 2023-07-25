from fastapi import APIRouter
from .handlers.user import user_router
router = APIRouter()

router.include_router(user_router)