from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: Optional[int]
    name: str
    price: int
    picture_url: str
    class Config:
        orm_mode=True

class CreateNewItemPayload(BaseModel):
    name: str
    price: int
    picture_url: str
    class Config:
        orm_mode=True

class EditItemPayload(BaseModel):
    name: str
    price: int
    picture_url: str
    class Config:
        orm_mode=True

def item_model_to_dict(item: CreateNewItemPayload):
    return vars(Item(
        name=item.name,
        price=item.price,
        picture_url=item.picture_url
    ))