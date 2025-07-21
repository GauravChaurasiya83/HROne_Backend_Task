from pydantic import BaseModel
from typing import List

class SizeSchema(BaseModel):
    size: str
    quantity: int

class ProductCreate(BaseModel):
    name: str
    price: float
    sizes: List[SizeSchema]

class ProductResponse(BaseModel):
    id: str
    name: str
    price: float
