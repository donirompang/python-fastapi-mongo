from __future__ import annotations
from typing import Any, List, Optional

from abc import abstractmethod, ABCMeta
from typing import TYPE_CHECKING

from business.billerPriceChanges.model import BillerPriceChanges


class BillerPriceChangesRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def create_biller_price_changes(self, billerPriceChanges: BillerPriceChanges) -> BillerPriceChanges:
        raise NotImplementedError    


class BillerPriceChangesServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def create_biller_price_changes(self, billerPriceChanges: BillerPriceChanges) -> BillerPriceChanges:
        raise NotImplementedError


class BillerPriceChangesService(BillerPriceChangesServiceInterface):
    def __init__(self, repo: BillerPriceChangesRepositoryInterface):
        self.__repo = repo

    def create_biller_price_changes(self, billerPriceChanges: BillerPriceChanges) -> BillerPriceChanges:
        return self.__repo.create_biller_price_changes(billerPriceChanges)



