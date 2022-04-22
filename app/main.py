"""Imported libraries and modules"""
from uuid import UUID
#from typing import List
from fastapi import FastAPI
from models import User #, Gender, Role
import database


app = FastAPI()


@app.get("/api/v1/get")
async def fetch_users():
    """localhost:8000/api/v1/get  >  fetch users from db"""
    return database.get_users()


@app.post("/api/v1/post")
async def registger_user(user: User):
    """localhost:8000/api/v1/post   >  adding users with POST"""
    return database.join_user_data(user)


@app.delete("/api/v1/delete/{user_id}")
async def delete_user(user_id: UUID):
    """localhost:8000/api/v1/delete/{user_id}  >  delete users by user_id"""
    return database.delete_users(user_id)


@app.put("/api/v1/put")
async def update_user(user_update: User):
    """localhost:8000/api/v1/put  >  update user data"""
    return database.update_users(user_update)
