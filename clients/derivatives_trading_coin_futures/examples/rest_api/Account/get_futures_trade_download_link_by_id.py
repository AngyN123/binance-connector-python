import os
import logging

from binance_derivatives_trading_coin_futures.derivatives_trading_coin_futures import (
    DerivativesTradingCoinFutures,
    ConfigurationRestAPI,
    DERIVATIVES_TRADING_COIN_FUTURES_REST_API_PROD_URL,
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


def get_futures_trade_download_link_by_id():
    try:
        response = client.rest_api.get_futures_trade_download_link_by_id(
            download_id="1",
        )

        rate_limits = response.rate_limits
        logging.info(
            f"get_futures_trade_download_link_by_id() rate limits: {rate_limits}"
        )

        data = response.data()
        logging.info(f"get_futures_trade_download_link_by_id() response: {data}")
    except Exception as e:
        logging.error(f"get_futures_trade_download_link_by_id() error: {e}")


if __name__ == "__main__":
    get_futures_trade_download_link_by_id()
