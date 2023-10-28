# The Trades class is meant to model a row from the Trades table in Firestore

class Trade:
    def __init__(self, tradeKey, ticker, name, buyPrice, buyQty, beta):
        self.tradeKey = tradeKey
        self.ticker = ticker
        self.name = name
        self.buyPrice = buyPrice
        self.buyQty = buyQty
        self.beta = beta  # market levered beta

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
        return rfRate + (self.beta * marketReturn)

    # Return class as a JSON

    def to_dict(self):
        return {
            'tradeKey': self.tradeKey,
            'ticker': self.ticker,
            'name': self.name,
            'buyPrice': self.buyPrice,
            'buyQty': self.buyQty,
            'beta': self.beta
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)
