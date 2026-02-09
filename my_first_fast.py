from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 
from typing import List

app = FastAPI(
    title = "My Newly Fast API App",
    description = "A simple CRUD API build with FastAPI",
    version =
)

@app.get("/") 
async def root(): 
    return {"message": "Hello World"}

