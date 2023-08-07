from fastapi import APIRouter, status, Depends
from schemas.task_schema import CreateTaskSchema, ListTaskSchema, UpdateTaskSchema
from models.task import Task
from models.user import User
from api.dependencies.user_dependencies import get_current_user
from services.task_service import TaskService
from uuid import UUID
import pymongo
from typing import List


task_router = APIRouter(
    prefix = '/tasks',
    tags=['Tasks']
)



@task_router.post('/create_task', summary='Create a task in the database', status_code=status.HTTP_201_CREATED, response_model=Task)
async def create_task(data: CreateTaskSchema, curent_user: User = Depends(get_current_user)) -> Task:
    return await TaskService.create_task(data=data, user=curent_user)


@task_router.get('/get_tasks', summary='Get a list of tasks from a User', status_code=status.HTTP_200_OK, response_model=List[ListTaskSchema])
async def get_tasks(curent_user: User = Depends(get_current_user)):
    return await TaskService.get_user_tasks(user=curent_user)


@task_router.get('/get_task/{task_id}', summary='Get a especific task from a User', status_code=status.HTTP_200_OK, response_model=ListTaskSchema)
async def get_task(task_id:UUID, curent_user: User = Depends(get_current_user)) -> Task:
    return await TaskService.get_task(user=curent_user, task_id=task_id)
    

@task_router.put('/update_task/{task_id}', summary='Update a task', status_code= status.HTTP_200_OK, response_model=ListTaskSchema)
async def update_task(task_id: UUID, data: UpdateTaskSchema,  curent_user: User = Depends(get_current_user)) -> Task:
    return await TaskService.update_task(task_id=task_id, data=data, user=curent_user)

@task_router.delete('/delete_task/{task_id}', summary='Delete a specific task', status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: UUID, curent_user: User = Depends(get_current_user)) -> None:
    await TaskService.delete_task(task_id=task_id, user=curent_user)
