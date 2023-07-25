from fastapi import APIRouter, status
from config.db import collection

router = APIRouter(
    tags = ['items'],
    prefix = ''

)

@router.post('/', status_code = status.HTTP_201_CREATED)
async def create_task():
    pass

async def get_task():
    pass

async def get_all_tasks():
    pass

async def update_task():
    pass

async def delete_task():
    pass 