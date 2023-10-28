# Developer Class Guide

This guide provides instructions on how to utilise the classes

## Trade Class

```
Trade(tradeKey, portfolioId, ticker, name, buyPrice, buyQty, beta)
```

### Attributes:

- **tradeKey**: A unique identifier for the trade.
- **ticker**: Stock ticker symbol.
- **name**: Name of the stock.
- **buyPrice**: Price at which the stock was bought.
- **buyQty**: Quantity of stocks bought.
- **beta**: Market levered beta.

### Public Methods:

- **getTradeValue()**: Calculate the current value of the trade based on buy price and buy quantity.
- **getTicker()**: Retrieve the ticker symbol of the trade.
- **getBeta()**: Retrieve the beta value of the trade.
- **getReturn(rfRate, marketReturn)**: Calculate the return of the trade.

## Portfolio Class

```
Portfolio(user_id, trades, rfRate, marketReturn)
```

### Attributes:

- **user_id** (str): A unique identifier for the user.
- **trades** (list): A list of Trade objects representing individual trades in the portfolio.
- **marketReturn** (float): The expected market return used in portfolio metric calculations.
- **rfRate** (float): The risk-free rate used in portfolio metric calculations.
- **portfolioValue** (float): The total value of the portfolio based on the sum of trade values.
- **portfolioReturn** (float): The total portfolio return
- **stddev** (float): The standard deviation of the portfolio
- **beta**: The systematic risk of the portfolio
- **alpha**: The actual excess return of the portfolio benchmarked against the market
- **sharpeRatio** (float): The risk-adjusted return of the portfolio
- **\_portfolioWeights** (list): Private attribute holding all the weights of each trade in the portfolio

### Public Methods:

- **getAlpha()**: Returns alpha.
- **getBeta()**: Returns beta.
- **getSharpeRatio()**: Returns the Sharpe ratio.
- **getReturn()**: Returns the actual return of the portfolio.
- **getMarketReturn()**: Returns the expected market return.
- **getStdDev()**: Returns the standard deviation of the portfolio.
- **getVariance()**: Returns the variance of the portfolio.
- **getRiskiestStock()**: Returns a tuple of (maxBetaStock, maxBetaValue)

### Private Methods:

- **\_weights()**: Captures the weightage of each stock in the portfolio.
- **\_allReturns()**: Returns the returns of every trade in the portfolio.
- **\_beta()**: Returns the beta of every trade in the portfolio.
- **\_expectedReturn()**: Returns the expected return of the portfolio.
- **\_stddev(self, \_\_allReturns)**: Returns the std deviation of the portfolio
- **\_sharpeRatio()**: Calculates the Sharpe ratio of the portfolio given the returns of all trades.
