# Compression

```python
import asyncio
import logging

from binance_common.configuration import ConfigurationWebSocketAPI
from binance_sdk_derivatives_trading_coin_futures.derivatives_trading_coin_futures import DerivativesTradingCoinFutures
from binance_sdk_derivatives_trading_coin_futures.websocket_api.models import PositionInformationResponse

logging.basicConfig(level=logging.INFO)

configuration_ws_api = ConfigurationWebSocketAPI(
    compression=0,
)

client = DerivativesTradingCoinFutures(config_ws_api=configuration_ws_api)


async def position_information():
    connection = None
    try:
        connection = await client.websocket_api.create_connection()

        response = await client.websocket_api.position_information(
            symbol="BNBUSDT",
        )

        data: PositionInformationResponse = response.data()
        logging.info(f"position_information() response: {data}")
    except Exception as e:
        logging.error(f"position_information() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)

if __name__ == "__main__":
    asyncio.run(position_information())
```
