from fastapi import APIRouter

from api.endpoints.billerTelegramBot.controller import router

api_router = APIRouter()
api_router.include_router(router, prefix="/telegram", tags=["telegram"])
