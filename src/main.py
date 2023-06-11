from config.utils import save_dataframe_as_csv
from scraper import ticker_data_google

if __name__ == '__main__':
    df = ticker_data_google()
    save_dataframe_as_csv(df=df, filename="data.csv")
