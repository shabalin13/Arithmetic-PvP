#from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
import logging

from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
import requests
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


@api_view(["GET"])
@permission_classes([AllowAny])
def ActivateUser(request, uid, token):
    """
    Intermediate view to activate a user's email.
    """
    post_url = "http://127.0.0.1:8000/api/v1/users/activation/"
    post_data = {"uid": uid, "token": token}
    pk = force_str(urlsafe_base64_decode(uid))
    logging.warning(f"PrimaryKey for the user {pk}")
    user = User.objects.get(pk=pk)
    user.is_active = True
    return Response("User has been created")

