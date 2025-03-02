import yfinance as yf
import pandas as pd

class DataFetcher:
    @staticmethod
    def fetch_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
        """Fetch historical stock data from Yahoo Finance."""
        return yf.download(ticker, start=start_date, end=end_date)

class DataPreprocessor:
    @staticmethod
    def handle_missing_values(data: pd.DataFrame) -> pd.DataFrame:
        """Handle missing values in the dataset."""
        data = data.fillna(method='ffill')  # Forward fill
        data = data.fillna(method='bfill')  # Backward fill
        return data

    @staticmethod
    def normalize_data(data: pd.DataFrame) -> pd.DataFrame:
        """Normalize the dataset using Min-Max scaling."""
        return (data - data.min()) / (data.max() - data.min())

    @staticmethod
    def convert_index_to_datetime(data: pd.DataFrame) -> pd.DataFrame:
        """Convert index to datetime if it's not already."""
        if not pd.api.types.is_datetime64_any_dtype(data.index):
            data.index = pd.to_datetime(data.index)
        return data

    @staticmethod
    def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
        """Preprocess the time series data."""
        data = DataPreprocessor.handle_missing_values(data)
        data = DataPreprocessor.normalize_data(data)
        data = DataPreprocessor.convert_index_to_datetime(data)
        return data

class DataSplitter:
    @staticmethod
    def split_data(data: pd.DataFrame, train_size: float) -> tuple:
        """Split the dataset into training and testing sets."""
        train_size = int(len(data) * train_size)
        train, test = data[:train_size], data[train_size:]
        return train, test

class FeatureEngineer:
    @staticmethod
    def create_lagged_features(data: pd.DataFrame, lags: int = 3) -> pd.DataFrame:
        """Create lagged features."""
        for lag in range(1, lags + 1):
            data[f'lag_{lag}'] = data['Close'].shift(lag)
        return data

    @staticmethod
    def create_rolling_statistics(data: pd.DataFrame, window: int = 3) -> pd.DataFrame:
        """Create rolling statistics features."""
        data['rolling_mean'] = data['Close'].rolling(window=window).mean()
        data['rolling_std'] = data['Close'].rolling(window=window).std()
        return data

    @staticmethod
    def create_features(data: pd.DataFrame) -> pd.DataFrame:
        """Create additional features from the time series data."""
        data = FeatureEngineer.create_lagged_features(data)
        data = FeatureEngineer.create_rolling_statistics(data)
        return data.dropna()  # Drop rows with NaN values after feature creation

# Example usage:
if __name__ == "__main__":
    ticker = "AAPL"
    start_date = "2020-01-01"
    end_date = "2021-01-01"
    
    data = DataFetcher.fetch_data(ticker, start_date, end_date)
    data = DataPreprocessor.preprocess_data(data)
    train, test = DataSplitter.split_data(data, train_size=0.8)
    train = FeatureEngineer.create_features(train)
    test = FeatureEngineer.create_features(test)
    
    print(train.head())
    print(test.head())