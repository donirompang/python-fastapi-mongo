from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field

class BillerPriceChanges(BaseModel):
    product_alias: str
    price: float
    biller_name: str

