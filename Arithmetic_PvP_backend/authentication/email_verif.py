from djoser import email
from djoser.email import PasswordResetEmail
from djoser import utils
from djoser.conf import settings
from django.contrib.auth.tokens import default_token_generator


class ActivationEmail(email.ActivationEmail):
    template_name = 'activation.html'

    def get_context_data(self):
        # ActivationEmail can be deleted
        context = super().get_context_data()

        user = context.get("user")
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.ACTIVATION_URL.format(**context)
        context["base_url"] = getattr(settings, "FRONTEND_ADDRESS", None)
        return context


class MyPasswordResetEmail(PasswordResetEmail):
    template_name = "password_reset.html"

    def get_context_data(self):
        # PasswordResetEmail can be deleted
        context = super().get_context_data()

        user = context.get("user")
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.PASSWORD_RESET_CONFIRM_URL.format(**context)
        context["base_url"] = getattr(settings, "FRONTEND_ADDRESS", None)
        return context
