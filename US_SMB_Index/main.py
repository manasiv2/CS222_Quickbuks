import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker):
    """
    Fetch historical stock data for the given ticker.
    :param ticker: Stock ticker symbol as a string.
    :return: Pandas DataFrame with historical stock data.
    """
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")  # Adjust period as needed
    return hist

def calculate_volatility(hist):
    """
    Calculate the volatility of a stock based on historical data.
    :param hist: Pandas DataFrame with historical stock data.
    :return: Float representing the stock's volatility.
    """
    return hist['Close'].pct_change().std()

def categorize_risk(hist):
    """
    Categorize stock into risk categories based on volatility.
    :param hist: Pandas DataFrame with historical stock data.
    :return: String representing the risk category.
    """
    volatility = calculate_volatility(hist)
    if volatility < 0.01:
        return 'Low'
    elif volatility < 0.02:
        return 'Medium'
    else:
        return 'High'
