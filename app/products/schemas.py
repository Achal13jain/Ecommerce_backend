from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    category: str
    image_url: Optional[str]

class ProductUpdate(ProductCreate):
    pass

class ProductOut(ProductCreate):
    id: int

    class Config:
        from_attributes = True

class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int
    category: str
    image_url: str

    class Config:
        orm_mode = True