# MangoTrader

This trading bot is designed to automate cryptocurrency trading strategies, leveraging market data to execute trades with the aim of optimizing profitability and minimizing risk. It supports several popular cryptocurrency exchanges through the CCXT library, provides a framework for implementing custom trading strategies, and incorporates essential risk management and notification features.

## Features - IN PROGRESS

- **Support for Multiple Exchanges**: Works with leading exchanges such as Binance and Coinbase.
- **Predefined and Custom Trading Strategies**: Comes with basic strategies like Moving Average Crossover and allows for easy integration of user-defined strategies.
- **Risk Management Tools**: Includes configurable options for stop loss, take profit, and position sizing.
- **Paper Trading Capability**: Test strategies in real-time market conditions without financial risk.
- **Real-Time Notifications**: Receive alerts about trades and market changes through Telegram.

## Getting Started

### Prerequisites

- Python 3.8 or newer
- pip

### Installation

1. Clone the repository and navigate into it:
   ```sh
   git clone https://github.com/yourusername/cryptocurrency-trading-bot.git
   cd cryptocurrency-trading-bot
   ```

2. Install required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

3. Configure the bot by editing `configs/config.json` with your desired parameters and API keys. For security, it's recommended to use environment variables for sensitive information like API keys.

### Running the Bot

Execute the bot from the command line:
```sh
python src/main.py
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes with clear, descriptive messages.
4. Push your branch and submit a pull request against the main branch of this repository.

Please ensure your code adheres to the existing style of the project to make the review process faster.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This trading bot is provided as-is, and it uses speculative trading strategies that can result in losses. Always use caution and trade responsibly. The developers assume no responsibility for financial losses incurred using this software. Trading cryptocurrencies involves significant risk and can result in the loss of your invested capital.

---

This README provides a basic overview of your trading bot project, how to get started with it, and guidelines for contributing. Adjust the content as necessary to fit your project's specifics and ensure that all links (e.g., to the LICENSE file) are correct based on your repository's structure.
