from mongoengine import *
import datetime

class BillerTelegramBot(Document):
    group_id = StringField(max_length=200, required=True)
    name = StringField(max_length=200, required=True)