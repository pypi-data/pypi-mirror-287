import httpx
import asyncio
import logging
from typing import Dict
from models import Currency, Wallet, TotalAmount

logger = logging.getLogger(__name__)


class Fetcher:
    URL = "https://www.cbr-xml-daily.ru/daily_json.js"

    def __init__(self, period: int, currencies: Dict[str, float], wallet: Wallet):
        self.__period = period
        self.__currencies = currencies
        self.__wallet = wallet

        if "rub" in currencies.keys():
            self.__wallet.add_currency(Currency(name="rub", rate=1, value=currencies["rub"]))
            del currencies["rub"]
    
    async def fetch_rates(self) -> None:
        while True:
            try:
                async with httpx.AsyncClient() as client:
                    response = await client.get(self.URL)
                    rates = response.json()["Valute"]
                    for currency in self.__currencies.keys():
                        if currency in self.__wallet.keys() and currency.upper() in rates.keys():
                            self.__wallet.set_rate(currency, rates[currency.upper()]["Value"])
                        elif currency not in self.__wallet.keys() and currency.upper() in rates.keys():
                            self.__wallet.add_currency(Currency(name=currency, rate=rates[currency.upper()]["Value"], value=self.__currencies[currency]))
                logger.info("Currency fetch success!")
            except Exception as e:
                logger.error(f"Failed to fetch rates: {e}")
            self.is_wallet_change()
            await asyncio.sleep(self.__period * 60)

    def is_wallet_change(self) -> None:
        if self.__wallet.is_changed():
            logger.info(self.get_total())

    async def print_total_every_minute(self) -> None:
        while True:
            await asyncio.sleep(60)
            logger.info(self.get_total())

    def get_total(self) -> TotalAmount:
        result = TotalAmount(amount={}, rates={}, sum={})
        local_currencies = list(self.__wallet.values())
        total = sum(currency.rate * currency.value for currency in local_currencies)
        for i in range(len(local_currencies)):
            result.amount[local_currencies[i].name] = local_currencies[i].value
            for j in range(i + 1, len(local_currencies)):
                result.rates[local_currencies[i].name + "-" + local_currencies[j].name] = round(local_currencies[j].rate / local_currencies[i].rate, 2)
            result.sum[local_currencies[i].name] = round(total / local_currencies[i].rate, 2)

        return result
