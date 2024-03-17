from dotenv import load_dotenv
import os


load_dotenv()


def get_exchange_config():
    return {
        "coinbase": {
            "apiKey": os.getenv("COINBASE_API_KEY"),
            "secret": os.getenv("COINBASE_SECRET")
        }
    }
