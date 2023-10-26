import yfinance as yf
import json
import sys


"""
get_stock_statistics Function:
Fetches stock statistics for a specified ticker from Yahoo Finance.

Parameters:
@param ticker: str
    The stock ticker symbol.

Returns:
@return: str
    A JSON string containing stock statistics.
"""

def get_stock_statistics(ticker):
    stock = yf.Ticker(ticker)
    info = stock.earnings
    
    # Convert info dictionary to JSON
    info_json = json.dumps(info, indent=2)
    
    return info_json


"""
get_historical_data Function:
Fetches historical market data for a specified ticker from Yahoo Finance.

Parameters:
@param ticker: str
    The stock ticker symbol.
@param period: str, optional (Default: '1Y')
    The time period for which to fetch historical data.
    Possible values are '1D', '5D', '3M', '6M', '1Y', '5Y'.
@param interval: str, optional (Default: '1d')
    The frequency of data.
    Possible values are '1d' for daily, '1wk' for weekly, '1mo' for monthly.

Returns:
@return: str
    A JSON string containing historical market data.
"""

def get_historical_data(ticker, period='1Y', interval='1d'):
    stock = yf.Ticker(ticker)
    historical_data = stock.history(period=period, interval=interval)
    
    # Convert historical_data DataFrame to JSON
    historical_data_json = historical_data.to_json(indent=2, date_format='iso')
    
    return historical_data_json


"""
get_options_data Function:
Fetches options data for a specified ticker from Yahoo Finance.

Parameters:
@param ticker: str
    The stock ticker symbol.

Returns:
@return: dict
    A dictionary containing two keys: 'calls' and 'puts'.
    Each key maps to a JSON string containing options data for call options and put options, respectively.
"""

def get_options_data(ticker):
    stock = yf.Ticker(ticker)
    
    # Fetch options data
    options_data = stock.option_chain()
    
    # Convert options data DataFrames to JSON
    calls_json = options_data.calls.to_json(indent=2, date_format='iso')
    puts_json = options_data.puts.to_json(indent=2, date_format='iso')
    
    # Package calls and puts JSON strings into a dictionary
    options_data_json = {'calls': calls_json, 'puts': puts_json}
    
    return options_data_json


if __name__ == "__main__":
    function_name = sys.argv[1]
    args = sys.argv[2:]
    
    if function_name == 'get_stock_statistics' and len(args) == 1:
        print(get_stock_statistics(*args))
    elif function_name == 'get_historical_data' and len(args) >= 1:
        print(get_historical_data(*args))
    elif function_name == 'get_options_data' and len(args) == 1:
        print(json.dumps(get_options_data(*args)))
