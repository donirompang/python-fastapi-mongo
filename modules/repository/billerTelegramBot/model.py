from mongoengine import *
import datetime

class PriceChangesPattern(EmbeddedDocument):
    keyword = StringField(max_length=200, required=True)
    regex_pattern = StringField(max_length=200, required=True)


class BillerTelegramBot(Document):
    telegram_group_id = StringField(max_length=200, required=True)
    biller_name = StringField(max_length=200, required=True)
    price_changes_pattern = EmbeddedDocumentListField(PriceChangesPattern)
