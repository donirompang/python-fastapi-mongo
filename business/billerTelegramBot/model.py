from typing import Optional
from pydantic import BaseModel, EmailStr


class BillerTelegramBot(BaseModel):
    group_id: str
    name: str

    class Config:
        allow_mutation = False
        orm_mode = True