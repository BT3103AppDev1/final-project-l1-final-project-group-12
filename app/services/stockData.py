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

    """
    get_market_cap Function:
    Fetches information on market cap for a ticker from https://finance.yahoo.com/quote/:ticker
    
    Parameters:
    @param ticker: str
        The stock ticker symbol.

    Returns:
    @return: str
        A str for market cap for specified ticker.
    """
def get_market_cap(ticker):
    url = f'https://finance.yahoo.com/quote/{ticker}'
    response = requests.get(url)

    if response.status_code == 200:
        doc = lxml.html.fromstring(response.content)

        # Modify the XPath expression to match the location of the market cap data on the page
        market_cap_element = doc.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[1]/td[2]')

        if market_cap_element:
            market_cap_value = market_cap_element[0].text  # Extract the text content of the element
            return market_cap_value
        else:
            return "Data not found."
    else:
        return f"Failed to retrieve data. Status code: {response.status_code}"

    """
    get_avg_volume Function:
    Fetches information on average volume for a ticker from https://finance.yahoo.com/quote/:ticker
    
    Parameters:
    @param ticker: str
        The stock ticker symbol.

    Returns:
    @return: str
        A str for average volume for specified ticker.
    """
def get_avg_volume(ticker):
    url = f'https://finance.yahoo.com/quote/{ticker}'
    response = requests.get(url)

    if response.status_code == 200:
        doc = lxml.html.fromstring(response.content)

        # Modify the XPath expression to match the location of the volume data on the page
        volume_element = doc.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[8]/td[2]')
        if volume_element:
            volume_value = volume_element[0].text  # Extract the text content of the element
            return volume_value
        else:
            return "Volume data not found on the page."
    else:
        return f"Failed to retrieve data. Status code: {response.status_code}"

    """
    get_percentage_change Function:
    Fetches information on percentage change for a ticker from https://finance.yahoo.com/quote/:ticker
    
    Parameters:
    @param ticker: str
        The stock ticker symbol.

    Returns:
    @return: str
        A str for percentage change for specified ticker.
    """
def get_percentage_change(ticker):
    url = f'https://finance.yahoo.com/quote/{ticker}'
    response = requests.get(url)

    if response.status_code == 200:
        doc = lxml.html.fromstring(response.content)

        # Modify the XPath expression to match the location of the percentage change data on the page
        percentage_change_element = doc.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[3]/span')

        if percentage_change_element:
            percentage_change_value = percentage_change_element[0].text  # Extract the text content of the element
            # Remove brackets if they exist
            percentage_change_value = percentage_change_value.strip('()')
            return percentage_change_value
        else:
            return "Percentage Change data not found on the page."
    else:
        return f"Failed to retrieve data. Status code: {response.status_code}"

    """
    get_ticker Function:
    Fetches ticker based on stock name from https://query2.finance.yahoo.com/v1/finance/search
    
    Parameters:
    @param ticker: stockName
        The stock name

    Returns:
    @return: str
        A str for ticker based on specified stockName
    """

def get_ticker(stockName):
    yfinance = "https://query2.finance.yahoo.com/v1/finance/search"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    params = {"q": stockName, "quotes_count": 1, "country": "United States"}

    res = requests.get(url=yfinance, params=params, headers={'User-Agent': user_agent})
    data = res.json()

    company_code = data['quotes'][0]['symbol']
    return company_code
   
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
    elif function_name == 'get_market_cap' and len(args) == 1:
        print(json.dumps(get_market_cap(*args)))
    elif function_name == 'get_avg_volume' and len(args) == 1:
        print(json.dumps(get_avg_volume(*args)))
    elif function_name == 'get_percentage_change' and len(args) == 1:
        print(json.dumps(get_percentage_change(*args)))
    elif function_name == 'get_ticker' and len(args) == 1:
        print(json.dumps(get_ticker(*args)))

        