import logging
from abc import ABC
from typing import Any, List, Optional, Union

from eth_typing import URI
from web3 import HTTPProvider, WebsocketProvider
from web3._utils.rpc_abi import RPC
from web3.exceptions import ExtraDataLengthError
from web3.middleware.geth_poa import geth_poa_cleanup
from web3.middleware.validation import _check_extradata_length
from web3.providers import JSONBaseProvider
from web3.types import RPCEndpoint, RPCResponse

logger = logging.getLogger(__name__)


class NoActiveProviderError(Exception):
    """Base exception if all providers are offline"""


class ProtocolNotSupported(Exception):
    """Supported protocols: http, https, ws, wss"""


class BaseMultiProvider(JSONBaseProvider, ABC):
    """Base provider for providers with multiple endpoints"""

    _providers: List[Union[HTTPProvider, WebsocketProvider]] = []

    def __init__(  # pylint: disable=too-many-arguments
        self,
        endpoint_urls: List[Union[URI, str]],
        request_kwargs: Optional[Any] = None,
        session: Optional[Any] = None,
        websocket_kwargs: Optional[Any] = None,
        websocket_timeout: Optional[Any] = None,
    ):
        logger.info({"msg": f"Initialize {self.__class__.__name__}"})
        self._hosts_uri = endpoint_urls
        self._providers = []

        if endpoint_urls:
            self.endpoint_uri = endpoint_urls[0]

        for host_uri in endpoint_urls:
            if host_uri.startswith("ws"):
                self._providers.append(
                    WebsocketProvider(host_uri, websocket_kwargs, websocket_timeout)
                )
            elif host_uri.startswith("http"):
                self._providers.append(HTTPProvider(host_uri, request_kwargs, session))
            else:
                protocol = host_uri.split("://")[0]
                raise ProtocolNotSupported(f'Protocol "{protocol}" is not supported.')

        super().__init__()

    @staticmethod
    def _sanitize_poa_response(method: RPCEndpoint, response: RPCResponse) -> None:
        if method in (RPC.eth_getBlockByHash, RPC.eth_getBlockByNumber):
            if (
                "result" in response
                and isinstance(response["result"], dict)
                and "extraData" in response["result"]
                and "proofOfAuthorityData" not in response["result"]
            ):
                try:
                    _check_extradata_length(response["result"]["extraData"])
                except ExtraDataLengthError:
                    logger.debug({"msg": "PoA blockchain cleanup response."})
                    response["result"] = geth_poa_cleanup(response["result"])


class MultiProvider(BaseMultiProvider):
    """
    Provider that switches rpc endpoint to next if current is broken.
    """

    _current_provider_index: int = 0
    _last_working_provider_index: int = 0

    def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        provider = self._providers[self._current_provider_index]

        try:
            response = provider.make_request(method, params)
        except Exception as error:  # pylint: disable=W0703
            logger.debug(
                {
                    "msg": "Provider not responding.",
                    "error": str(error),
                }
            )

            self._current_provider_index = (self._current_provider_index + 1) % len(
                self._hosts_uri
            )

            provider = self._providers[self._current_provider_index]

            self.endpoint_uri = provider.endpoint_uri

            if self._last_working_provider_index == self._current_provider_index:
                msg = "No active provider available."
                logger.debug({"msg": msg})
                raise NoActiveProviderError(msg) from error

            return self.make_request(method, params)

        else:
            self._sanitize_poa_response(method, response)

            logger.debug(
                {
                    "msg": "Send request using MultiProvider.",
                    "method": method,
                    "params": str(params),
                }
            )
            self._last_working_provider_index = self._current_provider_index
            return response


class FallbackProvider(BaseMultiProvider):
    """Basic fallback provider"""

    def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        for provider in self._providers:
            try:
                response = provider.make_request(method, params)
            except Exception as error:  # pylint: disable=broad-except
                logger.debug(
                    {
                        "msg": "Provider not responding.",
                        "error": str(error),
                    }
                )
            else:
                self._sanitize_poa_response(method, response)

                logger.debug(
                    {
                        "msg": "Send request using FallbackProvider.",
                        "method": method,
                        "params": str(params),
                    }
                )
                return response
        msg = "No active provider available."
        logger.debug({"msg": msg})
        raise NoActiveProviderError(msg)
