from fastapi import APIRouter, Body

from app.service.item_service import get_item_service, create_new_item_service, edit_item_service, delete_item_service
from app.model.item_model import CreateNewItemPayload, EditItemPayload

router = APIRouter()

@router.get("/get-items")
def get_item(): 
    return get_item_service()

@router.post("/create-item")
def create_new_item(body: CreateNewItemPayload = Body(...)): 
    return create_new_item_service(body)

@router.patch("/edit-item/{item_id}")
def edit_item(item_id: str, body: EditItemPayload = Body(...)): 
    return edit_item_service(item_id, body)

@router.delete("/delete-item/{item_id}")
def delete_item(item_id: str): 
    return delete_item_service(int(item_id))