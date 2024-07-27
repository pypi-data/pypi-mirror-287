from typing import Dict, List
from models import Currency
from models.wallet_interface import WalletInterface

class Wallet(WalletInterface):
    def __init__(self):
        self.__wallet: Dict[str, Currency] = {}
        self.__changed = False
    
    def add_currency(self, currency: Currency) -> None:
        self.__wallet[currency.name] = currency
        self.__changed = True
    
    def set_rate(self, currency_name: str, currency_rate: float) -> None:
        if self.__wallet[currency_name].rate != currency_rate:
            self.__wallet[currency_name].rate = currency_rate
            self.__changed = True
    
    def set_currency(self, currency_name: str, currency_value: float) -> None:
        if self.__wallet[currency_name].value != currency_value:
            self.__wallet[currency_name].value = currency_value
            self.__changed = True
    
    def modify_currency(self, currency_name: str, currency_value: float) -> None:
        if currency_value != 0:
            self.__wallet[currency_name].value += currency_value
            self.__changed = True

    def get_currency(self, currency_name: str) -> Currency:
        return self.__wallet[currency_name]

    def __str__(self) -> str:
        return str(self.__wallet)
    
    def keys(self) -> List[str]:
        return list(self.__wallet.keys())
    
    def values(self) -> List[Currency]:
        return list(self.__wallet.values())
    
    def is_changed(self) -> bool:
        if self.__changed:
            self.__changed = False
            return True
        return False