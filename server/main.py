from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from pydantic import BaseModel
from typing import Union

import requests

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PROJECT_ID = "ae6e42f5-dafd-49fb-8524-3d6fa9bf2077"
PRIVATE_KEY = "218e1773-1939-451e-8415-0cc74de390df"

class User(BaseModel):
    username: str
    secret: str
    email: Union[str, None] = None
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None

@app.post('/login/')
async def login(user: User):
    response = requests.get('https://api.chatengine.io/users/me/',
        headers={
            "Project-ID": PROJECT_ID,
            "User-Name": user.username,
            "User-Secret": user.secret,
        }
    )
    # return response.json()
    return JSONResponse(content=response.json(), headers={"Access-Control-Allow-Origin": "*"})

@app.post('/signup/')
async def root(user: User):
    response = requests.post('https://api.chatengine.io/users/',
        data={
            "username": user.username,
            "secret": user.secret,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        },
        headers={
            "Private-Key": PRIVATE_KEY
        }
    )
    # return response.json()
    return JSONResponse(content=response.json(), headers={"Access-Control-Allow-Origin": "*"})

# uvicorn main:app --reload --port 3001