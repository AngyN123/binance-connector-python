import os
import logging

from binance_sdk_derivatives_trading_coin_futures.derivatives_trading_coin_futures import (
    DerivativesTradingCoinFutures,
    ConfigurationRestAPI,
    DERIVATIVES_TRADING_COIN_FUTURES_REST_API_PROD_URL,
)
from binance_sdk_derivatives_trading_coin_futures.rest_api.models import (
    KlineCandlestickDataIntervalEnum,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv(
        "BASE_PATH", DERIVATIVES_TRADING_COIN_FUTURES_REST_API_PROD_URL
    ),
)

# Initialize DerivativesTradingCoinFutures client
client = DerivativesTradingCoinFutures(config_rest_api=configuration_rest_api)


def kline_candlestick_data():
    try:
        response = client.rest_api.kline_candlestick_data(
            symbol="symbol_example",
            interval=KlineCandlestickDataIntervalEnum["INTERVAL_1m"].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"kline_candlestick_data() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"kline_candlestick_data() response: {data}")
    except Exception as e:
        logging.error(f"kline_candlestick_data() error: {e}")


if __name__ == "__main__":
    kline_candlestick_data()
