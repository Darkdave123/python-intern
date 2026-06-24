from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


class TaskCreate(BaseModel):
    title: str
    description: str
    priority: str
    status: str
    due_date: str


class TaskUpdate(TaskCreate):
    pass