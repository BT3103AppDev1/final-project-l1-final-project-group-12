from services.portfolio_calculation import calculate_portfolio_metrics, expected_return_CAPM


class Portfolio:
    def __init__(self, user_id, equities, benchmark_return, risk_free_rate):
        self.user_id = user_id
        self.equities = equities
        self.benchmark_return = benchmark_return
        self.risk_free_rate = risk_free_rate
    
    @property
    def metrics(self):
        """Calculate and return the portfolio's metrics."""
        beta, alpha, sharpe = calculate_portfolio_metrics(
            self.equities, self.benchmark_return, self.risk_free_rate)
        return {
            'beta': beta,
            'alpha': alpha,
            'sharpe_ratio': sharpe
        }
    
    def expected_return_for_equity(self, equity):
        """Return the expected return for a given equity using CAPM."""
        return expected_return_CAPM(
            self.risk_free_rate, equity['beta'], self.benchmark_return)
    
    def __repr__(self):
        return f"<Portfolio for user {self.user_id}>"

