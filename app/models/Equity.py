class Equity:
    def __init__(self, ticker, beta, qty, avg_price, return_rate):
        self.ticker = ticker
        self.beta = beta
        self.qty = qty
        self.avg_price = avg_price
        self.return_rate = return_rate

    def __str__(self):
        return f"Equity({self.ticker}, Beta: {self.beta}, Quantity: {self.qty}, Average Price: ${self.avg_price}, Return: {self.return_rate*100}%)"

    def current_value(self):
        """Calculate the current value of the equity based on average price and quantity."""
        return self.qty * self.avg_price

    def expected_value(self):
        """Calculate the expected value based on return rate."""
        return self.current_value() * (1 + self.return_rate)
