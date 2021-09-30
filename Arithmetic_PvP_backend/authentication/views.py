from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from api.models import Player
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode


@api_view(["GET"])
@permission_classes([AllowAny])
def activate_user(request, uid, token):
    pk = force_str(urlsafe_base64_decode(uid))
    user = User.objects.get(pk=pk)
    user.is_active = True
    user.save()
    player = Player(user=user)
    player.save()
    return Response("User has been created")

