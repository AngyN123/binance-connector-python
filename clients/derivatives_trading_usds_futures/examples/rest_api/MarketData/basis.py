import os
import logging

from binance_derivatives_trading_usds_futures.derivatives_trading_usds_futures import (
    DerivativesTradingUsdsFutures,
    ConfigurationRestAPI,
    DERIVATIVES_TRADING_USDS_FUTURES_REST_API_PROD_URL,
)
from binance_derivatives_trading_usds_futures.rest_api.models import (
    BasisContractTypeEnum,
)
from binance_derivatives_trading_usds_futures.rest_api.models import BasisPeriodEnum


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


def basis():
    try:
        response = client.rest_api.basis(
            pair="pair_example",
            contract_type=BasisContractTypeEnum["PERPETUAL"].value,
            period=BasisPeriodEnum["PERIOD_5m"].value,
            limit=30,
        )

        rate_limits = response.rate_limits
        logging.info(f"basis() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"basis() response: {data}")
    except Exception as e:
        logging.error(f"basis() error: {e}")


if __name__ == "__main__":
    basis()
