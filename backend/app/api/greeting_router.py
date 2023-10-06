from fastapi import APIRouter, Body

from app.service.greeting_service import greeting_service, create_greeting_service
from app.model.greeting_model import CreateGreeting


router = APIRouter()

@router.get("/")
def greeting():
    return greeting_service()

@router.post("/new_greeting")
def create_greeting(greeting: CreateGreeting = Body(...)):
    return create_greeting_service(greeting)