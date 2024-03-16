import ccxt


def fetch_data(symbol='BTC/USDT'):
    exchange = ccxt.binance()  # Initialize the Binance exchange
    ticker = exchange.fetch_ticker(symbol)  # Fetch the ticker for BTC/USDT
    return ticker['last']  # Return the last price


if __name__ == "__main__":
    print(fetch_data())
