from typing import Optional, List
from pydantic import BaseModel, EmailStr

class PriceChangesPattern(BaseModel):
    keyword: str
    regex_pattern: str

class BillerTelegramBot(BaseModel):
    telegram_group_id: str
    biller_name: str
    price_changes_pattern : List[PriceChangesPattern]
