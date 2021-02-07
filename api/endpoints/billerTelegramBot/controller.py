from typing import List, Optional

from fastapi import APIRouter, HTTPException, Depends
from starlette import status

from api.utils import get_biller_telegram_bot_service
from business.billerTelegramBot.service import BillerTelegramBotServiceInterface
from business.billerTelegramBot.model import BillerTelegramBot

router = APIRouter()


@router.post("", response_model=BillerTelegramBot)
async def create_user(billerTelegramBot: BillerTelegramBot, billerTelegramBotService: BillerTelegramBotServiceInterface = Depends(get_biller_telegram_bot_service)) -> BillerTelegramBot:
    return billerTelegramBotService.create_biller_telegram_bot(billerTelegramBot)


@router.get("")
async def home():
    return {"message": "Hello World!"}


@router.get("/{id}", response_model=BillerTelegramBot)
async def get_user_by_id(id: str, billerTelegramBotService: BillerTelegramBotServiceInterface = Depends(get_biller_telegram_bot_service)) -> Optional[BillerTelegramBot]:
    billerTelegramBot = await billerTelegramBotService.get_by_group_id(id)
    if billerTelegramBot:
        return billerTelegramBot
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"billerTelegramBot with id:{id} not found",
    )

