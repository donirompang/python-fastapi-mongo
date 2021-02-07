from fastapi import FastAPI
from api.api import api_router


def create_app() -> FastAPI:
    try:
        app = FastAPI()
        app.include_router(api_router, prefix="/api/v1")
    except Exception as e:
        pass
    return app


app: FastAPI = create_app()