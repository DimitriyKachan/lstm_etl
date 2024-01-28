import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


def extract(ticker: str, start_date: str):
    current_date = datetime.now().strftime('%Y-%m-%d')
    yf_ticker = yf.Ticker(ticker)
    history = yf_ticker.history(start=start_date, end=current_date)
    history['Date'] = history.index
    return history


def load(filename: str, ticker: str):
    saved_df = pd.read_csv(filename)
    last_date = datetime.strptime(saved_df['Date'].values[-1][:10], "%Y-%m-%d")
    needed_date = (last_date + timedelta(days=1)).strftime('%Y-%m-%d')
    update_df = extract(ticker, needed_date)
    updated_df = pd.concat([saved_df, update_df], axis=0)
    updated_df = updated_df.reset_index()
    updated_df = updated_df.drop('index', axis=1)
    updated_df.to_csv(filename, index=False)
    return updated_df


load('apple_history.csv', 'AAPL')
