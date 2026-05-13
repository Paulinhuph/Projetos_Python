from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional
from bson import ObjectId

class Sale(BaseModel):
    sale_date: date
    product_id: str
    quantity: int
    total_value: float

    model_config = ConfigDict(
        populate_by_name=True
        arbitrary_types_allowed=True
    )