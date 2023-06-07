import pandas as pd
import requests
from bs4 import BeautifulSoup

ticker_symbol = "TSLA"
market_index = "NASDAQ"


def get_reponse_url(ticker_symbol, market_index):
    """
    get_reponse_url _summary_

    Args:
        ticker_symbol (_type_): _description_
        market_index (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        url = f"https://www.google.com/finance/quote/{ticker_symbol}:{market_index}?hl=en"
        # Set a timeout value of 5 seconds
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Check for any HTTP errors
        # Process the response as needed
        return response
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)


def ticker_data_google():
    """
    ticker_data_google _summary_
    """
    response = get_reponse_url(ticker_symbol, market_index)
    soup = BeautifulSoup(response.text, "html.parser")

    price = soup.find('div', class_='YMlKec fxKbKc').text
    company_name = soup.find('div', class_='zzDege').text

    time_market_status = soup.find('div', class_='ygUjEc').nextSibling.text
    market_status = time_market_status.split(':')[0]
    # Date and time
    month = time_market_status.split(' ')[1]
    day = time_market_status.split(' ')[2][:-1]

    time_prepared = time_market_status.split(' ')[3]
    meridiem = time_prepared[-2:]
    time = time_prepared.split()[0]

    df = pd.DataFrame(columns=['price', 'company_name',
                      'market_status', 'month', 'day', 'meridiem', 'time'])
    df.loc[0] = [price, company_name,
                 market_status, month, day, meridiem, time]

    return df
