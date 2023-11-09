"""
Sharpe Ratio Portfolio Optimizer
--------------------------------
`maximize_sharpe_ratio`: Adjusts quantities to maximize the portfolio's Sharpe Ratio.

Inputs:
- Portfolio object

Outputs:
- A new Portfolio class, where trades are updated with adjusted quantities that maximize the portfolio Sharpe Ratio while maintaining the portfolio value.
"""
import cvxpy as cp
from app.models.Trade import Trade
from app.models.Portfolio import Portfolio


def maximiseSharpeMethod(portfolio):

    # Extract relevant data from portfolio using provided methods
    trades = portfolio.getTrades()
    n = len(trades)
    returns = [trade.getReturn(
        portfolio.rfRate, portfolio.getMarketReturn()) for trade in trades]
    values = [trade.getTradeValue() for trade in trades]
    total_value = portfolio.portfolioValue

    # Define optimization variables
    weights = cp.Variable(n)

    # Calculate portfolio expected return and variance
    port_return = cp.sum(weights * returns)
    # Assuming all covariances are 0, the variance is simply the weighted sum of variances (stddev squared)
    # of individual assets.
    # here we assume returns as a proxy for risk
    port_variance = cp.sum(weights**2 * [r**2 for r in returns])

    # Define Sharpe Ratio
    sharpe_ratio = (port_return - portfolio.rfRate) / cp.sqrt(port_variance)

    # Constraints
    constraints = [cp.sum(weights) == 1, cp.sum(
        weights * values) == total_value]

    # Optimization problem
    problem = cp.Problem(cp.Maximize(sharpe_ratio), constraints)

    # Solve the problem
    problem.solve()

    # Extract optimized weights
    optimized_weights = weights.value

    # Adjust the trade quantities to reflect the optimized weights using provided methods
    adjusted_trades = []
    for i, trade in enumerate(trades):
        adjusted_qty = (optimized_weights[i] * total_value) / trade.buyPrice
        adjusted_trade = Trade(trade.tradeKey, trade.getTicker(
        ), trade.name, trade.buyPrice, adjusted_qty, trade.getBeta())
        adjusted_trades.append(adjusted_trade)

    # Return a new Portfolio instance with the adjusted trades
    return Portfolio(portfolio.user_id, adjusted_trades, portfolio.rfRate, portfolio.getMarketReturn())
