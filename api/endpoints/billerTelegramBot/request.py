from typing import Optional, List
from pydantic import BaseModel, EmailStr

class TelegramText(BaseModel):
    text: str

class TelegramCallback(BaseModel):
    message: TelegramText
    
