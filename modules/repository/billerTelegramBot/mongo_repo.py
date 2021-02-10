from typing import Optional, List
from mongoengine import connect
from modules.repository.billerTelegramBot.model import BillerTelegramBot as ModelDB
from business.billerTelegramBot.service import BillerTelegramBotRepositoryInterface
from business.billerTelegramBot.model import BillerTelegramBot
import bson

class BillerTelegramBotMongoRepository(BillerTelegramBotRepositoryInterface):
    def create_biller_telegram_bot(self, billerTelegramBot: BillerTelegramBot) -> BillerTelegramBot:
        '''
        This is for create biller telegram bot to DB
        '''
        # make object from DB Model
        result = ModelDB(
            id=bson.objectid.ObjectId(billerTelegramBot.id),
            telegram_group_id=billerTelegramBot.telegram_group_id,
            biller_name=billerTelegramBot.biller_name,
            price_changes_pattern=[x.dict() for x in billerTelegramBot.price_changes_pattern],
            telegram_bot_token=billerTelegramBot.telegram_bot_token
        )

        # save it to DB
        result.save()
        return result.to_business_model()

    def get_by_group_id(self, id: str) -> Optional[BillerTelegramBot]:
        '''
        This is for get by group ID
        '''

        # get data in DB
        result = ModelDB.objects(telegram_group_id=id).first()
        
        # check and convert to business model
        if result:
            return result.to_business_model()
        return None

    def get_all(self) -> List[BillerTelegramBot]:
        '''
        This is for get all data
        '''

        # iterate cursor from DB
        listBiller = []
        for result in ModelDB.objects:
            listBiller.append(result.to_business_model())
        return listBiller

    def delete_by_id(self, id: str) -> bool:
        '''
        This is for delete data by ID
        '''

        # get data in DB
        result = ModelDB.objects(id=id).first()

        # delete it if exists
        if result:
            result.delete()
            return True
        return False

    def get_by_id(self, id: str) -> Optional[BillerTelegramBot]:
        '''
        This is for get data by ID
        '''

        # get data in DB
        result = ModelDB.objects(id=id).first()

        # check and convert it to business model
        if result:
            return result.to_business_model()
        return None

