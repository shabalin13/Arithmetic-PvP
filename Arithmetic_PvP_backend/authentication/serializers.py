import logging

from django.contrib.auth.password_validation import validate_password
from djoser.compat import get_user_email_field_name
from djoser.email import PasswordResetEmail
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, User, UserFunctionsMixin
from django.core import exceptions as django_exceptions
from rest_framework import exceptions, serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from djoser.conf import settings


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'username')

    def validate(self, attrs):
        user = User(**attrs)
        password = attrs.get("password")

        if User.objects.filter(email=attrs.get("email")).exists():
            raise ValidationError("User with this email is already exists")

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(serializer_error["non_field_errors"])

        return attrs


class MyUserFunctionsMixin:
    def get_user(self, is_active=True):
        try:
            loc_data = self.initial_data
            user = User.objects.get(username=loc_data.get(self.username_field, ""), email=loc_data.get(self.email_field, ""))
            if user.has_usable_password():
                return user
        except User.DoesNotExist:
            pass
        if (
            settings.PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND
            or settings.USERNAME_RESET_SHOW_EMAIL_NOT_FOUND
        ):
            self.fail("user_not_found")


class MySendEmailResetSerializer(serializers.Serializer, MyUserFunctionsMixin):
    default_error_messages = {
        "user_not_found": "User not found"
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.email_field = get_user_email_field_name(User)
        self.username_field = 'username'

        self.fields[self.email_field] = serializers.EmailField()
        self.fields['username'] = serializers.ReadOnlyField()

