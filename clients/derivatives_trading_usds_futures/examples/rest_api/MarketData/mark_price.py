import os
import logging

from binance_derivatives_trading_usds_futures.derivatives_trading_usds_futures import (
    DerivativesTradingUsdsFutures,
    ConfigurationRestAPI,
    DERIVATIVES_TRADING_USDS_FUTURES_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv(
        "BASE_PATH", DERIVATIVES_TRADING_USDS_FUTURES_REST_API_PROD_URL
    ),
)

# Initialize DerivativesTradingUsdsFutures client
client = DerivativesTradingUsdsFutures(config_rest_api=configuration_rest_api)


def mark_price():
    try:
        response = client.rest_api.mark_price()

        rate_limits = response.rate_limits
        logging.info(f"mark_price() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"mark_price() response: {data}")
    except Exception as e:
        logging.error(f"mark_price() error: {e}")


if __name__ == "__main__":
    mark_price()
