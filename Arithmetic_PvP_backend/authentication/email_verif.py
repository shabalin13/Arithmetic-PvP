from djoser import email
from djoser.email import PasswordResetEmail


class ActivationEmail(email.ActivationEmail):
    template_name = 'activation.html'


class MyPasswordResetEmail(PasswordResetEmail):
    template_name = "password_reset.html"
