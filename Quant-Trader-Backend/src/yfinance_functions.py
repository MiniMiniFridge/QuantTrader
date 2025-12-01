import tqdm
import research_v2 as r2

SYMBOL_STOCKS = ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'AMZN', 'NVDA']  # your list here

def analyze_stock_universe(stock_data_dict, forecast_horizon=1, max_lags=4):
    """
    Apply feature engineering to multiple stocks
    """
    featured_stocks = {}
    for symbol, data in stock_data_dict.items():
        try:
            featured_data = r2.add_log_return_features(data, "close", forecast_horizon, max_lags)
            featured_stocks[symbol] = featured_data
            print(f"✓ Processed {symbol}")
        except Exception as e:
            print(f"✗ Failed to process {symbol}: {e}")
    
    return featured_stocks