#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
from pydantic import BaseModel, Field, field_validator
from datetime import date, datetime
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    birth_date: date
    registration_date: datetime = Field(default_factory=datetime.now)
    age: Optional[int] = None

    @field_validator("email")
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError("Invalid email")
        return v.lower()
    
    @field_validator("age", mode="before")
    def calculate_age(cls, v, info):
        if v is None and "birth_date" in info.data:
            today = date.today()
            born = info.data["birth_date"]
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        return v
    
    @field_validator("registration_date")
    def ensure_registration_not_future(cls, v):
        if v > datetime.now():
            raise ValueError("The registration date cannot be in the future")
        return v
    

if __name__=="__main__":
    try:
        user = User(name="Eddy Giusepe",
                    email="EDDYGIUSEPE@gmail.com",
                    birth_date=date(1981, 9, 4)
                   )

        print(f"Usuário criado: {user}")
        print(f"Email normalizado: {user.email}")
        print(f"Idade calculada: {user.age}")
    except ValueError as e:
        print(f"Erro de validação: {e}")
        