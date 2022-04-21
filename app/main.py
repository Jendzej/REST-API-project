from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Gender, Role
from uuid import UUID

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


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def registger_user(user: User):
    db.append(user)
    return {"user_id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id {user_id} does not exists"
    )
