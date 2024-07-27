from abc import ABC, abstractmethod
from typing import List
from models import Currency

class WalletInterface(ABC):
    @abstractmethod
    def add_currency(self, currency: Currency) -> None:
        ...
    
    @abstractmethod
    def set_rate(self, currency_name: str, currency_rate: float) -> None:
        ...
    
    @abstractmethod
    def set_currency(self, currency_name: str, currency_value: float) -> None:
        ...
    
    @abstractmethod
    def modify_currency(self, currency_name: str, currency_value: float) -> None:
        ...

    @abstractmethod
    def get_currency(self, currency_name: str) -> Currency:
        ...

    @abstractmethod
    def __str__(self) -> str:
        ...
    
    @abstractmethod
    def keys(self) -> List[str]:
        ...
    
    @abstractmethod
    def values(self) -> List[Currency]:
        ...
    
    @abstractmethod
    def is_changed(self) -> bool:
        ...