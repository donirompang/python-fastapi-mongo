from typing import List, Optional
import re
from fastapi import APIRouter, HTTPException, Depends, Path
from starlette import status

from utils.dependencies import get_biller_telegram_bot_service
from utils.dependencies import get_biller_price_changes_service
from business.billerTelegramBot.service import BillerTelegramBotServiceInterface
from business.billerPriceChanges.service import BillerPriceChangesServiceInterface
from business.billerTelegramBot.model import BillerTelegramBot
from business.billerPriceChanges.model import BillerPriceChanges
from business.billerTelegramBot.spec import UpsertBillerTelegramBotSpec
from api.endpoints.billerTelegramBot.request import TelegramCallback

router = APIRouter()


@router.post("", response_model=BillerTelegramBot)
async def create_biller_telegram_bot(upsertBillerTelegramBot: UpsertBillerTelegramBotSpec, billerTelegramBotService: BillerTelegramBotServiceInterface = Depends(get_biller_telegram_bot_service)) -> BillerTelegramBot:
    return billerTelegramBotService.create_biller_telegram_bot(upsertBillerTelegramBot)


@router.get("/group/{id}", response_model=BillerTelegramBot)
async def get_by_group_id(id: str, billerTelegramBotService: BillerTelegramBotServiceInterface = Depends(get_biller_telegram_bot_service)) -> Optional[BillerTelegramBot]:
    billerTelegramBot = billerTelegramBotService.get_by_group_id(id)
    if billerTelegramBot:
        return billerTelegramBot
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"billerTelegramBot with group_id:{id} not found",
    )

@router.get("", response_model=List[BillerTelegramBot])
async def get_user_by_id(billerTelegramBotService: BillerTelegramBotServiceInterface = Depends(get_biller_telegram_bot_service)) -> Optional[BillerTelegramBot]:
    return billerTelegramBotService.get_all()


@router.delete("/{id}")
async def delete_by_id(id: str, billerTelegramBotService: BillerTelegramBotServiceInterface = Depends(get_biller_telegram_bot_service)) -> Optional[BillerTelegramBot]:
    result = billerTelegramBotService.delete_by_id(id)
    return {"status" : result}



@router.get("/{id}", response_model=BillerTelegramBot)
async def get_by_id(id: str, billerTelegramBotService: BillerTelegramBotServiceInterface = Depends(get_biller_telegram_bot_service)) -> Optional[BillerTelegramBot]:
    billerTelegramBot = billerTelegramBotService.get_by_id(id)
    if billerTelegramBot:
        return billerTelegramBot
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"billerTelegramBot with id:{id} not found",
    )

@router.put("/{id}", response_model=BillerTelegramBot)
async def update_biller_telegram_bot(id: str, upsertBillerTelegramBot: UpsertBillerTelegramBotSpec, billerTelegramBotService: BillerTelegramBotServiceInterface = Depends(get_biller_telegram_bot_service)) -> Optional[BillerTelegramBot]:
    billerTelegramBot = billerTelegramBotService.update_biller_telegram_bot(id, upsertBillerTelegramBot)
    if billerTelegramBot:
        return billerTelegramBot
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"billerTelegramBot with id:{id} not found",
    )

@router.post("/callback")
async def telegram_callback(telegramCallback: TelegramCallback, billerPriceChangesService: BillerPriceChangesServiceInterface = Depends(get_biller_price_changes_service)):
    # if "perubahan" not in telegramCallback.message.text:
    #     return {"status" : "not ok"}

    # info = re.findall('(\w{5})-Rp.([0-9]{4,})', telegramCallback.message.text)
    # print(info)

    # for kp, harga in info:
    #     print(kp)
    #     print(harga)

    newBillerPriceChanges = BillerPriceChanges(
        biller_name="XXX",
        product_alias="SSS",
        price=232413
    )

    billerPriceChangesService.create_biller_price_changes(newBillerPriceChanges)

    return {"status" : "ok"}