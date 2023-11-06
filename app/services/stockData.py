import yfinance as yf
import json
import sys
import lxml.html
import requests

"""
get_current_price Function:
Fetches stock statistics for a specified ticker from Yahoo Finance.

Parameters:
@param ticker: str
    The stock ticker symbol.

Returns:
@return: float
    A float of the latest stock value.
"""
def get_current_price(ticker):
    ticker = yf.Ticker(ticker)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'].iloc[0]

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

    """
    get_top_gainers Function:
    Fetches information on the top 5 stock gainers from https://finance.yahoo.com/gainers

    Parameters:
    @param None

    Returns:
    @return: str
        A JSON string containing 'stock_name' for each gainer.
    """
def get_top_gainers():
    url = 'https://finance.yahoo.com/gainers'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
    }
    ytext = requests.get(url, headers=headers).text
    yroot = lxml.html.fromstring(ytext)

    top_gainers = []

    for i, x in enumerate(yroot.xpath('//*[@id="fin-scr-res-table"]//td[@aria-label="Name"]')):
        stock_name = x.text_content().strip()
        top_gainers.append({"stock_name": stock_name})

        # Limit to the top 5 gainers
        if i == 4:
            break

    return top_gainers

    """
    get_top_losers Function:
    Fetches information on the top 5 stock losers from https://finance.yahoo.com/gainers

    Parameters:
    @param None

    Returns:
    @return: str
        A JSON string containing 'stock_name' for each loser.
    """

def get_top_losers():
    url = 'https://finance.yahoo.com/losers'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
    }
    ytext = requests.get(url, headers=headers).text
    yroot = lxml.html.fromstring(ytext)

    top_losers = []

    for i, x in enumerate(yroot.xpath('//*[@id="fin-scr-res-table"]//td[@aria-label="Name"]')):
        stock_name = x.text_content().strip()
        top_losers.append({"stock_name": stock_name})

        # Limit to the top 5 losers
        if i == 4:
            break

    return top_losers

    """
    get_most_actives Function:
    Fetches information on the most active stocks from https://finance.yahoo.com/most-active

    Parameters:
    @param None

    Returns:
    @return: str
        A JSON string containing market data for the most active stocks
    """

def get_most_actives():
    url = 'https://finance.yahoo.com/most-active'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
    }
    ytext = requests.get(url, headers=headers).text
    yroot = lxml.html.fromstring(ytext)

    most_actives = []

    # XPath expressions for the column headers
    headers = yroot.xpath('//*[@id="scr-res-table"]/div[1]/table/thead/tr/th')

    # Extract column names
    column_names = [header.text_content().strip() for header in headers]

    # Updated XPath expressions for the data rows
    rows = yroot.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr')

    for row in rows:
        data = row.xpath('./td')
        stock_info = {}

        for i, column in enumerate(data):
            column_name = column_names[i]
            column_value = column.text_content().strip()
            stock_info[column_name] = column_value

        most_actives.append(stock_info)

    return most_actives

if __name__ == "__main__":
    function_name = sys.argv[1]
    args = sys.argv[2:]
    
    if function_name == 'get_stock_statistics' and len(args) == 1:
        print(get_stock_statistics(*args))
    elif function_name == 'get_historical_data' and len(args) >= 1:
        print(get_historical_data(*args))
    elif function_name == 'get_options_data' and len(args) == 1:
        print(json.dumps(get_options_data(*args)))
    elif function_name == 'get_current_price' and len(args) == 1:
        print(json.dumps(get_current_price(*args)))
    elif function_name == 'get_top_gainers' and len(args) == 1:
        print(json.dumps(get_top_gainers()))
    elif function_name == 'get_top_losers' and len(args) == 1:
        print(json.dumps(get_top_losers()))
    elif function_name == 'get_most_actives' and len(args) == 1:
        print(json.dumps(get_most_actives()))