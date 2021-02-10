from mongoengine import *
import datetime
from business.billerTelegramBot.model import BillerTelegramBot as BillerTelegramBotBM

class PriceChangesPattern(EmbeddedDocument):
    keyword = StringField(max_length=200, required=True)
    regex_pattern = StringField(max_length=200, required=True)


class BillerTelegramBot(Document):
    telegram_group_id = StringField(max_length=200, required=True)
    biller_name = StringField(max_length=200, required=True)
    price_changes_pattern = EmbeddedDocumentListField(PriceChangesPattern)
    telegram_bot_token = StringField(max_length=200, required=True)

    def to_business_model(self) -> BillerTelegramBotBM:
        '''
        This is for convert from DB model to business model
        '''
        dataDict = self.to_mongo().to_dict()
        return BillerTelegramBotBM(
            telegram_group_id=dataDict["telegram_group_id"],
            biller_name=dataDict["biller_name"],
            telegram_bot_token=dataDict["telegram_bot_token"],
            price_changes_pattern=dataDict["price_changes_pattern"],
            id=str(dataDict["_id"])
        )
