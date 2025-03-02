
import yfinance as yf
import pandas as pd

def fetch_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """Fetch historical stock data from Yahoo Finance."""
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    """Preprocess the time series data."""
    # Handle missing values
    data = data.fillna(method='ffill')  # Forward fill
    data = data.fillna(method='bfill')  # Backward fill
    
    # Normalize data (example: Min-Max scaling)
    data = (data - data.min()) / (data.max() - data.min())
    
    # Convert index to datetime if it's not already
    if not pd.api.types.is_datetime64_any_dtype(data.index):
        data.index = pd.to_datetime(data.index)
    
    return data

def split_data(data: pd.DataFrame, train_size: float) -> tuple:
    """Split the dataset into training and testing sets."""
    train_size = int(len(data) * train_size)
    train, test = data[:train_size], data[train_size:]
    return train, test

def create_features(data: pd.DataFrame) -> pd.DataFrame:
    """Create additional features from the time series data."""
    # Example: Create lagged features
    for lag in range(1, 4):  # Create 3 lagged features
        data[f'lag_{lag}'] = data['Close'].shift(lag)
    
    # Example: Create rolling statistics
    data['rolling_mean'] = data['Close'].rolling(window=3).mean()
    data['rolling_std'] = data['Close'].rolling(window=3).std()
    
    return data.dropna()  # Drop rows with NaN values after feature creation