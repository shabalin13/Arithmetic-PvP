from django.db import IntegrityError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from api.models import Player, SinglePlayerModeLevelsStatistics
from django.utils.encoding import force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode


NUM_OF_LEVELS = 21

@api_view(["GET"])
@permission_classes([AllowAny])
def activate_user(request, uid, token):
    try:
        pk = force_str(urlsafe_base64_decode(uid))
        user = User.objects.get(pk=pk)
        user.is_active = True
        user.save()
        player = Player(user=user)
        player.save()
        for i in range(1, NUM_OF_LEVELS + 1):
            level_stats = SinglePlayerModeLevelsStatistics(player=player, index=i)
            level_stats.save()
        return Response("User has been created")
    except DjangoUnicodeDecodeError:
        return Response(data="No user with the given credentials", status=404)
    except IntegrityError:
        return Response(data="You already activate your email", status=404)

