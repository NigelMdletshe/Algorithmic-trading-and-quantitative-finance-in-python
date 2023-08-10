import yfinance as yf

# Define the ticker symbol for the stock you want to download
ticker_symbol = "AAPL"  # Apple Inc.

# Define the date range for the historical data
start_date = "2022-01-01"
end_date = "2022-12-31"

# Download the historical data
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Display the downloaded data
print(stock_data)
