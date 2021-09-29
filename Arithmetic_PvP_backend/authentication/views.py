#from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
import logging

from rest_framework.response import Response
#from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
import requests


@api_view(["GET"])
@permission_classes([AllowAny])
def ActivateUser(request, uid, token):
    """
    Intermediate view to activate a user's email.
    """
    post_url = "http://127.0.0.1:8000/api/v1/users/activation/"
    post_data = {"uid": uid, "token": token}
    result = requests.post(post_url, json=post_data)
    content = result.text
    logging.warning(result.text)
    return Response(content)

