from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field

class PriceChangesPattern(BaseModel):
    keyword: str
    regex_pattern: str

class BillerTelegramBot(BaseModel):
    id: str
    telegram_group_id: str
    biller_name: str
    price_changes_pattern : List[PriceChangesPattern]
    telegram_bot_token: str
    class Config:
        orm_mode = True
