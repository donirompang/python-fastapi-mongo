from typing import Optional, List
from pydantic import BaseModel, EmailStr

class TelegramChat(BaseModel):
    id: int
    type: str

class TelegramText(BaseModel):
    text: str
    chat: TelegramChat

class TelegramCallback(BaseModel):
    message: TelegramText
    
