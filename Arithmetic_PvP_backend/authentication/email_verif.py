from djoser import email


class ActivationEmail(email.ActivationEmail):
    template_name = 'activation.html'

