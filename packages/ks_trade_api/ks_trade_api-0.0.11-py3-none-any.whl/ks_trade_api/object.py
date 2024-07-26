from .constant import *
from dataclasses import dataclass, field, asdict
from datetime import datetime
import re
from typing import Union
from decimal import Decimal
from typing import Optional

"""
Basic data structure used for general trading function in the trading platform.
"""

from dataclasses import dataclass, field
from datetime import datetime
from logging import INFO
from ks_utility.jsons import json_dumps
from ks_utility.object import ErrorData
from ks_trade_api.constant import Direction, Exchange, Interval, Offset, Status, Product, OptionType, OrderType


ACTIVE_STATUSES = set([Status.SUBMITTING, Status.NOTTRADED, Status.PARTTRADED])


@dataclass
class BaseData:
    """
    Any data object needs a gateway_name as source
    and should inherit base data.
    """

    gateway_name: str

    extra: dict = field(default=None, init=False)

    def json(self) -> str:
        return json_dumps(self.dict())
    
    def dict(self) -> dict:
        return asdict(self)


@dataclass
class TickData(BaseData):
    """
    Tick data contains information about:
        * last trade in market
        * orderbook snapshot
        * intraday market statistics.
    """

    symbol: str
    exchange: Exchange
    datetime: datetime

    name: str = ""
    volume: float = 0
    turnover: float = 0
    open_interest: float = 0
    last_price: float = 0
    last_volume: float = 0
    limit_up: float = 0
    limit_down: float = 0

    open_price: float = 0
    high_price: float = 0
    low_price: float = 0
    pre_close: float = 0

    bid_price_1: float = 0
    bid_price_2: float = 0
    bid_price_3: float = 0
    bid_price_4: float = 0
    bid_price_5: float = 0

    ask_price_1: float = 0
    ask_price_2: float = 0
    ask_price_3: float = 0
    ask_price_4: float = 0
    ask_price_5: float = 0

    bid_volume_1: float = 0
    bid_volume_2: float = 0
    bid_volume_3: float = 0
    bid_volume_4: float = 0
    bid_volume_5: float = 0

    ask_volume_1: float = 0
    ask_volume_2: float = 0
    ask_volume_3: float = 0
    ask_volume_4: float = 0
    ask_volume_5: float = 0

    localtime: datetime = None

    def __post_init__(self) -> None:
        """"""
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"


@dataclass
class BarData(BaseData):
    """
    Candlestick bar data of a certain trading period.
    """

    symbol: str
    exchange: Exchange
    datetime: datetime

    interval: Interval = None
    volume: float = 0
    turnover: float = 0
    open_interest: float = 0
    open_price: float = 0
    high_price: float = 0
    low_price: float = 0
    close_price: float = 0

    def __post_init__(self) -> None:
        """"""
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"


@dataclass
class OrderData(BaseData):
    """
    Order data contains information for tracking lastest status
    of a specific order.
    """

    symbol: str
    exchange: Exchange
    orderid: str

    type: OrderType = OrderType.LIMIT
    direction: Direction = None
    offset: Offset = Offset.NONE
    price: float = 0
    volume: float = 0
    traded: float = 0
    status: Status = Status.SUBMITTING
    datetime: datetime = None
    reference: str = ""

    def __post_init__(self) -> None:
        """"""
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"
        self.vt_orderid: str = f"{self.gateway_name}.{self.orderid}"

    def is_active(self) -> bool:
        """
        Check if the order is active.
        """
        return self.status in ACTIVE_STATUSES

    def create_cancel_request(self) -> "CancelRequest":
        """
        Create cancel request object from order.
        """
        req: CancelRequest = CancelRequest(
            orderid=self.orderid, symbol=self.symbol, exchange=self.exchange, gateway_name=self.gateway_name
        )
        return req


@dataclass
class TradeData(BaseData):
    """
    Trade data contains information of a fill of an order. One order
    can have several trade fills.
    """

    symbol: str
    exchange: Exchange
    orderid: str
    tradeid: str
    direction: Direction = None

    offset: Offset = Offset.NONE
    price: float = 0
    volume: float = 0
    datetime: datetime = None

    def __post_init__(self) -> None:
        """"""
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"
        self.vt_orderid: str = f"{self.gateway_name}.{self.orderid}"
        self.vt_tradeid: str = f"{self.gateway_name}.{self.tradeid}"


@dataclass
class PositionData(BaseData):
    """
    Position data is used for tracking each individual position holding.
    """

    symbol: str
    exchange: Exchange
    direction: Direction

    volume: float = 0
    frozen: float = 0
    price: float = 0
    pnl: float = 0
    yd_volume: float = 0

    def __post_init__(self) -> None:
        """"""
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"
        self.vt_positionid: str = f"{self.gateway_name}.{self.vt_symbol}.{self.direction.value}"


@dataclass
class AccountData(BaseData):
    """
    Account data contains information about balance, frozen and
    available.
    """

    accountid: str

    balance: float = 0
    frozen: float = 0

    def __post_init__(self) -> None:
        """"""
        self.available: float = self.balance - self.frozen
        self.vt_accountid: str = f"{self.gateway_name}.{self.accountid}"


@dataclass
class LogData(BaseData):
    """
    Log data is used for recording log messages on GUI or in log files.
    """

    msg: str
    level: int = INFO

    def __post_init__(self) -> None:
        """"""
        self.time: datetime = datetime.now()


@dataclass
class ContractData(BaseData):
    """
    Contract data contains basic information about each contract traded.
    """

    symbol: str
    exchange: Exchange
    name: str
    product: Product
    size: float
    pricetick: float

    min_volume: float = 1           # minimum trading volume of the contract
    stop_supported: bool = False    # whether server supports stop order
    net_position: bool = False      # whether gateway uses net position volume
    history_data: bool = False      # whether gateway provides bar history data

    option_strike: float = 0
    option_underlying: str = ""     # vt_symbol of underlying contract
    option_type: OptionType = None
    option_listed: datetime = None
    option_expiry: datetime = None
    option_portfolio: str = ""
    option_index: str = ""          # for identifying options with same strike price

    def __post_init__(self) -> None:
        """"""
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"


@dataclass
class QuoteData(BaseData):
    """
    Quote data contains information for tracking lastest status
    of a specific quote.
    """

    symbol: str
    exchange: Exchange
    quoteid: str

    bid_price: float = 0.0
    bid_volume: int = 0
    ask_price: float = 0.0
    ask_volume: int = 0
    bid_offset: Offset = Offset.NONE
    ask_offset: Offset = Offset.NONE
    status: Status = Status.SUBMITTING
    datetime: datetime = None
    reference: str = ""

    def __post_init__(self) -> None:
        """"""
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"
        self.vt_quoteid: str = f"{self.gateway_name}.{self.quoteid}"

    def is_active(self) -> bool:
        """
        Check if the quote is active.
        """
        return self.status in ACTIVE_STATUSES

    def create_cancel_request(self) -> "CancelRequest":
        """
        Create cancel request object from quote.
        """
        req: CancelRequest = CancelRequest(
            orderid=self.quoteid, symbol=self.symbol, exchange=self.exchange
        )
        return req


@dataclass
class SubscribeRequest:
    """
    Request sending to specific gateway for subscribing tick data update.
    """

    symbol: str
    exchange: Exchange

    def __post_init__(self) -> None:
        """"""
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"


@dataclass
class OrderRequest:
    """
    Request sending to specific gateway for creating a new order.
    """

    symbol: str
    exchange: Exchange
    direction: Direction
    type: OrderType
    volume: float
    price: float = 0
    offset: Offset = Offset.NONE
    reference: str = ""

    def __post_init__(self) -> None:
        """"""
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"

    def create_order_data(self, orderid: str, gateway_name: str) -> OrderData:
        """
        Create order data from request.
        """
        order: OrderData = OrderData(
            symbol=self.symbol,
            exchange=self.exchange,
            orderid=orderid,
            type=self.type,
            direction=self.direction,
            offset=self.offset,
            price=self.price,
            volume=self.volume,
            reference=self.reference,
            gateway_name=gateway_name,
        )
        return order


@dataclass
class CancelRequest:
    """
    Request sending to specific gateway for canceling an existing order.
    """

    orderid: str
    symbol: str
    exchange: Exchange
    gateway_name: str

    def __post_init__(self) -> None:
        """"""
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"
        self.vt_orderid: str = f"{self.gateway_name}.{self.orderid}"


@dataclass
class HistoryRequest:
    """
    Request sending to specific gateway for querying history data.
    """

    symbol: str
    exchange: Exchange
    start: datetime
    end: datetime = None
    interval: Interval = None

    def __post_init__(self) -> None:
        """"""
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"


@dataclass
class QuoteRequest:
    """
    Request sending to specific gateway for creating a new quote.
    """

    symbol: str
    exchange: Exchange
    bid_price: float
    bid_volume: int
    ask_price: float
    ask_volume: int
    bid_offset: Offset = Offset.NONE
    ask_offset: Offset = Offset.NONE
    reference: str = ""

    def __post_init__(self) -> None:
        """"""
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"

    def create_quote_data(self, quoteid: str, gateway_name: str) -> QuoteData:
        """
        Create quote data from request.
        """
        quote: QuoteData = QuoteData(
            symbol=self.symbol,
            exchange=self.exchange,
            quoteid=quoteid,
            bid_price=self.bid_price,
            bid_volume=self.bid_volume,
            ask_price=self.ask_price,
            ask_volume=self.ask_volume,
            bid_offset=self.bid_offset,
            ask_offset=self.ask_offset,
            reference=self.reference,
            gateway_name=gateway_name,
        )
        return quote


@dataclass
class MyBookData(BaseData):
    symbol: str
    exchange: Exchange
    datetime: datetime
    localtime: datetime = None
    name: str = ""

    bid_price_1: Decimal = Decimal('0')
    bid_price_2: Decimal = Decimal('0')
    bid_price_3: Decimal = Decimal('0')
    bid_price_4: Decimal = Decimal('0')
    bid_price_5: Decimal = Decimal('0')

    ask_price_1: Decimal = Decimal('0')
    ask_price_2: Decimal = Decimal('0')
    ask_price_3: Decimal = Decimal('0')
    ask_price_4: Decimal = Decimal('0')
    ask_price_5: Decimal = Decimal('0')

    bid_volume_1: Decimal = Decimal('0')
    bid_volume_2: Decimal = Decimal('0')
    bid_volume_3: Decimal = Decimal('0')
    bid_volume_4: Decimal = Decimal('0')
    bid_volume_5: Decimal = Decimal('0')

    ask_volume_1: Decimal = Decimal('0')
    ask_volume_2: Decimal = Decimal('0')
    ask_volume_3: Decimal = Decimal('0')
    ask_volume_4: Decimal = Decimal('0')
    ask_volume_5: Decimal = Decimal('0')

    def __post_init__(self) -> None:
        """"""
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"

@dataclass
class MyTickData(MyBookData):
    volume: Decimal = Decimal('0')
    turnover: Decimal = Decimal('0')
    open_interest: Decimal = Decimal('0')
    last_price: Decimal = Decimal('0')
    last_volume: Decimal = Decimal('0')
    limit_up: Decimal = Decimal('0')
    limit_down: Decimal = Decimal('0')
    open_price: Decimal = Decimal('0')
    high_price: Decimal = Decimal('0')
    low_price: Decimal = Decimal('0')
    pre_close: Decimal = Decimal('0')

    settlement_price: float = 0
    pre_settlement_price: float = 0

@dataclass
class MyRawTickData(BaseData):
    symbol: str
    exchange: Exchange
    datetime: datetime
    localtime: datetime = None
    name: str = ""
    
    volume: Decimal = Decimal('0')
    turnover: Decimal = Decimal('0')
    open_interest: Decimal = Decimal('0')
    last_price: Decimal = Decimal('0')
    last_volume: Decimal = Decimal('0')
    limit_up: Decimal = Decimal('0')
    limit_down: Decimal = Decimal('0')
    open_price: Decimal = Decimal('0')
    high_price: Decimal = Decimal('0')
    low_price: Decimal = Decimal('0')
    pre_close: Decimal = Decimal('0')

    settlement_price: float = 0
    pre_settlement_price: float = 0

    def __post_init__(self) -> None:
        """"""
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"

@dataclass
class MyOrderData(OrderData):
    # todo 增加
    # frozen_margin: float = 0
    # frozen_commission: float = 0

    price: Decimal = Decimal('0')
    volume: Decimal = Decimal('0')
    traded: Decimal = Decimal('0')


    error: str = ''
    order_sys_id: str = ''
    profit_price: Union[Decimal, None] = None # My.add 止盈价
    loss_price: Union[Decimal, None] = None # My.add 止损价
    positionids: list[str] = field(default_factory=list)
    
    
    def __post_init__(self) -> None:
        """"""
        self.exchange: Exchange = EXCHANGE_MAP[self.exchange] if type(self.exchange) is str else self.exchange
        self.type: OrderType = ORDER_TYPE_MAP[self.type] if type(self.type) is str else self.type
        self.direction: Direction = DIRECTION_MAP[self.direction] if type(self.direction) is str else self.direction
        self.offset: Offset = OFFSET_MAP[self.offset] if type(self.offset) is str else self.offset
        self.status: Offset = STATUS_MAP[self.status] if type(self.status) is str else self.status
        self.vt_positionids: list[str] = [f"{self.gateway_name}.{x}" for x in self.positionids]
        if isinstance(self.datetime, str):
            self.datetime: datetime = datetime.strptime(self.datetime, DATETIME_FMT) if self.datetime else ''
        if self.datetime is None:
            self.datetime = datetime.now().astimezone(CHINA_TZ)

        super().__post_init__()

@dataclass
class MyTradeData(TradeData):
    price: Decimal = Decimal('0')
    volume: Decimal = Decimal('0')

    position_price: Decimal = Decimal('0')
    positionid: str = ''

    def __post_init__(self) -> None:
        """"""
        self.exchange: Exchange = EXCHANGE_MAP[self.exchange]
        self.direction: Direction = DIRECTION_MAP[self.direction]
        self.offset: Offset = OFFSET_MAP[self.offset]
        if isinstance(self.datetime, str):
            self.datetime: datetime = datetime.strptime(self.datetime, DATETIME_FMT)
        # 先要获取exchange的enum，才能拼接vt_symbol
        super().__post_init__()
        matched = re.search(r'_((\d*-*)+)$', self.positionid)
        self.position_date: str = matched[1] if matched else ''

@dataclass
class MyPositionData(BaseData):
    """
    Trade data contains information of a fill of an order. One order
    can have several trade fills.
    """

    symbol: str
    exchange: Exchange
    direction: Direction = None

    pnl: float = 0
    yd_volume: Decimal = Decimal('0')

    price: Decimal = Decimal('0')
    volume: Decimal = Decimal('0')
    frozen: Decimal = Decimal('0')
    orderids: list[str] = field(default_factory=list)
    available: Decimal = Decimal('0')
    margin: float = 0
    profit: float = 0 # 持仓盈亏
    settle_profit: float = 0 # 盯市盈亏
    date: str = ''
    profit_price: Union[float, None] = None # My.add 止盈价
    loss_price: Union[float, None] = None # My.add 止损价

    def __post_init__(self) -> None:
        """"""
        self.exchange: Exchange = EXCHANGE_MAP[self.exchange]
        self.direction: Direction = DIRECTION_MAP[self.direction]
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"
        self.vt_orderids: list[str] = [f"{self.gateway_name}.{x}" for x in self.orderids]
        self.positionid: str = f"{self.symbol}_{self.exchange.value}_{self.direction.name}_{self.date}"
        if self.volume > 0:
            self.available: float = self.volume - self.frozen
        else:
            self.available: float = self.volume + self.frozen
        self.vt_positionid: str = f"{self.gateway_name}.{self.positionid}"


@dataclass
class MyMarginRateData(BaseData):
    """
    保证金费率
    """

    symbol: str
    exchange: Exchange
    
    long_margin_ratio_by_money: float = 0
    long_margin_ratio_by_volume: float = 0
    short_margin_ratio_by_money: float = 0
    short_margin_ratio_by_volume: float = 0

    def __post_init__(self) -> None:
        """"""
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"

@dataclass
class MyCommissionRateData(BaseData):
    """
    手续费率
    """

    symbol: str
    exchange: Exchange
    
    open_ratio_by_money: float = 0
    open_ratio_by_volume: float = 0
    close_ratio_by_money: float = 0
    close_ratio_by_volume: float = 0
    close_today_ratio_by_money: float = 0
    close_today_ratio_by_volume: float = 0

    def __post_init__(self) -> None:
        """"""
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"

@dataclass
class MyOptionInstrTradeCost(BaseData):
    """
    保证金费率
    """

    symbol: str
    exchange: Exchange
    
    fixed_margin: float = 0
    mini_margin: float = 0

    def __post_init__(self) -> None:
        """"""
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"

@dataclass
class MyPushData(BaseData):
    """
    Log data is used for recording log messages on GUI or in log files.
    """

    msg: str = ''
    title: str = ''
    is_at_all: bool = True
    dd_index: int = 0 # 第几个钉钉，默认第一个

@dataclass
class MyZmqData(BaseData):
    """
    Log data is used for recording log messages on GUI or in log files.
    """
    topic: str = ''
    msg: str = ''

@dataclass
class MyOrderRequest(OrderRequest):
    time_in_force: TimeInForce = TimeInForce.GTD
    profit_price: Union[float, None] = None, # My.add 止盈价
    loss_price: Union[float, None] = None, # My.add 止损价
    
    def create_order_data(self, orderid: str, gateway_name: str) -> OrderData:
        """
        Create order data from request.
        """
        order: MyOrderData = MyOrderData(
            symbol=self.symbol,
            exchange=self.exchange,
            orderid=orderid,
            type=self.type,
            direction=self.direction,
            offset=self.offset,
            price=self.price,
            volume=self.volume,
            reference=self.reference,
            profit_price=self.profit_price,
            loss_price=self.loss_price,
            gateway_name=gateway_name
        )
        return order
    
@dataclass
class MySubscribeRequest(SubscribeRequest):
    types: list[SubscribeType] = field(default_factory=list)

    def __post_init__(self) -> None:
        """"""
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}" if self.exchange else ''

@dataclass
class MyAccountData(AccountData):
    """
    Account data contains information about balance, frozen and
    available.
    """

    currency: Currency = Currency.CNY


    
