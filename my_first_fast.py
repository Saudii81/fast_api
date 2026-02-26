from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 
from typing import List

app = FastAPI(
    title = "My Newly Fast API App",
    description = "A simple CRUD API build with FastAPI",
    version = "1.0.0" 
)

# Creating a Data Model
class Todo(BaseModel):
    id: int
    title = str
    completed: bool = False

# In-Memory database
todo: List[Todo] = []

# HOme route
@app.get("/") 
async def home(): 
    return {
        "message": "Hello to my First FastAPI App!",
        "docs": "/docs" 
        }

# todo get one todo
@app.get("/todo/{todo_id}")
def get_todo(todo_id: int)