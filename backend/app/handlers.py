from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import item_router, greeting_router

app = FastAPI(
    title="GuuTAR Shop",
    docs_url="/api/docs"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(
    item_router.router,
    prefix="/api/items"
)

app.include_router(
    greeting_router.router,
    prefix="/api/greeting"
)