from pydantic import BaseModel
from typing import Dict


class ICurrency(BaseModel):
    name: str
    value: float


class Currency(ICurrency):
    rate: float


class TotalAmount(BaseModel):
    amount: Dict[str, float]
    rates: Dict[str, float]
    sum: Dict[str, float]


class ArgsModel(BaseModel):
    period: int
    debug: bool
    currencies: Dict[str, float]
