import loguru

from rest_framework import authentication
from rest_framework import exceptions
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from django.core.exceptions import ValidationError as DjangoValidationError
from uuid import uuid4, UUID

from .common import validate_signature, HEADER_REQ_USER_TOKEN


class NftinemaAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            _, debug_signature = validate_signature(request)
            loguru.logger.debug(f"Validated signature: {debug_signature}")
            token = request.headers.get(HEADER_REQ_USER_TOKEN)
            if not token:
                loguru.logger.debug("No user token provided")
                raise AuthenticationFailed("No user token provided")

            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_uuid = payload.get("uuid")
            if not user_uuid:
                loguru.logger.debug("Invalid token")
                raise AuthenticationFailed("Invalid token")

            User = get_user_model()
            user, created = User.objects.update_or_create(
                username=user_uuid, defaults={"uuid": UUID(user_uuid)}
            )
            return (user, None)
        except (
            jwt.ExpiredSignatureError,
            jwt.InvalidTokenError,
            ValidationError,
            DjangoValidationError,
        ) as e:
            raise AuthenticationFailed(str(e))
