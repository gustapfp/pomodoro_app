from fastapi import FastAPI
from core.config import settings
from beanie import init_beanie 
from motor.motor_asyncio import AsyncIOMotorClient


app = FastAPI(
    title = settings.PROJECT_NAME,
    open_api_url = f"{settings.API_V1_STR}/openapi.json"
)

@app.on_event("startup")
async def app_init():
    client_db = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).todoapp # connection string + database name
    await init_beanie(
        database = client_db,
        document_models = [
                           ]
    )