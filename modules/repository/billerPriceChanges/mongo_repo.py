from typing import Optional, List
from mongoengine import connect
from modules.repository.billerPriceChanges.model import BillerPriceChanges as ModelDB
from business.billerPriceChanges.service import BillerPriceChangesRepositoryInterface
from business.billerPriceChanges.model import BillerPriceChanges
import bson

class BillerPriceChangesMongoRepository(BillerPriceChangesRepositoryInterface):
    def create_biller_price_changes(self, billerPriceChanges: BillerPriceChanges) -> BillerPriceChanges:
        '''
        This is for create to DB
        '''
        # make object from DB Model
        result = ModelDB(
            biller_name=billerPriceChanges.biller_name,
            price=billerPriceChanges.price,
            product_alias=billerPriceChanges.product_alias
        )

        # save it to DB
        result.save()
        return result.to_business_model()

    