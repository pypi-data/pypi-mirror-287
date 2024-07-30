import httpx
import logging
from typing import Any, Dict
from pydantic import BaseModel

from faimly_t_ddd_core.infrastructure.cross_cutting.facade.endpoint_billing_options import EndPointsPaymentBillingOptions
from faimly_t_ddd_core.infrastructure.cross_cutting.facade.i_message_dispatcher import ResponseDispatcher


class HttpDispatcher:
    def __init__(self, http_client: httpx.AsyncClient, http_endpoint: EndPointsPaymentBillingOptions, logger: logging.Logger):
        self._http_client = http_client
        self._http_endpoint = http_endpoint
        self._logger = logger

    async def dispatch_async(self, message: str) -> ResponseDispatcher:
        try:
            headers = {
                'Content-Type': 'application/json',
                self._http_endpoint.api_header: self._http_endpoint.api_key
            }

            response = await self._http_client.post(
                self._http_endpoint.http_endpoint,
                content=message,
                headers=headers
            )

            response_json = response.text

            return ResponseDispatcher(
                is_success=response.is_success,
                status_code=response.status_code,
                response_json=response_json
            )
        except Exception as ex:
            self._logger.error(ex)
            raise ex
