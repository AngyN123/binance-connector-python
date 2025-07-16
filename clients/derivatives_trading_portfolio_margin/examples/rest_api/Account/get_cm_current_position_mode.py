import os
import logging

from binance_derivatives_trading_portfolio_margin.derivatives_trading_portfolio_margin import (
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


def get_cm_current_position_mode():
    try:
        response = client.rest_api.get_cm_current_position_mode()

        rate_limits = response.rate_limits
        logging.info(f"get_cm_current_position_mode() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"get_cm_current_position_mode() response: {data}")
    except Exception as e:
        logging.error(f"get_cm_current_position_mode() error: {e}")


if __name__ == "__main__":
    get_cm_current_position_mode()
