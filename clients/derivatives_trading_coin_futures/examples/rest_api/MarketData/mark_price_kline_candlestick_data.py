import os
import logging

from binance_derivatives_trading_coin_futures.derivatives_trading_coin_futures import (
    DerivativesTradingCoinFutures,
    ConfigurationRestAPI,
    DERIVATIVES_TRADING_COIN_FUTURES_REST_API_PROD_URL,
)
from binance_derivatives_trading_coin_futures.rest_api.models import (
    MarkPriceKlineCandlestickDataIntervalEnum,
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


def mark_price_kline_candlestick_data():
    try:
        response = client.rest_api.mark_price_kline_candlestick_data(
            symbol="symbol_example",
            interval=MarkPriceKlineCandlestickDataIntervalEnum["INTERVAL_1m"].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"mark_price_kline_candlestick_data() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"mark_price_kline_candlestick_data() response: {data}")
    except Exception as e:
        logging.error(f"mark_price_kline_candlestick_data() error: {e}")


if __name__ == "__main__":
    mark_price_kline_candlestick_data()
