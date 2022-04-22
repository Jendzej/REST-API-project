"""Imported libraries and modules"""
from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException
from models import User, Gender, Role
from typing import Optional, List


app = FastAPI()

db: List[User] = [
    User(
            id=UUID("1f5dcdf0-7b97-4292-812e-0b82164c351d"),
            first_name="Jan",
            last_name="Kowalski",
            gender=Gender.male,
            roles=[Role.student]
    ),
    User(
            id=UUID("d0b84f45-6477-4d8d-ab5d-c9773f8a1ef9"),
            first_name="Aleksandra",
            last_name="Kowalska",
            gender=Gender.female,
            roles=[Role.admin, Role.user]
    )
]


@app.get("/api/v1/get")
async def fetch_users():
    """localhost:8000/api/v1/users  >  fetch users from db"""
    return db


@app.post("/api/v1/post")
async def registger_user(user: User):
    """localhost:8000/api/v1/users   >  adding users with POST"""
    db.append(user)
    return {"user_id": user.id}


@app.delete("/api/v1/delete")
async def delete_user(user_id: UUID):
    """localhost:8000/api/v1/users/{user_id}  >  delete users by user_id"""
    for user in db.copy():
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id {user_id} does not exists"
    )


@app.put("/api/v1/put")
async def update_user(user_update: User):
    for user in db:
        if user_update.id == user.id:
            updated = user_update 
            db.remove(user)
            db.append(updated)
            return db