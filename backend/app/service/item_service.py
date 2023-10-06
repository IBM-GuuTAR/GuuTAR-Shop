from starlette.responses import JSONResponse
from typing import List
from fastapi import status

from app.model.item_model import Item, CreateNewItemPayload, EditItemPayload, item_model_to_dict
from app.util.util_service import server_error

items: List[Item] = [{"id": 0, "name": "Glass", "price": 20}, {"id": 1, "name": "Bowl", "price": 50}]

def get_item_service(): 
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "data": { "items": items }
            }
        )
    except Exception as e:
        return server_error(e)
    
def create_new_item_service(item: CreateNewItemPayload): 
    try:
        item = item_model_to_dict(item)
        item["id"] = len(items)

        items.append(item)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": "Create new item successful",
                "data": { "item": item }
            }
        )
    except Exception as e:
        return server_error(e)
    
def edit_item_service(item_id: int, item: EditItemPayload): 
    try:
        item = item_model_to_dict(item)

        is_found = False

        for idx, _item in enumerate(items):
            if _item["id"] == item_id:
                is_found = True
                items[idx] = item
                break
        
        if is_found:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "message": "Edit item successful",
                    "data": { "item": item }
                }
            )
        else:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={
                    "message": f"item_id: {item_id} not found",
                }
            )
    except Exception as e:
        return server_error(e)

def delete_item_service(item_id: int):
    try:
        is_found = False

        for idx, _item in enumerate(items):
            if _item["id"] == item_id:
                is_found = True
                item = _item
                items.pop(idx)
                break
        
        if is_found:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "message": "Delete item successful",
                    "data": { "item": item }
                }
            )
        else:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={
                    "message": f"item_id: {item_id} not found",
                }
            )
    except Exception as e:
        return server_error(e)