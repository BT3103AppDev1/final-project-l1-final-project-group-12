import math
from Trade import Trade
import json
import yfinance as yf
import cvxpy as cp
import sys


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
        self.stddev = self._stddev(__allReturns)
        self.beta = self._beta()
        self.alpha = self.portfolioReturn - self._expectedReturn()
        self.sharpeRatio = self._sharpeRatio()

    # Private Methods
    def _weights(self):  # Captures the weightage of each stock in the portfolio
        localPortfolioWeights = {}
        for eachTrade in self.trades:
            localPortfolioWeights[eachTrade.getTicker()] = float(
                eachTrade.getTradeValue() / self.portfolioValue)
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

        if portfolioStdDev == 0:
            return 0
        else:
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
        return Portfolio.maximiseAlphaMethod(self)

    def optimiseForMinBeta(self):
        return Portfolio.minimiseBetaMethod(self)

    def optimiseforBestBalance(self):
        return Portfolio.maximiseSharpeMethod(self)
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
            'userId': self.user_id,
            'trades': [trade.to_dict() for trade in self.trades],
            'marketReturn': self.marketReturn,
            'rfRate': self.rfRate,
            'portfolioValue': self.portfolioValue,
            'portfolioReturn': self.portfolioReturn,
            'stddev': self.stddev,
            'beta': self.beta,
            'alpha': self.alpha,
            'sharpeRatio': self.sharpeRatio,
            'variance': self.stddev * self.stddev
        }

    def to_json(self):
        """Converts the Portfolio class instance into a JSON string."""
        return json.dumps(self.to_dict(), indent=4)

    # Optimisation Methods to be hidden
    @staticmethod
    def maximiseAlphaMethod(portfolio):
        # Extract relevant data from portfolio using provided methods
        trades = portfolio.getTrades()
        n = len(trades)
        returns = [trade.getReturn(
            portfolio.rfRate, portfolio.getMarketReturn()) for trade in trades]
        betas = [trade.getBeta() for trade in trades]
        values = [trade.getTradeValue() for trade in trades]
        total_value = portfolio.portfolioValue

        # Define optimization variables
        weights = cp.Variable(n, nonneg=True)

        # Calculate portfolio expected return and alpha
        port_return = cp.sum(weights * returns)
        expected_port_return = portfolio.rfRate + \
            cp.sum(weights * betas) * portfolio.getMarketReturn()
        port_alpha = port_return - expected_port_return

        # Adjusted constraints
        constraints = [cp.sum(weights * values) <= total_value]

        # Optimization problem
        problem = cp.Problem(cp.Maximize(port_alpha), constraints)

        # Solve the problem
        problem.solve()

        # Extract optimized weights
        optimized_weights = weights.value

        if optimized_weights is None:
            return portfolio

        # Adjust the trade quantities to reflect the optimized weights using provided methods
        adjusted_trades = []
        for i, trade in enumerate(trades):
            adjusted_qty = (
                optimized_weights[i] * total_value) / trade.buyPrice
            adjusted_trade = Trade(
                trade.tradeKey, trade.getTicker(), trade.buyPrice, adjusted_qty)
            adjusted_trades.append(adjusted_trade)

        # Return a new Portfolio instance with the adjusted trades
        newPortfolio = Portfolio(portfolio.user_id, adjusted_trades)

        if (newPortfolio.getAlpha() > portfolio.getAlpha()):
            return newPortfolio
        elif (newPortfolio.getAlpha() == portfolio.getAlpha() and newPortfolio.getBeta() < portfolio.getBeta()):
            return newPortfolio
        return portfolio

    @staticmethod
    def maximiseSharpeMethod(portfolio):

        # Extract relevant data from portfolio using provided methods
        trades = portfolio.getTrades()
        n = len(trades)
        returns = [trade.getReturn(
            portfolio.rfRate, portfolio.getMarketReturn()) for trade in trades]
        values = [trade.getTradeValue() for trade in trades]
        total_value = portfolio.portfolioValue

        # Define optimization variables
        weights = cp.Variable(n, nonneg=True)
        t = cp.Variable(nonneg=True)

        # Calculate portfolio expected return and variance
        port_return = cp.sum(weights * returns)
        # Assuming all covariances are 0, the variance is simply the weighted sum of variances (stddev squared)
        # of individual assets.
        # here we assume returns as a proxy for risk
        port_variance = cp.sum(weights**2 * [r**2 for r in returns])

        gamma = 1000     # Set gamma to some large value to penalize risk
        objective = port_return - gamma * t

        # Constraints
        constraints = [cp.sum(weights) == 1, cp.sum(
            weights * values) == total_value, port_variance <= t]

        problem = cp.Problem(cp.Maximize(objective), constraints)

        # Solve the problem
        problem.solve()

        # Extract optimized weights
        optimized_weights = weights.value

        if optimized_weights is None:
            return portfolio
        # Adjust the trade quantities to reflect the optimized weights using provided methods
        adjusted_trades = []
        for i, trade in enumerate(trades):
            adjusted_qty = (
                optimized_weights[i] * total_value) / trade.buyPrice
            adjusted_trade = Trade(
                trade.tradeKey, trade.getTicker(),  trade.buyPrice, adjusted_qty)
            adjusted_trades.append(adjusted_trade)

        # Return a new Portfolio instance with the adjusted trades
        newPortfolio = Portfolio(portfolio.user_id, adjusted_trades)

        if (newPortfolio.getSharpeRatio() > portfolio.getSharpeRatio()):
            return newPortfolio
        return portfolio

    @staticmethod
    def minimiseBetaMethod(portfolio):
        # Extract relevant data from portfolio using provided methods
        trades = portfolio.getTrades()
        n = len(trades)
        betas = [trade.getBeta() for trade in trades]
        values = [trade.getTradeValue() for trade in trades]
        total_value = portfolio.portfolioValue

        # Define optimization variables
        weights = cp.Variable(n, nonneg=True)

        # Calculate portfolio beta
        port_beta = cp.sum(weights * betas)

        # Adjusted constraints
        constraints = [cp.sum(weights * values) <= total_value]

        # Optimization problem
        problem = cp.Problem(cp.Minimize(port_beta), constraints)

        # Solve the problem
        problem.solve()

        # Extract optimized weights
        optimized_weights = weights.value

        if optimized_weights is None:
            return portfolio

        # Adjust the trade quantities to reflect the optimized weights using provided methods
        adjusted_trades = []
        for i, trade in enumerate(trades):
            adjusted_qty = (
                optimized_weights[i] * total_value) / trade.buyPrice
            adjusted_trade = Trade(
                trade.tradeKey, trade.getTicker(), trade.buyPrice, adjusted_qty)
            adjusted_trades.append(adjusted_trade)

        newPortfolio = Portfolio(portfolio.user_id, adjusted_trades)
        # Return a new Portfolio instance with the adjusted trades
        if (newPortfolio.getBeta() < portfolio.getBeta()):
            return newPortfolio
        elif (newPortfolio.getBeta() == portfolio.getBeta() and newPortfolio.getAlpha() > portfolio.getAlpha()):
            return newPortfolio
        return portfolio


if __name__ == "__main__":
    userOldPortfolioData = json.loads(sys.argv[1])
    objectiveOfUpdate = sys.argv[2]

    if (objectiveOfUpdate == "alpha"):
        user_id = userOldPortfolioData["userId"]
        trades = [Trade(trade['id'], trade['ticker'], trade['buyPrice'],
                        trade['buyQty']) for trade in userOldPortfolioData["allTradesData"]]

        portfolio = Portfolio(user_id, trades).optimiseForMaxAlpha()
        print(portfolio.to_json())
    elif (objectiveOfUpdate == "beta"):
        user_id = userOldPortfolioData["userId"]
        trades = [Trade(trade['id'], trade['ticker'], trade['buyPrice'],
                        trade['buyQty']) for trade in userOldPortfolioData["allTradesData"]]

        portfolio = Portfolio(user_id, trades).optimiseForMinBeta()
        print(portfolio.to_json())
    elif (objectiveOfUpdate == "balance"):
        user_id = userOldPortfolioData["userId"]
        trades = [Trade(trade['id'], trade['ticker'], trade['buyPrice'],
                        trade['buyQty']) for trade in userOldPortfolioData["allTradesData"]]

        portfolio = Portfolio(user_id, trades).optimiseforBestBalance()
        print(portfolio.to_json())
    else:
        user_id = userOldPortfolioData["userId"]
        trades = [Trade(trade['id'], trade['ticker'], trade['buyPrice'],
                        trade['buyQty']) for trade in userOldPortfolioData["allTradesData"]]

        portfolio = Portfolio(user_id, trades)
        print(portfolio.to_json())
