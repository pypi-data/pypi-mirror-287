import pandas as pd
import requests
import yfinance as yf
from datetime import datetime, timedelta

def get_stock_data(ticker, start_date, end_date):
    # Calculate the start and end dates
    end_date = end_date
    start_date = start_date

    # Fetch stock data from yfinance
    data = yf.download(ticker, start=start_date, end=end_date)

    if data.empty:
        print("No data available for the given period.")
        return None, None

    # Find the min and max dates in the data
    min_date = data.index.min()
    max_date = data.index.max()

    return min_date, max_date

def fetch_data_for_date(ticker, date):
    """Fetch stock data for a specific date."""
    data = yf.download(ticker, start=date.strftime('%Y-%m-%d'), end=(date + timedelta(days=1)).strftime('%Y-%m-%d'))
    if data.empty:
        print(f"\nTicker: {ticker}")
        print(f"No data available for {date.strftime('%Y-%m-%d')}.")
    return data

def check_stock_changes(tickers, min_date, max_date, mentioned_percent):
    results = []
    print(f"\nFetching the closing price as of {min_date.strftime('%Y-%m-%d')} and {max_date.strftime('%Y-%m-%d')}.")

    for ticker in tickers:
        try:
            # Fetch data for start and end dates
            start_data = fetch_data_for_date(ticker, min_date)
            end_data = fetch_data_for_date(ticker, max_date)

            print(f"\nTicker: {ticker}")
            print(start_data)
            print(end_data)

            # Check if we have data for both dates
            if start_data.empty or end_data.empty:
                print(f"Not enough data for {ticker}.")
                continue

            # Get the closing price at the start and end dates
            start_price = start_data['Close'].iloc[0]
            end_price = end_data['Close'].iloc[0]

            # Calculate percentage change
            percentage_change = ((end_price - start_price) / start_price) * 100

            # Check if the percentage change meets the requirement
            if (mentioned_percent < 0 and percentage_change <= mentioned_percent) or (mentioned_percent >= 0 and percentage_change >= mentioned_percent):
                results.append((ticker, percentage_change))

        except Exception as e:
            print(f"Error processing {ticker}: {e}")

    return results
