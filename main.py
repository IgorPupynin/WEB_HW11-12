import uvicorn
from fastapi import FastAPI

from src.routes import aut, contacts

app = FastAPI()

app.include_router(auth.router, prefix='/api')
app.include_router(contacts.router, prefix='/api')


@app.get("/")
def read_root():
    return {"message": "Hello world!"}


    