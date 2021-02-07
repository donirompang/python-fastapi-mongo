from typing import Optional
from mongoengine import connect
from modules.repository.billerTelegramBot.mongo_model import BillerTelegramBot as ModelDB
from business.billerTelegramBot.service import BillerTelegramBotRepositoryInterface
from business.billerTelegramBot.model import BillerTelegramBot

# connect mongo
connect('project1', host='mongodb://localhost/rigorous')

class BillerTelegramBotMongoRepository(BillerTelegramBotRepositoryInterface):
    async def create_biller_telegram_bot(self, billerTelegramBot: BillerTelegramBot) -> BillerTelegramBot:
        result = ModelDB(group_id=billerTelegramBot.group_id, name=billerTelegramBot.name)
        result.save()
        return BillerTelegramBot.parse_obj(result.to_mongo())

    async def get_by_group_id(self, id: str) -> BillerTelegramBot:
        result = ModelDB.objects.get(group_id=id)
        return BillerTelegramBot.parse_obj(result.to_mongo())

