import requests

def get_names():
    return requests.get("https://tasterai.herokuapp.com/food").json()

def get_kilocalories(name):
    return requests.get(f"https://tasterai.herokuapp.com/food/kilocalories/{name}").json()

def get_grease(name):
    return requests.get(f"https://tasterai.herokuapp.com/food/grease/{name}").json()

def get_saturated(name):
    return requests.get(f"https://tasterai.herokuapp.com/food/saturated/{name}").json()

def get_carbohydrates(name):
    return requests.get(f"https://tasterai.herokuapp.com/food/carbohydrates/{name}").json()

def get_sugar(name):
    return requests.get(f"https://tasterai.herokuapp.com/food/sugar/{name}").json()

def get_fiber(name):
    return requests.get(f"https://tasterai.herokuapp.com/food/fiber/{name}").json()

def get_protein(name):
    return requests.get(f"https://tasterai.herokuapp.com/food/protein/{name}").json()

def get_sal(name):
    return requests.get(f"https://tasterai.herokuapp.com/food/sal/{name}").json()

def get_name_recipes(name):
    return requests.get(f"https://tasterai.herokuapp.com/recipes/{name}").json()

def get_preparation_recipes(name):
    return requests.get(f"https://tasterai.herokuapp.com/recipes/preparation/{name}").json()

def get_cooking_recipes(name):
    return requests.get(f"https://tasterai.herokuapp.com/recipes/cooking/{name}").json()

def get_ingredients_recipes(name):
    return requests.get(f"https://tasterai.herokuapp.com/recipes/ingredients/{name}").json()

def get_elaboration_recipes(name):
    return requests.get(f"https://tasterai.herokuapp.com/recipes/elaboration/{name}").json()

def post_add_recipes(dict):
    return requests.post(f"https://tasterai.herokuapp.com/add/recipe",json=dict).json()