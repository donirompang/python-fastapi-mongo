from mongoengine import *
import datetime
from business.billerPriceChanges.model import BillerPriceChanges as BillerPriceChangesBM


class BillerPriceChanges(Document):
    product_alias = StringField(max_length=200, required=True)
    price = FloatField(required=True)
    biller_name = StringField(max_length=200, required=True)

    def to_business_model(self) -> BillerPriceChangesBM:
        '''
        This is for convert from DB model to business model
        '''
        dataDict = self.to_mongo().to_dict()
        return BillerPriceChangesBM(
            product_alias=dataDict["product_alias"],
            price=dataDict["price"],
            biller_name=dataDict["biller_name"],
        )
