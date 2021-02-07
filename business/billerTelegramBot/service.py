# used only for python >=3.6
from __future__ import annotations
from typing import Any, List, Optional

from abc import abstractmethod, ABCMeta
from typing import TYPE_CHECKING

from business.billerTelegramBot.model import BillerTelegramBot

# if TYPE_CHECKING:
#     from src.infrastructure.database.models.user import BillerTelegramBot


class BillerTelegramBotRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    async def create_biller_telegram_bot(self, billerTelegramBot: BillerTelegramBot) -> BillerTelegramBot:
        raise NotImplementedError

    @abstractmethod
    async def get_by_group_id(self, id: str) -> BillerTelegramBot:
        raise NotImplementedError


class BillerTelegramBotServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    async def create_biller_telegram_bot(self, billerTelegramBot: BillerTelegramBot) -> BillerTelegramBot:
        raise NotImplementedError

    @abstractmethod
    async def get_by_group_id(self, id: str) -> Optional[BillerTelegramBot]:
        raise NotImplementedError


class BillerTelegramBotService(BillerTelegramBotServiceInterface):
    def __init__(self, biller_tele_bot_repo: BillerTelegramBotRepositoryInterface):
        self.__repo = biller_tele_bot_repo

    async def create_biller_telegram_bot(self, billerTelegramBot: BillerTelegramBot) -> BillerTelegramBot:
        billerTelegramBot = await self.__repo.create_biller_telegram_bot(billerTelegramBot)
        return BillerTelegramBot.from_orm(billerTelegramBot)

    async def get_by_group_id(self, id: str) -> Optional[BillerTelegramBot]:
        billerTelegramBot = await self.__repo.get_by_group_id(id)
        if billerTelegramBot:
            return BillerTelegramBot.from_orm(billerTelegramBot)
        else:
            return None

