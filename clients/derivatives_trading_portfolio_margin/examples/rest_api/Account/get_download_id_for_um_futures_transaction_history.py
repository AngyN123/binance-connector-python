import os
import logging

from binance_sdk_derivatives_trading_portfolio_margin.derivatives_trading_portfolio_margin import (
    DerivativesTradingPortfolioMargin,
    ConfigurationRestAPI,
    DERIVATIVES_TRADING_PORTFOLIO_MARGIN_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv(
        "BASE_PATH", DERIVATIVES_TRADING_PORTFOLIO_MARGIN_REST_API_PROD_URL
    ),
)

# Initialize DerivativesTradingPortfolioMargin client
client = DerivativesTradingPortfolioMargin(config_rest_api=configuration_rest_api)


def get_download_id_for_um_futures_transaction_history():
    try:
        response = client.rest_api.get_download_id_for_um_futures_transaction_history(
            start_time=1623319461670,
            end_time=1641782889000,
        )

        rate_limits = response.rate_limits
        logging.info(
            f"get_download_id_for_um_futures_transaction_history() rate limits: {rate_limits}"
        )

        data = response.data()
        logging.info(
            f"get_download_id_for_um_futures_transaction_history() response: {data}"
        )
    except Exception as e:
        logging.error(
            f"get_download_id_for_um_futures_transaction_history() error: {e}"
        )


if __name__ == "__main__":
    get_download_id_for_um_futures_transaction_history()
