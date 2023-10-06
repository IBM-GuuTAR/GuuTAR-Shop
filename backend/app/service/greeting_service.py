from starlette.responses import JSONResponse
from fastapi import status

from app.model.greeting_model import CreateGreeting
from app.util.util_service import server_error
from app.database.redis import redis_get, redis_set

def greeting_service(): 
    try:
        greeting = redis_get('greeting')

        print(greeting)

        if greeting:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "data": { "greeting": greeting }
                }
            )
        else:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={
                    "message": "No greeting message"
                }
            )
    except Exception as e:
        return server_error(e)
    
def create_greeting_service(greeting: CreateGreeting): 
    try:
        greeting = greeting.model_dump()["greeting"]
        greeting = redis_set('greeting', greeting, 300)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": "Create greeting message!"
            }
        )
    except Exception as e:
        return server_error(e)