from fastapi import FastAPI
from core.config import settings
from beanie import init_beanie 
from motor.motor_asyncio import AsyncIOMotorClient
from models.user import User
from models.task import Task
from api.api_v1.router import router

tags_metadata = [
    {
        'name': 'Users',
        'description': 'Operations with users'
     },
     {
         'name': 'Auth',
         'description': 'Authentication operation and token generation'
     }, 
     {
         'name': 'Tasks',
         'description': 'CRUD operations with tasks'
     }
] 

app = FastAPI(
    title = settings.PROJECT_NAME,
    open_api_url = f"{settings.API_V1_STR}/openapi.json", 
    openapi_tags=tags_metadata
)

app.include_router(router,
                   prefix=settings.API_V1_STR)

@app.on_event("startup")
async def app_init():
    client_db = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).todoapp # connection string + database name
    await init_beanie(
        database = client_db,
        document_models = [
            User,
            Task,
                           ]
    )