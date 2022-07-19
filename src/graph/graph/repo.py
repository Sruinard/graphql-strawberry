from graph import models


class StockRepository:

    def __init__(self, stocks=[]):
        self.stocks = stocks
        self.stocks.append(

            models.Stock(
                ticker="AAPL"
            ))
        self.stocks.append(
            models.Stock(
                ticker="MSFT"
            )
        )

    def get(self):
        return self.stocks

    def get_by_ticker_name(self, ticker_name):
        return [stock for stock in self.stocks if stock.ticker == ticker_name]


StockRepositoryImpl = StockRepository()
