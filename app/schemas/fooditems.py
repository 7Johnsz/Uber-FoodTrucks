from pydantic import BaseModel

class Menu(BaseModel):
    food_type: str
    
    class Config:
        extra = "forbid"