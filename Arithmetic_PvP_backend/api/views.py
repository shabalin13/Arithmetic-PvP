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
from .serializers import PlayerSerializer, RoomSerializer, TaskSerializer
from .cron import exit_ranked_rooms

BRONZE_END = 999
GOLD_BEGIN, GOLD_END = 1500, 1999
PLATINUM_BEGIN, PLATINUM_END = 2000, 2499
DIAMOND_END = 2499
PlAYERS_NUM = 4


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def join_ranked_room(request):
    if request.method == 'PUT':
        player = Player.objects.get(user=request.user)
        room = Room.objects.annotate(players_num=Count('playerinroom')).filter(players_num__lt=PlAYERS_NUM,
                                                                               end_time__gt=timezone.now()).exclude(
            playerinroom__player=player).first()
        if room is None:
            room = Room.objects.create_ranked_room()
            # TODO: implement all cases
            if player.rating <= BRONZE_END:
                tasks = [Task.objects.create_easy_task(room, index=i) for i in range(room.tasks_num)]
                for task in tasks:
                    task.save()
            room.save()
        player_in_room = PlayerInRoom(player=player, room=room)
        player_in_room.save()
        return Response(RoomSerializer(room).data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_task_rr(request, room_pk):
    if request.method == 'GET':
        room = get_object_or_404(Room, id=room_pk)
        player = Player.objects.get(user=request.user)
        p_in_r = get_object_or_404(room.playerinroom_set, player=player)
        if room.type != 'RR':
            return Response({'error': 'This room is not rating'})
        if room.end_time <= timezone.now():
            return Response({'error': 'This room already expired'})
        task = Task.objects.get(room__id=room_pk, index=p_in_r.task_index)
        return Response(TaskSerializer(task).data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def submit_answer_rr(request, room_pk, answer):
    if request.method == 'PUT':
        room = get_object_or_404(Room, id=room_pk)
        player = Player.objects.get(user=request.user)
        p_in_r = get_object_or_404(room.playerinroom_set, player=player)
        if room.type != 'RR':
            return Response({'error': 'This room is not rating'})
        if room.end_time <= timezone.now():
            return Response({'error': 'This room already expired'})
        task = Task.objects.get(room__id=room_pk, index=p_in_r.task_index)

        p_in_r.attempts += 1
        p_in_r.last_activity = timezone.now()
        if task.answer == answer:
            p_in_r.task_index += 1
            p_in_r.save()
            return Response({'is_correct': True})
        else:
            p_in_r.save()
            return Response({'is_correct': False})


@api_view(['DELETE'])
def delete_expired_rooms(request):
    if request.method == 'DELETE':
        exit_ranked_rooms()
        return Response({'deleted': 'True'})


@api_view(['GET'])
def get_players_num(request, pk):
    if request.method == 'GET':
        room = get_object_or_404(Room, pk=pk)
        players = room.playerinroom_set.count()
        return Response({'players_num': players})
