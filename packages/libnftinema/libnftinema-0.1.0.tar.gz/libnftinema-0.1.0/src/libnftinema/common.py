from urllib.parse import urlparse

import arrow
import hashlib
import hmac
import json
from collections import OrderedDict

from django.conf import settings
from django.core.exceptions import ValidationError


HEADER_REQ_CLIENT_ID = "X-Request-Client-Id"
HEADER_REQ_ID = "X-Request-Idempotency-Key"
HEADER_REQ_EXPIRES = "X-Request-Expires"
HEADER_REQ_SIGNATURE = "X-Request-Signature"
HEADER_REQ_DEBUG_SIGNATURE = "X-Request-Debug-Signature"
HEADER_REQ_USER_TOKEN = "X-Request-User-Token"


def get_signature(request) -> (str, str):
    KEY = settings.NFTINEMA_CLIENT_SECRET.encode()
    headers = OrderedDict(
        sorted(
            (k, v)
            for k, v in request.headers.items()
            if k.lower()
            in [
                HEADER_REQ_CLIENT_ID.lower(),
                HEADER_REQ_USER_TOKEN.lower(),
                HEADER_REQ_ID.lower(),
                HEADER_REQ_EXPIRES.lower(),
            ]
        )
    )
    headers_hash = hmac.new(KEY, json.dumps(headers).encode("utf-8"), hashlib.sha1)

    if hasattr(request, "build_absolute_uri"):
        full_url = request.build_absolute_uri()
    else:
        full_url = request.url

    url_parts = urlparse(full_url)
    query_string = url_parts.query.encode("utf-8")
    qs_hash = hmac.new(KEY, query_string, hashlib.sha1)

    body_hash = hmac.new(KEY, request.body, hashlib.sha1)

    debug_signature = (
        f"headers:{headers_hash.hexdigest()},"
        f"qs:{qs_hash.hexdigest()},"
        f"body:{body_hash.hexdigest()}"
    )

    signature = hmac.new(KEY, debug_signature.encode("utf-8"), hashlib.sha1)

    return signature, debug_signature


def validate_signature(request) -> (str, str):
    now = arrow.utcnow()
    expires = request.headers.get(HEADER_REQ_EXPIRES)
    if not expires:
        raise ValidationError(f"Missing {HEADER_REQ_EXPIRES} header")
    expires = arrow.get(expires)
    if expires < now:
        raise ValidationError(f"Request expired at {expires}")

    signature, debug_signature = get_signature(request)
    if signature.hexdigest() != request.headers.get(HEADER_REQ_SIGNATURE):
        raise ValidationError(
            f"Invalid signature {signature.hexdigest()} != {request.headers.get(HEADER_REQ_SIGNATURE)}"
        )

    return signature, debug_signature


def add_signature_to_request(request):
    pass
