import math
import Trade
import json
import yfinance as yf
from app.services.maxAlpha import maximiseAlphaMethod
from app.services.maxBalance import maximiseSharpeMethod
from app.services.minBeta import minimiseBetaMethod


class Portfolio:
    def __init__(self, user_id, trades):
        # Assert that every item in the equities list is an instance of Trade class
        if not all(isinstance(trade, Trade) for trade in trades):
            raise ValueError(
                "All items in equities must be instances of the Trade class.")

        self.user_id = user_id
        self.trades = trades
        self.rfRate = self.__riskFreeRate()
        self.marketReturn = self.__marketReturn()
        self.portfolioValue = sum([eachTrade.getTradeValue()
                                  for eachTrade in trades])  # Actual value, used to capture weight

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
        return self.rfRate + self.beta * (self.marketReturn - self.rfRate)

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

    # Public Methods to compute optimisation
    def optimiseForMaxAlpha(self):
        return maximiseAlphaMethod(self)

    def optimiseForMinBeta(self):
        return minimiseBetaMethod(self)

    def optimiseforBestBalance(self):
        return minimiseBetaMethod(self)
    # Private Helper Methods

    def __riskFreeRate(self):
        tnx = yf.Ticker("^TNX")
        riskFreeRate = tnx.history(period="1y")['Close'].iloc[-1]
        return riskFreeRate

    def __marketReturn(self):
        # Fetch the data for S&P 500 for the last year
        sp500 = yf.Ticker("^GSPC")
        data = sp500.history(period="1y")

        # Calculate the annual return
        start_price = data['Close'].iloc[0]
        end_price = data['Close'].iloc[-1]
        marketReturn = (end_price - start_price) / start_price

        return marketReturn

    def __repr__(self):
        return f"<Portfolio for user {self.user_id}>"

    def to_dict(self):
        """Converts the Portfolio class instance into a dictionary."""
        return {
            'user_id': self.user_id,
            'trades': [trade.to_dict() for trade in self.trades],
            'marketReturn': self.marketReturn,
            'rfRate': self.rfRate,
            'portfolioValue': self.portfolioValue,
            'portfolioReturn': self.portfolioReturn,
            'stddev': self.stddev,
            'beta': self.beta,
            'alpha': self.alpha,
            'sharpeRatio': self.sharpeRatio
        }

    def to_json(self):
        """Converts the Portfolio class instance into a JSON string."""
        return json.dumps(self.to_dict(), indent=4)


if __name__ == "__main__":
    userOldPortfolioData = json.loads(sys.argv[1])
    user_id = userOldPortfolioData['userId']
    trades = [Trade(trade['tradeKey'], trade['ticker'], trade['buyPrice'],
                    trade['buyQty']) for trade in userOldPortfolioData['allTradesData']]

    portfolio = Portfolio(user_id, trades)
    print(portfolio.to_json())
