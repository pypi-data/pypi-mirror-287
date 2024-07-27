import json
from typing import Optional

from httpx import Response


class CapsolverError(Exception):
    def __init__(self, message=None, response: Optional[Response] = None):
        super(CapsolverError, self).__init__(message)

        self._message = message
        self.http_body = response.text if response else None
        self.http_status = response.status_code if response else None
        try:
            self.json_body = response.json() if response else None
        except json.JSONDecodeError:
            self.json_body = None
        self.headers = response.headers if response else {}

    def __str__(self):
        return f"{type(self).__name__}: {self._message}" or "<empty message>"


class InvalidRequestError(CapsolverError):
    pass


class IncompleteJobError(CapsolverError):
    pass


class RateLimitError(CapsolverError):
    pass


class AuthenticationError(CapsolverError):
    pass


class InsufficientCreditError(CapsolverError):
    pass


class UnknownError(CapsolverError):
    pass


class Timeout(CapsolverError):
    pass


class APIError(CapsolverError):
    pass


class ServiceUnavailableError(CapsolverError):
    pass
