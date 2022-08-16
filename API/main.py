from fastapi import FastAPI
from routers import data_nutricional

app = FastAPI()
app.include_router(data_nutricional.router)

@app.get("/")
def raiz():
    return {
        "message":"Welcome to the TasterAI"
    }