from schemas.task_schema import CreateTaskSchema, ListTaskSchema, UpdateTaskSchema
from models.user import User
from models.task import Task
from typing import List
from uuid import UUID
from fastapi import HTTPException, status

class TaskService:
    
    @staticmethod
    async def create_task(data: CreateTaskSchema, user: User) -> Task:
        new_task = Task(**data.dict(), owner=user)
        return await new_task.insert()
         
    
    @staticmethod
    async def get_user_tasks(user: User) -> List[Task]:
        tasks_list = await Task.find(Task.owner.id ==  user.id).to_list()
        return tasks_list
    
    @staticmethod
    async def get_task(user: User, task_id: UUID) -> Task:
        target_task = await Task.find_one(Task.owner.id == user.id, Task.task_id == task_id)
        if not target_task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The task your are loking for doesn't exists ")
        return target_task
    
    @staticmethod
    async def update_task(user: User, data: UpdateTaskSchema, task_id: UUID) -> Task:
        target_task = await TaskService.get_task(user=user, task_id=task_id)
        if not target_task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The task your are loking for doesn't exists ")
        
        await target_task.update({
            '$set': data.dict(
                exclude_unset=True,   
            )
        })
        await target_task.save()
        return target_task
    
    @staticmethod
    async def delete_task(user:User, task_id: UUID) -> Task:
        target_task = await TaskService.get_task(user=user, task_id=task_id)

        if target_task:
            return await target_task.delete()
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The task your are loking for doesn't exists ")
        