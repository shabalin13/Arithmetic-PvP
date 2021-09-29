import logging

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend, UserModel


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        logging.warning(f"Some one is login with the following credentials:\n\n{username}\n{password}")
        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=username)
        except UserModel.DoesNotExist:
            try:
                user = user_model.objects.get(username=username)
            except UserModel.DoesNotExist:
                return None
            else:
                if user.check_password(password):
                    return user
        else:
            if user.check_password(password):
                return user
        return None
