from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import exceptions



class CustomJSONWebTokenAuthentication(JSONWebTokenAuthentication):
    """
    code:
        https://github.com/encode/django-rest-framework/blob/master/rest_framework/authentication.py
        https://github.com/GetBlimp/django-rest-framework-jwt/blob/master/rest_framework_jwt/utils.py
        https://github.com/GetBlimp/django-rest-framework-jwt/blob/master/rest_framework_jwt/serializers.py
        https://github.com/GetBlimp/django-rest-framework-jwt/blob/master/rest_framework_jwt/authentication.py
        https://github.com/GetBlimp/django-rest-framework-jwt/blob/master/rest_framework_jwt/serializers.py
        https://github.com/GetBlimp/django-rest-framework-jwt/blob/master/rest_framework_jwt/views.py

    """

    def authenticate_credentials(self, payload):
        """
        Returns an active user that matches the payload's user id and email.
        """
        User = get_user_model()

        try:
            user = User.objects.get_by_natural_key(username)
        except User.DoesNotExist:
            msg = _('Invalid signature.')
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = _('User account is disabled.')
            raise exceptions.AuthenticationFailed(msg)

        return user

