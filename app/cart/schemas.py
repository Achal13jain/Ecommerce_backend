from pydantic import BaseModel, Field
from typing import Optional, List

class CartItemCreate(BaseModel):
    product_id: int
    quantity: int= Field(..., gt=0, description="Quantity must be greater than zero")
    
class AddToCartRequest(BaseModel):
    items: List[CartItemCreate]

class CartItemOut(BaseModel):
    id: int
    product_id: int
    quantity: int

    class Config:
        from_attributes = True


class CartOut(BaseModel):
    id: int
    user_id: int
    items: List[CartItemOut] = []

    class Config:
        from_attributes = True
