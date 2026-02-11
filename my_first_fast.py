from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 
from typing import List

app = FastAPI(
    title = "My Newly Fast API App",
    description = "A simple CRUD API build with FastAPI",
    version = "1.0.0" 
)



@app.get("/") 
async def root(): 
    return {"message": "Hello World"}

