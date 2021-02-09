from typing import Optional
from mongoengine import connect
from modules.repository.billerTelegramBot.model import BillerTelegramBot as ModelDB
from business.billerTelegramBot.service import BillerTelegramBotRepositoryInterface
from business.billerTelegramBot.model import BillerTelegramBot


class BillerTelegramBotMongoRepository(BillerTelegramBotRepositoryInterface):
    def create_biller_telegram_bot(self, billerTelegramBot: BillerTelegramBot) -> BillerTelegramBot:
        result = ModelDB(
            telegram_group_id=billerTelegramBot.telegram_group_id,
            biller_name=billerTelegramBot.biller_name,
            price_changes_pattern=[x.dict() for x in billerTelegramBot.price_changes_pattern]
        )
        result.save()
        return BillerTelegramBot.parse_obj(result.to_mongo())

    def get_by_group_id(self, id: str) -> BillerTelegramBot:
        result = ModelDB.objects.get(group_id=id)
        return BillerTelegramBot.parse_obj(result.to_mongo())

