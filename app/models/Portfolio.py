import math
"""
    Initialisation:
    - user_id (str): A unique identifier for the user.
    - trades (list): A list of Trade objects representing individual trades in the portfolio.
    - rfRate (float): The risk-free rate used in portfolio metric calculations.
    - marketReturn (float): The expected market return used in portfolio metric calculations.

    Public Attributes:
    - user_id (str): A unique identifier for the user.
    - trades (list): A list of Trade objects representing individual trades in the portfolio.
    - marketReturn (float): The expected market return used in portfolio metric calculations.
    - rfRate (float): The risk-free rate used in portfolio metric calculations.
    - portfolioValue (float): The total value of the portfolio based on the sum of trade values.
    - beta: The systematic risk of the portfolio
    - alpha: The actual excess return of the portfolio benchmarked against the market
    - sharpeRatio (float): The risk-adjusted return of the portfolio
    
    Public Methods:
    - getMetrics(): Calculate and return a dictionary of portfolio metrics, including beta, alpha, and Sharpe ratio.
"""


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
        self.beta = self._beta()
        __allReturns = self._allReturns()  # temp assignment
        self.portfolioReturn = sum(__allReturns)  # ACTUAL return of portfolio
        self.alpha = self.portfolioReturn - self._expectedReturn()
        self.sharpeRatio = self._sharpeRatio(__allReturns)

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

    def _sharpeRatio(self, __allReturns):
        excessReturn = self.portfolioReturn - self.rfRate  # Excess Return of Portfolio
        portfolioStdDev = math.sqrt(
            sum((r - self.portfolioReturn) ** 2 for r in __allReturns) / len(__allReturns))
        return float(excessReturn/portfolioStdDev)

    # Public Getter Methods

    @property
    def getMetrics(self):
        '''
        Parameters: NA
        Result    : Returns a dictionary of beta, alpha, and sharpe ratio
        '''
        return {
            'beta': self.beta,
            'alpha': self.alpha,
            'sharpe_ratio': self.sharpeRatio
        }

    def __repr__(self):
        return f"<Portfolio for user {self.user_id}>"
