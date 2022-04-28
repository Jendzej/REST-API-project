"""Imported libraries and modules"""
from uuid import UUID
from fastapi import FastAPI
from models import User
import database
import uvicorn


app = FastAPI()


@app.get("/api/v1/users/")
async def fetch_all_users():
    """localhost:8000/api/v1/get  >  fetch users from db"""
    return database.get_users()


@app.get("/api/v1/users/1/{user_id}")
async def fetch_one_user(user_id: UUID):
    return database.get_one_user(user_id)


@app.post("/api/v1/users/")
async def insert_user_data(user: User):
    """localhost:8000/api/v1/post   >  adding users with POST"""
    return database.join_user_data(user)


@app.delete("/api/v1/users/1/{user_id}")
async def delete_user(user_id: UUID):
    """localhost:8000/api/v1/delete/{user_id}  >  delete users by user_id"""
    return database.delete_users(user_id)


@app.put("/api/v1/users/1/{user_id}")
async def update_user(user_id: UUID): # user_update: User
    """localhost:8000/api/v1/put  >  update user data"""
    return database.update_users(user_id)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        reload=True,
        port=8000
    )
