import logging

from fastapi import status
from fastapi.responses import JSONResponse

def server_error(e: Exception):
    logging.error(e)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "message": "Server Error"
        }
    )