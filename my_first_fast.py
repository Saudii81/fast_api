from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 
from typing import List

app = FastAPI

@app.get("/") 
async def root(): 
    return {"message": "Hello World"}

