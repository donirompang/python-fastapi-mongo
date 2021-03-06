from fastapi import FastAPI
from api.api import api_router
from mongoengine import connect
from config.config import get_config
import telegram


def create_app() -> FastAPI:
    try:
        connect('project1', host='mongodb://localhost/rigorous')
        app = FastAPI()
        app.include_router(api_router, prefix="/api/v1")
    except Exception as e:
        print(e)
    return app


app: FastAPI = create_app()