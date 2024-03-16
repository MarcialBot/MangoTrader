import ccxt
import time


class MarketDataFetcher:
    def __init__(self, exchange_id='coinbase'):
        self.exchange = getattr(ccxt, exchange_id)()
        self.last_request_time = 0
        self.rate_limit = self.exchange.rateLimit / 1000

    def safe_fetch(self, fetch_function, *args, **kwargs):

        time_since_last_request = time.time() - self.last_request_time

        if time_since_last_request < self.rate_limit:
            time.sleep(self.rate_limit - time_since_last_request)

        data = fetch_function(*args, **kwargs)

        self.last_request_time = time.time()

        return data

    def fetch_ticker(self, symbol):
        return self.safe_fetch(self.exchange.fetchTicker, symbol)

    def fetch_ohlcv(self, symbol, timeframe):
        return self.safe_fetch(self.exchange.fetchOHCLV, symbol)

    def fetch_balance(self):
        return self.safe_fetch(self.exchange.fetchBalance)

    def fetch_recent_trades(self, symbol):
        return self.safe_fetch(self.exchange.fetchTrades, symbol)
