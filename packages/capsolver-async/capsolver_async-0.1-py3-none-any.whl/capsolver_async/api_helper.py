import json
import platform
from typing import Optional

from httpx import AsyncClient, Response, TimeoutException, HTTPError
from httpx._types import ProxyTypes

from .exceptions import RateLimitError, InvalidRequestError, AuthenticationError, InsufficientCreditError, \
    IncompleteJobError, UnknownError, APIError, Timeout


class ApiHelper:
    def __init__(self, key: str, api_base: str):
        self._key = key
        self._api_base = api_base
        self._session: Optional[AsyncClient] = None

        self._init_session()

    def _init_session(self, proxy: Optional[ProxyTypes] = None):
        user_agent = "pycapsolver"
        uname_without_node = " ".join(v for k, v in platform.uname()._asdict().items() if k != "node")

        capsolver_client_user_agent = {
            "httplib": "httpx",
            "lang": "python",
            "lang_version": platform.python_version(),
            "platform": platform.platform(),
            "publisher": "Qunik",
            "uname": uname_without_node,
        }

        self._session = AsyncClient(
            base_url=self._api_base,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._key}",
                "X-capsolver-Client-User-Agent": json.dumps(capsolver_client_user_agent),
                "User-Agent": user_agent
            },
            proxy=proxy
        )

    async def post(self, url: str, json_data=None) -> dict:
        if json_data is None:
            json_data = {}
        json_data.update({"clientKey": self._key})
        try:
            response = await self._session.post(url, json=json_data)
        except TimeoutException as ex:
            raise Timeout("Request timed out") from ex
        except HTTPError as ex:
            raise APIError("Error communicating with capsolver") from ex
        self._handle_error(response)

        return response.json()

    @staticmethod
    def _handle_error(response: Response):
        try:
            response.json()
        except json.JSONDecodeError:
            raise APIError(f"HTTP code {response.status_code} from API ({response.content})", response)

        response_json = response.json()
        response_code = response.status_code
        error_data = response_json.get("errorDescription")

        match response_code:
            case 429:
                raise RateLimitError(error_data, response)
            case 400:
                raise InvalidRequestError(error_data, response)
            case 401:
                raise AuthenticationError(error_data, response)
            case 403:
                raise InsufficientCreditError(error_data, response)
            case 409:
                raise IncompleteJobError(error_data, response)
            case 200 | 201 | 202 | 204:
                pass
            case _:
                raise UnknownError(error_data, response)
