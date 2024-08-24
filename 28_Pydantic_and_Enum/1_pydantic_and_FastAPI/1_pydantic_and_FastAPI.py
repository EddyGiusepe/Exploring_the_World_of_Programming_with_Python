#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Execução
========
uvicorn 1_pydantic_and_FastAPI:app --reload

ou

python 1_pydantic_and_FastAPI.py
"""
from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    name: str
    email: str


from fastapi import FastAPI, HTTPException

app = FastAPI(title='🤗 Using Pydantic with FastAPI 🤗',
              version='1.0.0',
              description="""Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro\n
              Lembrando o uso de Pydantic""")

# Lista para armazenar os usuários:
users = []

# Rota para criar um novo usuário:
@app.post("/create_a_new_user/", response_model=User)
def create_user(user: User):
    # Verifica se o ID já existe:
    if any(u.id == user.id for u in users):
        raise HTTPException(status_code=400, detail="User ID already exists")
    
    users.append(user)
    return user

# Rota para listar todos os usuários:
@app.get("/list_all_users/", response_model=List[User])
def get_users():
    return users



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)