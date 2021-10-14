import logging

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend, UserModel


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # logging.warning(f"Some one is login with the following credentials:\n\n{username}\n{password}")
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = get_user_model().objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
