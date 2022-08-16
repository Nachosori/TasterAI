from pydantic import BaseModel

class foods(BaseModel):
    food:str

class Recipes(BaseModel):
    type:str
    name:str
    preparation:str
    cooking:str
    ingredients:list
    elaboration:list

    
