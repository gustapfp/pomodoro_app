from pydantic import BaseModel, Field
from typing import Optional
from models.user import User
from datetime import datetime
from uuid import UUID

class CreateTaskSchema(BaseModel):
    title:str = Field(..., max_length=50, min_length=5, description='Task title')
    description: str = Field(..., max_length=150, min_length=5, description='Task title')
    status: Optional[bool] = False

class UpdateTaskSchema(BaseModel):
    title: Optional[str] 
    description: Optional[str] 
    status: Optional[bool] = False

class ListTaskSchema(BaseModel):
    task_id: UUID 
    status: bool
    title: str
    description: str
    created_at: datetime
    updated_at: datetime