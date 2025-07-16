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


def um_notional_and_leverage_brackets():
    try:
        response = client.rest_api.um_notional_and_leverage_brackets()

        rate_limits = response.rate_limits
        logging.info(f"um_notional_and_leverage_brackets() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"um_notional_and_leverage_brackets() response: {data}")
    except Exception as e:
        logging.error(f"um_notional_and_leverage_brackets() error: {e}")


if __name__ == "__main__":
    um_notional_and_leverage_brackets()
