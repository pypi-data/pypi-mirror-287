from fastapi import FastAPI, HTTPException, APIRouter
from contextlib import asynccontextmanager
import logging
import asyncio
from typing import List
from models import Wallet, ICurrency

logger = logging.getLogger(__name__)


class API:
    @asynccontextmanager
    async def __lifespan(self, app: FastAPI):
        loop = asyncio.get_event_loop()
        loop.create_task(self.__fetcher.fetch_rates())
        loop.create_task(self.__fetcher.print_total_every_minute())

        logger.info("Starting up")
        yield
        logger.info("Shutting down")
    
    def __init__(self, wallet: Wallet, fetcher):
        self.__wallet = wallet
        self.__fetcher = fetcher
        self.app = FastAPI(lifespan=self.__lifespan)

        self.__router = APIRouter()
        self.__router.add_api_route("/amount/get", self.__get_total_amount, methods=["GET"])
        self.__router.add_api_route("/{currency}/get", self.__get_currency_amount, methods=["GET"])
        self.__router.add_api_route("/amount/set", self.__set_currency_amount, methods=["POST"])
        self.__router.add_api_route("/modify", self.__modify_currency_amount, methods=["POST"])

        self.app.include_router(self.__router)

    def __get_currency_amount(self, currency: str):
        if currency not in self.__wallet.keys():
            raise HTTPException(status_code=404, detail="Currency not found")
        return { "name": currency.upper(), "value": self.__wallet.get_currency(currency).value }
    
    def __set_currency_amount(self, currencies: List[ICurrency]):
        for currency in currencies:
            if currency.name in self.__wallet.keys():
                self.__wallet.set_currency(currency.name, currency.value)
            else:
                logger.warning(f"'{currency.name}' not in list of currencies!")
        self.__fetcher.is_wallet_change()
        return { "status": "success" }
    
    def __modify_currency_amount(self, currencies: List[ICurrency]):
        for currency in currencies:
            if currency.name in self.__wallet.keys():
                self.__wallet.modify_currency(currency.name, currency.value)
            else:
                logger.warning(f"'{currency.name}' not in list of currencies!")
        self.__fetcher.is_wallet_change()
        return { "status": "success" }
    
    def __get_total_amount(self):
        return self.__fetcher.get_total()
