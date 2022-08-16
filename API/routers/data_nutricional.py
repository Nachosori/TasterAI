from datetime import date
from tokenize import Name
from fastapi import APIRouter, Body, Header
from database.mongodb import db
from bson import json_util
from models.data_nutricional import foods, Recipes
from json import loads


router = APIRouter()

# Devuelve una lista de alimentos.

@router.get("/food")
def get_list_food():
    resul = list(db["data_aliments"].find({}).distinct("type"))
    return loads(json_util.dumps(resul))

@router.get("/food/kilocalories/{name}")
def get_data_food(name):
    resul = list(db["data_aliments"].find({"name":name}).distinct(f"kilocalories"))
    return loads(json_util.dumps(resul))

@router.get("/food/grease/{name}")
def get_data_food(name):
    resul = list(db["data_aliments"].find({"name":name}).distinct(f"grease"))
    return loads(json_util.dumps(resul))

@router.get("/food/saturated/{name}")
def get_data_food(name):
    resul = list(db["data_aliments"].find({"name":name}).distinct(f"saturated fat"))
    return loads(json_util.dumps(resul))

@router.get("/food/carbohydrates/{name}")
def get_data_food(name):
    resul = list(db["data_aliments"].find({"name":name}).distinct(f"carbohydrates"))
    return loads(json_util.dumps(resul))

@router.get("/food/sugar/{name}")
def get_data_food(name):
    resul = list(db["data_aliments"].find({"name":name}).distinct(f"sugar"))
    return loads(json_util.dumps(resul))

@router.get("/food/fiber/{name}")
def get_data_food(name):
    resul = list(db["data_aliments"].find({"name":name}).distinct(f"fiber"))
    return loads(json_util.dumps(resul))

@router.get("/food/protein/{name}")
def get_data_food(name):
    resul = list(db["data_aliments"].find({"name":name}).distinct(f"protein"))
    return loads(json_util.dumps(resul))

@router.get("/food/sal/{name}")
def get_data_food(name):
    resul = list(db["data_aliments"].find({"name":name}).distinct(f"sal"))
    return loads(json_util.dumps(resul))

@router.get("/recipes/{food}")
def get_data_recipes(food):
    resul = list(db["recipes"].find({"type":food}).distinct("name"))
    return loads(json_util.dumps(resul))

@router.get("/recipes/preparation/{food}")
def get_data_recipes(food):
    resul = list(db["recipes"].find({"name":food}).distinct("preparation"))
    return loads(json_util.dumps(resul))

@router.get("/recipes/cooking/{food}")
def get_data_recipes(food):
    resul = list(db["recipes"].find({"name":food}).distinct("cooking"))
    return loads(json_util.dumps(resul))

@router.get("/recipes/ingredients/{food}")
def get_data_recipes(food):
    resul = list(db["recipes"].find({"name":food}).distinct("ingredients"))
    return loads(json_util.dumps(resul))

@router.get("/recipes/elaboration/{food}")
def get_data_recipes(food):
    resul = list(db["recipes"].find({"name":food}).distinct("elaboration"))
    return loads(json_util.dumps(resul))

@router.post("/add/recipe")
def add_recipe(recipe:Recipes):
    print(recipe)
    resultado = db["recipes"].insert_one(recipe.dict())
    return {
        "message":"Añadido correctamente",
        "id":f"{resultado.inserted_id}"
    }