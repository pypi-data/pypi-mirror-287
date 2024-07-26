# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..market.kline import Kline
from ..trading.order import Order
from ..trading.quote import Quote
from ..market.orderbook import Orderbook
from ..trading.quote_request import QuoteRequest
from ..trading.execution_report import ExecutionReport
from ..exchange_account_portfolio import ExchangeAccountPortfolio
from ..trading.place_order_request import PlaceOrderRequest
from ..trading.cancel_order_request import CancelOrderRequest

__all__ = ["Event", "Payload"]

Payload = Union[
    QuoteRequest,
    PlaceOrderRequest,
    CancelOrderRequest,
    Quote,
    Order,
    ExecutionReport,
    ExchangeAccountPortfolio,
    Orderbook,
    Kline,
]


class Event(BaseModel):
    event_id: str = FieldInfo(alias="eventId")
    """A unique identifier for the event."""

    event_type: Literal[
        "cadenza.task.quoteRequestAck",
        "cadenza.task.placeOrderRequestAck",
        "cadenza.task.cancelOrderRequestAck",
        "cadenza.dropCopy.quote",
        "cadenza.dropCopy.order",
        "cadenza.dropCopy.portfolio",
        "cadenza.marketData.orderBook",
        "cadenza.marketData.kline",
    ] = FieldInfo(alias="eventType")
    """Event Type"""

    timestamp: int
    """Unix timestamp in milliseconds when the event was generated."""

    payload: Optional[Payload] = None
    """The actual data of the event, which varies based on the event type."""

    source: Optional[str] = None
    """The source system or module that generated the event."""
