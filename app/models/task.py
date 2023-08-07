from beanie import Document, Indexed, Link, before_event, Replace, Insert
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional
from pydantic import Field
from models.user import User

class Task(Document): 
    task_id: UUID = Field(default_factory=uuid4, unique=True)
    title: Indexed(str)
    description: Indexed(str)
    status: bool = False
    owner: Link[User]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def __repr__(self) -> str:
            return f"Task: {self.title}" 
    
    def __str__(self) -> str:
           return self.title 
    
    def __eq__(self, anotherTask: object) -> bool:
        if isinstance(anotherTask, Task): 
            return self.task_id == anotherTask.task_id # Make the comparation between the two objects
        return False
    
    def __hash__(self) -> int:
           return hash(self.title)
    
    @before_event([Replace, Insert])
    def sync_update_at(self):
        self.updated_at = datetime.utcnow()