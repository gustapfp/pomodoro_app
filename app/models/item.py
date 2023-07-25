from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description:str
    responsavel: str # Change to type User later
    prioridade: str
