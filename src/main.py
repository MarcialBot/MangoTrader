from data.market_data import MarketDataFetcher
# from strategies.basic_strategy import should_buy
# from execution.simulator import execute_buy
from utils.logger import log_info


def main():
    fetcher = MarketDataFetcher("coinbase")
    symbol = 'BTC/USDT'
    last_price = fetcher.fetch_ticker(symbol)
    log_info(f"Last price of {symbol}: {last_price}")

#    if should_buy(last_price):
#        execute_buy(symbol, last_price)


if __name__ == "__main__":
    main()
