from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from bson import ObjectId

class Product(BaseModel):
    id: Optional[ObjectId] = Field(None, alias='_id')
    name: str
    price: float
    description: Optional[str] = None
    stock: int

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )

class ProductDBModel(Product):
    def model_dump(self, *, mode = 'python', include = None, exclude = None, context = None, by_alias = None, exclude_unset = False, exclude_defaults = False, exclude_none = False, exclude_computed_fields = False, round_trip = False, warnings = True, fallback = None, serialize_as_any = False, polymorphic_serialization = None):
        data = super().model_dump(mode=mode, include=include, exclude=exclude, context=context, by_alias=by_alias, exclude_unset=exclude_unset, exclude_defaults=exclude_defaults, exclude_none=exclude_none, exclude_computed_fields=exclude_computed_fields, round_trip=round_trip, warnings=warnings, fallback=fallback, serialize_as_any=serialize_as_any, polymorphic_serialization=polymorphic_serialization)
        if self.id:
            data['_id'] = str(data['_id'])
        return data
    
class UpdateProduct(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    stock: Optional[int] = None

