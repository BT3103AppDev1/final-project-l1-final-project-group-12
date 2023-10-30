"""
Min Beta Portfolio Optimizer
----------------------------
Functions:
Adjusts quantities to minimize the portfolio's beta.

Inputs:
- Portfolio object
Outputs:
- A new Portfolio class, where trades are updated with adjusted quantities that minimize the portfolio beta while maintaining the portfolio value.

"""
import cvxpy as cp
from app.models.Trade import Trade
from app.models.Portfolio import Portfolio


def minimiseBetaMethod(portfolio):
    # Extract relevant data from portfolio using provided methods
    trades = portfolio.getTrades()
    n = len(trades)
    betas = [trade.getBeta() for trade in trades]
    values = [trade.getTradeValue() for trade in trades]
    total_value = portfolio.portfolioValue

    # Define optimization variables
    weights = cp.Variable(n)

    # Calculate portfolio beta
    port_beta = cp.sum(weights * betas)

    # Constraints
    constraints = [cp.sum(weights) == 1, cp.sum(
        weights * values) == total_value]

    # Optimization problem
    problem = cp.Problem(cp.Minimize(port_beta), constraints)

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
