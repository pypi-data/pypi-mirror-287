import requests
import uuid
import arrow
from .common import (
    get_signature,
    HEADER_REQ_CLIENT_ID,
    HEADER_REQ_ID,
    HEADER_REQ_EXPIRES,
    HEADER_REQ_SIGNATURE,
    HEADER_REQ_USER_TOKEN,
)


class APIClient:
    def __init__(self, base_url, client_id, user_token):
        self.base_url = base_url
        self.client_id = client_id
        self.user_token = user_token

    def _prepare_request(self, method, endpoint, headers=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        default_headers = {
            HEADER_REQ_CLIENT_ID: self.client_id,
            HEADER_REQ_USER_TOKEN: self.user_token,
            HEADER_REQ_ID: str(uuid.uuid4()),
            HEADER_REQ_EXPIRES: str(arrow.utcnow().shift(minutes=5)),
        }
        if headers:
            default_headers.update(headers)

        request = requests.Request(method, url, headers=default_headers, **kwargs)
        prepared_request = request.prepare()
        signature, debug_signature = get_signature(prepared_request)
        prepared_request.headers[HEADER_REQ_SIGNATURE] = signature.hexdigest()
        return prepared_request

    def _send_request(self, prepared_request):
        with requests.Session() as session:
            response = session.send(prepared_request)
            return response

    def post(self, endpoint, data, headers=None):
        prepared_request = self._prepare_request("POST", endpoint, headers, json=data)
        return self._send_request(prepared_request)

    def put(self, endpoint, data, headers=None):
        prepared_request = self._prepare_request("PUT", endpoint, headers, json=data)
        return self._send_request(prepared_request)

    def patch(self, endpoint, data, headers=None):
        prepared_request = self._prepare_request("PATCH", endpoint, headers, json=data)
        return self._send_request(prepared_request)

    def get(self, endpoint, params=None, headers=None):
        prepared_request = self._prepare_request(
            "GET", endpoint, headers, params=params
        )
        return self._send_request(prepared_request)

    def head(self, endpoint, headers=None):
        prepared_request = self._prepare_request("HEAD", endpoint, headers)
        return self._send_request(prepared_request)
