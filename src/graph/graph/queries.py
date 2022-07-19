import strawberry as sb
from graph import models
from graph import repo
from typing import List, Optional


@sb.type
class RetrieveMarketData:
    open: float
    close: float
    high: float
    low: float
    volume: int


@sb.type
class Stock:
    ticker: str


@sb.type
class RetrieveStocks:
    stocks: Stock


@sb.input
class Filter:
    ticker_name: str

# QUERY CONSTRUCTOR


@ sb.type
class Query:

    @ sb.field
    def retrieve_stocks(self, filter: Optional[Filter] = None) -> Optional[List[Stock]]:
        stocks = repo.StockRepositoryImpl.get()
        if filter is not None:
            stocks = repo.StockRepositoryImpl.get_by_ticker_name(
                ticker_name=filter.ticker_name)
        return stocks
