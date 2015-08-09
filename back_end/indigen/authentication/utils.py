__author__ = 'fucus'
import jwt

from datetime import datetime

from rest_framework_jwt.settings import api_settings


def jwt_payload_handler(user):
    try:
        username = user.get_username()
    except AttributeError:
        username = user.username

    return {
        'user_id': user.pk,
        'username': username,
        'nickname': user.nickname,
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
    }
