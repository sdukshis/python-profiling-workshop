import random
import asyncio

from fastapi import FastAPI, HTTPException


class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.friends = list()

    def add_friend(self, friend_id: int):
        if friend_id not in self.friends:
            self.friends.append(friend_id)
    

users: dict[int, User] = {}


app = FastAPI()

@app.on_event("startup")
async def populate_users():
    for i in range(100):
        users[i] = User(i, "John")
    
    for user_id in users.keys():
        for _ in range(random.randint(1, 7)):
            users[user_id].add_friend(random.choice(users).id)

@app.get("/users/{user_id}")
async def user(user_id:int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    await asyncio.sleep(0.2)
    return {"user_id": user_id, "name": users[user_id].name}


@app.get("/friends/{user_id}")
async def friends(user_id:int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    await asyncio.sleep(1)
    return users[user_id].friends

