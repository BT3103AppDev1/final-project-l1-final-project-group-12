import math
import Trade
import json


class Portfolio:
    def __init__(self, user_id, trades, rfRate, marketReturn):
        # Assert that every item in the equities list is an instance of Trade class
        if not all(isinstance(trade, Trade) for trade in trades):
            raise ValueError(
                "All items in equities must be instances of the Trade class.")

        self.user_id = user_id
        self.trades = trades
        self.marketReturn = marketReturn
        self.rfRate = rfRate
        self.portfolioValue = sum([eachTrade.getTradeValue()
                                  for eachTrade in trades])

        # Portfolio Alpha & Beta calculations
        self._portfolioWeights = self._weights()
        __allReturns = self._allReturns()  # temp assignment
        self.portfolioReturn = sum(__allReturns)  # ACTUAL return of portfolio
        self.stddev = self._stddev()
        self.beta = self._beta()
        self.alpha = self.portfolioReturn - self._expectedReturn()
        self.sharpeRatio = self._sharpeRatio()

    # Private Methods
    def _weights(self):  # Captures the weightage of each stock in the portfolio
        localPortfolioWeights = {}
        for eachTrade in self.trades:
            localPortfolioWeights[eachTrade.getTicker()] = float(
                eachTrade.getTradeValue / self.portfolioValue)
        return localPortfolioWeights

    def _allReturns(self):  # Returns the returns of every trade in the portfolio
        return [(eachTrade.getReturn(self.rfRate, self.marketReturn) * self._portfolioWeights[eachTrade.getTicker()])
                for eachTrade in self.trades]

    def _beta(self):  # Returns the beta of eavery trade in the portfolio
        return sum([(eachTrade.getBeta() * self._portfolioWeights[eachTrade.getTicker()])
                    for eachTrade in self.trades])

    def _expectedReturn(self):  # Returns expected return of the portfolio
        return self.rfRate + self.beta * self.marketReturn

    def _stddev(self, __allReturns):
        return math.sqrt(sum((r - self.portfolioReturn) ** 2 for r in __allReturns) / len(__allReturns))

    def _sharpeRatio(self):
        excessReturn = self.portfolioReturn - self.rfRate  # Excess Return of Portfolio
        portfolioStdDev = self.stddev
        return float(excessReturn/portfolioStdDev)

    # Public Getter Methods

    def getAlpha(self):
        return self.alpha

    def getBeta(self):
        return self.beta

    def getSharpeRatio(self):
        return self.sharpeRatio

    def getReturn(self):
        return self.portfolioReturn

    def getMarketReturn(self):
        return self.marketReturn

    def getStdDev(self):
        return self.stddev

    def getVariance(self):
        return (self.stddev)**2

    def getRiskiestStock(self):
        maxTicker = ""
        maxBeta = 0

        for eachTrade in self.trades:
            if eachTrade.getBeta() > maxBeta:
                maxBeta = eachTrade.getBeta()
                maxTicker = eachTrade.getTicker()

        return (maxTicker, maxBeta)

    def getTrades(self):
        return self.trades

    def __repr__(self):
        return f"<Portfolio for user {self.user_id}>"

    # Return class as a JSON
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'portfolioValue': self.portfolioValue,
            'marketReturn': self.marketReturn,
            'rfRate': self.rfRate,
            'portfolioReturn': self.portfolioReturn,
            'stddev': self.stddev,
            'beta': self.beta,
            'alpha': self.alpha,
            'sharpeRatio': self.sharpeRatio,
            'trades': [trade.to_dict() for trade in self.trades]
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)
