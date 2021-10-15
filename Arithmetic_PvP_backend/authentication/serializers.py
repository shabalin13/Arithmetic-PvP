from django.contrib.auth.password_validation import validate_password
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, User
from django.core import exceptions as django_exceptions
from rest_framework import exceptions, serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


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
