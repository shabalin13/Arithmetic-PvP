from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Count
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist

from . import permissions
from .models import Player, Room, Task, PlayerInRoom
from .serializers import PlayerSerializer, RoomSerializer
from .cron import exit_ranked_rooms

BRONZE_END = 999
SILVER_BEGIN, SILVER_END = 1000, 1499
GOLD_BEGIN, GOLD_END = 1500, 1999
PLATINUM_BEGIN, PLATINUM_END = 2000, 2499
DIAMOND_END = 2499
PlAYERS_NUM = 4


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def join_ranked_room(request):
    if request.method == 'PUT':
        player = Player.objects.get(user=request.user)
        room = Room.objects.annotate(players_num=Count('player')).filter(players_num__lt=PlAYERS_NUM,
                                                                         end_time__gt=timezone.now()).exclude(
            playerinroom__player__id=player.pk).first()
        if room is None:
            room = Room.objects.create_ranked_room()
            if player.rating <= BRONZE_END:
                tasks = [Task.objects.create_easy_task(room, i) for i in range(room.tasks_num)]
                for task in tasks:
                    task.save()
            room.save()
        player_in_room = PlayerInRoom(player=player, room=room)
        player_in_room.save()
        return Response(RoomSerializer(room).data)


@api_view(['GET'])
@permission_classes([IsAuthenticated, permissions.IsInRoom])
def get_next_task(request):
    pass


@api_view(['DELETE'])
def delete_expired_rooms(request):
    if request.method == 'DELETE':
        exit_ranked_rooms()
        return Response({'deleted': 'True'})


@api_view(['GET'])
def get_players_num(request, pk):
    if request.method == 'GET':
        room = get_object_or_404(Room, pk=pk)
        players = room.player_set.count()
        return Response({'players_num': players})
