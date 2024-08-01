# libnftinema/test_server.py
import pytest
import jwt
import uuid
import arrow
from django.conf import settings
from django.core.exceptions import ValidationError
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.test import APIRequestFactory
from django.contrib.auth import get_user_model
from .common import (
    HEADER_REQ_CLIENT_ID,
    HEADER_REQ_USER_TOKEN,
    HEADER_REQ_ID,
    HEADER_REQ_EXPIRES,
    HEADER_REQ_SIGNATURE,
    get_signature,
)
from .server import NftinemaAuthentication

CLIENT_ID = "your_client_id"
USER_UUID = str(uuid.uuid4())
USER_TOKEN = jwt.encode({"uuid": USER_UUID}, settings.SECRET_KEY, algorithm="HS256")


def prepare_request(method, url, data=None, override_headers=None):
    factory = APIRequestFactory()
    headers = {
        HEADER_REQ_CLIENT_ID: CLIENT_ID,
        HEADER_REQ_USER_TOKEN: USER_TOKEN,
        HEADER_REQ_ID: str(uuid.uuid4()),
        HEADER_REQ_EXPIRES: str(arrow.utcnow().shift(minutes=5)),
    }
    if override_headers:
        headers.update(override_headers)

    request = factory.generic(
        method, url, data, content_type="application/json", **headers
    )
    request.META[f"HTTP_{HEADER_REQ_EXPIRES.replace('-', '_').upper()}"] = headers[
        HEADER_REQ_EXPIRES
    ]
    request.META[f"HTTP_{HEADER_REQ_USER_TOKEN.replace('-', '_').upper()}"] = headers[
        HEADER_REQ_USER_TOKEN
    ]
    request.META[f"HTTP_{HEADER_REQ_CLIENT_ID.replace('-', '_').upper()}"] = headers[
        HEADER_REQ_CLIENT_ID
    ]
    request.META[f"HTTP_{HEADER_REQ_ID.replace('-', '_').upper()}"] = headers[
        HEADER_REQ_ID
    ]

    request.headers = headers  # Manually set headers if not already present
    signature, _ = get_signature(request)
    request.META[f"HTTP_{HEADER_REQ_SIGNATURE.replace('-', '_').upper()}"] = (
        signature.hexdigest()
    )

    request.headers[HEADER_REQ_SIGNATURE] = signature.hexdigest()
    return request


@pytest.fixture
def auth_instance():
    return NftinemaAuthentication()


@pytest.fixture
def user(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        User = get_user_model()
        return User.objects.create_user(username=USER_UUID, uuid=USER_UUID)


@pytest.mark.django_db
def test_authenticate_success(auth_instance, user):
    request = prepare_request("POST", "/test-url/", data={"key": "value"})
    authenticated_user, _ = auth_instance.authenticate(request)
    assert authenticated_user.username == USER_UUID


@pytest.mark.django_db
def test_authenticate_missing_user_token(auth_instance):
    request = prepare_request(
        "POST",
        "/test-url/",
        data={"key": "value"},
        override_headers={HEADER_REQ_USER_TOKEN: ""},
    )
    with pytest.raises(AuthenticationFailed, match="No user token provided"):
        auth_instance.authenticate(request)


@pytest.mark.django_db
def test_authenticate_invalid_token(auth_instance):
    invalid_token = jwt.encode(
        {"uuid": str(uuid.uuid4())}, "wrong_secret", algorithm="HS256"
    )
    request = prepare_request(
        "POST",
        "/test-url/",
        data={"key": "value"},
        override_headers={HEADER_REQ_USER_TOKEN: invalid_token},
    )
    with pytest.raises(AuthenticationFailed, match="Signature verification failed"):
        auth_instance.authenticate(request)


@pytest.mark.django_db
def test_authenticate_expired_signature(auth_instance):
    expired_time = str(arrow.utcnow().shift(minutes=-1))
    request = prepare_request(
        "POST",
        "/test-url/",
        data={"key": "value"},
        override_headers={HEADER_REQ_EXPIRES: expired_time},
    )
    # request.META[f"HTTP_{HEADER_REQ_EXPIRES.replace('-', '_').upper()}"] = expired_time
    # request.headers[HEADER_REQ_EXPIRES] = expired_time
    with pytest.raises(AuthenticationFailed, match="Request expired at"):
        auth_instance.authenticate(request)


@pytest.mark.django_db
def test_authenticate_invalid_signature(auth_instance):
    request = prepare_request("POST", "/test-url/", data={"key": "value"})
    request.META[f"HTTP_{HEADER_REQ_SIGNATURE.replace('-', '_').upper()}"] = (
        "invalid_signature"
    )
    request.headers[HEADER_REQ_SIGNATURE] = "invalid_signature"
    with pytest.raises(AuthenticationFailed, match="Invalid signature"):
        auth_instance.authenticate(request)
