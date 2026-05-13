from pydantic import BaseModel
from typing import Optional

class Category(BaseModel):
    category_id: Optional[int] = None
    name: str
    slug: Optional[str] = None
    description: Optional[str] = None

    

    