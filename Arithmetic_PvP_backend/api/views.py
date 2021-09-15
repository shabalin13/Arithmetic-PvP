from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Count
from django.utils import timezone
from . import permissions
from .models import Player, Room
from .serializers import PlayerSerializer, RoomSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test(request):
    if request.method == 'GET':
        players = Player.objects.all()

        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, permissions.CanJoinNewRoom])
def join_ranked_room(request):
    if request.method == 'PUT':
        player = Player.objects.get(user=request.user)
        room = Room.objects.annotate(players_num=Count('player')).filter(players_num__lt=5,
                                                                         end_time__gt=timezone.now()).first()
        if room is None:
            room = Room.objects.create_ranked_room()
        player.room = room
        return


class PlayersNum(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
