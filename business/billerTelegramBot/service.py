from __future__ import annotations
from typing import Any, List, Optional
from abc import abstractmethod, ABCMeta
from typing import TYPE_CHECKING
from business.billerTelegramBot.model import BillerTelegramBot
from utils.helper import generate_id, validate_id

class BillerTelegramBotRepositoryInterface(metaclass=ABCMeta):
    '''
    BillerTelegramBot Repository Interface
    '''
    @abstractmethod
    def create_biller_telegram_bot(self, billerTelegramBot: BillerTelegramBot) -> BillerTelegramBot:
        raise NotImplementedError

    @abstractmethod
    def get_by_group_id(self, id: str) -> Optional[BillerTelegramBot]:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[BillerTelegramBot]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[BillerTelegramBot]:
        raise NotImplementedError


class BillerTelegramBotServiceInterface(metaclass=ABCMeta):
    '''
    BillerTelegramBot Service Interface
    '''
    @abstractmethod
    def create_biller_telegram_bot(self, upsertBillerTelegramBotSpec: UpsertBillerTelegramBotSpec) -> BillerTelegramBot:
        raise NotImplementedError

    @abstractmethod
    def get_by_group_id(self, id: str) -> Optional[BillerTelegramBot]:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[BillerTelegramBot]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[BillerTelegramBot]:
        raise NotImplementedError

    @abstractmethod
    def update_biller_telegram_bot(self, id: str, upsertBillerTelegramBotSpec: UpsertBillerTelegramBotSpec) -> Optional[BillerTelegramBot]:
        raise NotImplementedError


class BillerTelegramBotService(BillerTelegramBotServiceInterface):
    '''
    BillerTelegramBot Service Implementation
    '''
    def __init__(self, biller_tele_bot_repo: BillerTelegramBotRepositoryInterface):
        self.__repo = biller_tele_bot_repo

    def create_biller_telegram_bot(self, upsertBillerTelegramBot: UpsertBillerTelegramBotSpec) -> BillerTelegramBot:
        # create new BillerTelegramBot model
        newBillerTelegramBot = BillerTelegramBot(
            id=generate_id(),
            telegram_group_id=upsertBillerTelegramBot.telegram_group_id,
            biller_name=upsertBillerTelegramBot.biller_name,
            telegram_bot_token=upsertBillerTelegramBot.telegram_bot_token,
            price_changes_pattern=upsertBillerTelegramBot.price_changes_pattern
        )
        
        return self.__repo.create_biller_telegram_bot(newBillerTelegramBot)

    def get_by_group_id(self, id: str) -> Optional[BillerTelegramBot]:
        return self.__repo.get_by_group_id(id)

    def get_all(self) -> List[BillerTelegramBot]:
        return self.__repo.get_all()

    def delete_by_id(self, id: str) -> bool:
        # validate ID
        if not validate_id(id):
            return False
        return self.__repo.delete_by_id(id)

    def get_by_id(self, id: str) -> Optional[BillerTelegramBot]:
        # validate ID
        if not validate_id(id):
            return None
        return self.__repo.get_by_id(id)

    def update_biller_telegram_bot(self, id: str, upsertBillerTelegramBot: UpsertBillerTelegramBotSpec) -> Optional[BillerTelegramBot]:
        # validate ID
        if not validate_id(id):
            return None
        
        # get in DB
        billerTelegramBot = self.__repo.get_by_id(id)
        if not billerTelegramBot:
            return None
        
        # update neccesary data
        billerTelegramBot.telegram_bot_token = upsertBillerTelegramBot.telegram_bot_token
        billerTelegramBot.telegram_group_id = upsertBillerTelegramBot.telegram_group_id
        billerTelegramBot.biller_name = upsertBillerTelegramBot.biller_name
        billerTelegramBot.price_changes_pattern = upsertBillerTelegramBot.price_changes_pattern
        
        return self.__repo.create_biller_telegram_bot(billerTelegramBot)



