# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExchangeAccountBalance", "Balance"]


class Balance(BaseModel):
    asset: str
    """Asset"""

    borrowed: float
    """Borrowed balance from exchange"""

    free: float
    """Free balance"""

    locked: float
    """Locked balance"""

    net: float
    """Net Balance, net = total - borrowed"""

    total: float
    """Total available balance"""


class ExchangeAccountBalance(BaseModel):
    balances: List[Balance]
    """List of balances"""

    exchange_account_id: str = FieldInfo(alias="exchangeAccountId")
    """Exchange account ID"""
