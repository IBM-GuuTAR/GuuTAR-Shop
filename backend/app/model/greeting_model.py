from pydantic import BaseModel

class CreateGreeting(BaseModel):
    greeting: str
    class Config:
        orm_mode=True