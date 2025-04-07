import requests
import pandas as pd
from datetime import datetime , timedelta
import logging


# Configuración del logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Evitar múltiples handlers si ya existe uno
if not logger.handlers:
    handler = logging.FileHandler("logs/pipeline.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def fetch_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd",
        "include_last_updated_at": "true"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        price = data["bitcoin"]["usd"]
        timestamp = datetime.fromtimestamp(data["bitcoin"]["last_updated_at"])

        df = pd.DataFrame([{
            "price_usd": price,
            "timestamp": timestamp
        }])

        logger.info("BTC price fetched successfully")
        return df

    except Exception as e:
        logger.error(f"Error fetching BTC price: {e}")
        return pd.DataFrame()


def fetch_bitcoin_hourly_prices(hours=20):
    try:
        end_time = int(datetime.now().timestamp())
        start_time = int((datetime.now() - timedelta(hours=hours)).timestamp())

        url = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range"
        params = {
            "vs_currency": "usd",
            "from": start_time,
            "to": end_time
        }

        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # CoinGecko returns 'prices' as [timestamp, price]
        prices = data.get("prices", [])

        df = pd.DataFrame(prices, columns=["timestamp", "price_usd"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

        logger.info("BTC hourly prices fetched successfully")
        return df

    except Exception as e:
        logger.error(f"Error fetching hourly BTC prices: {e}")
        return pd.DataFrame()
