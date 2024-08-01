import pytest
from unittest.mock import MagicMock, patch
from requests import Request, Session
from .client import APIClient
from .common import (
    HEADER_REQ_CLIENT_ID,
    HEADER_REQ_USER_TOKEN,
    HEADER_REQ_ID,
    HEADER_REQ_EXPIRES,
    HEADER_REQ_SIGNATURE,
    get_signature,
)
import jwt
import arrow
import uuid
from django.conf import settings

CLIENT_ID = "your_client_id"
USER_UUID = str(uuid.uuid4())
USER_TOKEN = jwt.encode({"uuid": USER_UUID}, settings.SECRET_KEY, algorithm="HS256")


@pytest.fixture
def api_client():
    return APIClient(
        base_url="http://testserver/api", client_id=CLIENT_ID, user_token=USER_TOKEN
    )


@pytest.fixture
def mock_session_send():
    with patch.object(Session, "send", autospec=True) as mock_send:
        yield mock_send


def prepare_request(method, endpoint, data=None):
    request = Request(
        method,
        url=f"http://testserver/api/{endpoint}",
        json=data,
        headers={
            HEADER_REQ_CLIENT_ID: CLIENT_ID,
            HEADER_REQ_USER_TOKEN: USER_TOKEN,
            HEADER_REQ_ID: str(uuid.uuid4()),
            HEADER_REQ_EXPIRES: str(arrow.utcnow().shift(minutes=5)),
        },
    )
    prepared_request = request.prepare()
    signature, _ = get_signature(prepared_request)
    prepared_request.headers[HEADER_REQ_SIGNATURE] = signature.hexdigest()
    return prepared_request


def test_post(api_client, mock_session_send):
    data = {"key": "value"}
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_session_send.return_value = mock_response

    response = api_client.post("custom-auth/", data)
    assert response.status_code == 200


def test_put(api_client, mock_session_send):
    data = {"key": "value"}
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_session_send.return_value = mock_response

    response = api_client.put("custom-auth/", data)
    assert response.status_code == 200


def test_patch(api_client, mock_session_send):
    data = {"key": "value"}
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_session_send.return_value = mock_response

    response = api_client.patch("custom-auth/", data)
    assert response.status_code == 200


def test_get(api_client, mock_session_send):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_session_send.return_value = mock_response

    response = api_client.get("custom-auth/")
    assert response.status_code == 200


def test_head(api_client, mock_session_send):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_session_send.return_value = mock_response

    response = api_client.head("custom-auth/")
    assert response.status_code == 200
