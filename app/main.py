"""Imported libraries and modules"""
from uuid import UUID
from fastapi import FastAPI
from models import User
import database
import uvicorn


app = FastAPI()


@app.get("/api/v1/users/")
async def fetch_all_users():
    """GET method, which fetch all users from database"""
    return database.get_users()


@app.get("/api/v1/users/1/{user_id}")
async def fetch_one_user(user_id: UUID):
    """GET method, which fetch one user from database (by user_id)"""
    return database.get_one_user(user_id)


@app.post("/api/v1/users/")
async def insert_user_data(user: User):
    """POST method to inserting data to database"""
    return database.join_user_data(user)


@app.delete("/api/v1/users/1/{user_id}")
async def delete_user(user_id: UUID):
    """DELETE method to deleting user data from database (by user_id)"""
    return database.delete_users(user_id)


@app.put("/api/v1/users/1/{user_id}")
async def update_user(user_id: UUID, user: User): # user_update: User
    """PUT method to update user data from database (by user_id)"""
    return database.update_users(user_id, user)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        reload=True,
        port=8000
    )
