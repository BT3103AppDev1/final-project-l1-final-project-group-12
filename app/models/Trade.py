# The Trades class is meant to model a row from the Trades table in Firestore
import json
import urllib
import urllib.request
import sys
from urllib.parse import urlencode


class Trade:
    def __init__(self, tradeKey, ticker, buyPrice, buyQty):
        self.tradeKey = tradeKey
        self.ticker = ticker
        self.name = self.getStockName()
        self.buyPrice = buyPrice
        self.buyQty = buyQty
        self.beta = self.getStockBeta()  # market levered beta

    def __repr__(self):
        return f"Trade({self.ticker}, Name: {self.name}, Beta: {self.beta}, Quantity: {self.buyQty}, Buy Price: ${self.buyPrice})"

    # Public Getter Methods
    def getTradeValue(self):
        """Calculate the current value of the trade based on buy price and buy quantity."""
        return self.buyQty * self.buyPrice

    def getTicker(self):
        return self.ticker

    def getBeta(self):
        return self.beta

    def getReturn(self, rfRate, marketReturn):
        return rfRate + (self.beta * marketReturn - rfRate)

    def to_dict(self):
        return {
            'tradeKey': self.tradeKey,
            'ticker': self.ticker,
            'name': self.name,
            'buyPrice': self.buyPrice,
            'buyQty': self.buyQty,
            'beta': self.beta,
        }

    def to_json(self):
        """Converts the Portfolio class instance into a JSON string."""
        return json.dumps(self.to_dict(), indent=4)

    def getStockName(self):
        response = urllib.request.urlopen(
            f'https://query2.finance.yahoo.com/v1/finance/search?q={self.ticker}')
        content = response.read()
        data = json.loads(content.decode('utf8'))['quotes'][0]['shortname']
        return data

    def getStockBeta(self):
        ticker = self.ticker
        ticker = self.ticker.replace('\u200b', '')
        params = {
            'ticker': ticker,
            'index': '^GSPC',
            'interval': '1mo',
            'observations': '99999'
        }

        # Construct the full URL
        base_url = 'https://api.newtonanalytics.com/stock-beta/'
        full_url = base_url + '?' + urlencode(params)

        response = urllib.request.urlopen(full_url)
        content = response.read()
        data = json.loads(content.decode('utf8'))['data']
        return data


if __name__ == "__main__":
    trade_data = json.loads(sys.argv[1])
    trade = Trade(
        trade_data['tradeKey'],
        trade_data['ticker'],
        trade_data['buyPrice'],
        trade_data['buyQty']
    )
    print(trade.to_json())
