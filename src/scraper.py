import pandas as pd
import requests
from bs4 import BeautifulSoup

TICKER_SYMBOL = "TSLA"
MARKET_INDEX = "NASDAQ"


def get_reponse_url(ticker_symbol, market_index):
    """
    get_reponse_url _summary_

    Args:
        TICKER_SYMBOL (_type_): _description_
        MARKET_INDEX (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        url = "https://www.google.com/finance/quote/" + \
            f"{ticker_symbol}:{market_index}?hl=en"

        # Set a timeout value of 5 seconds
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Check for any HTTP errors
        # Process the response as needed
        return response
    except requests.exceptions.RequestException as request_exception:
        print("Request failed:", request_exception)


def ticker_data_google():
    """
    ticker_data_google _summary_
    """
    response = get_reponse_url(
        ticker_symbol=TICKER_SYMBOL, market_index=MARKET_INDEX)
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

    df_google_finance = pd.DataFrame(columns=['price', 'company_name',
                                             'market_status', 'month', 'day', 'meridiem', 'time'])  # noqa
    df_google_finance.loc[0] = [price, company_name,
                                market_status, month, day, meridiem, time]

    return df_google_finance
