from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Count
from django.utils import timezone
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User
from .models import Player, Room, Task, PlayerInRoom
from .serializers import RoomSerializer, TaskSerializer, UsernameSerializer, \
    PlayerInRoomProgressSerializer, PlayerInRoomResultsSerializer, PlayerSerializer
from .cron import exit_ranked_rooms

BRONZE_END = 999
GOLD_BEGIN, GOLD_END = 1500, 1999
PLATINUM_BEGIN, PLATINUM_END = 2000, 2499
DIAMOND_BEGIN = 2500
PlAYERS_IN_RR_NUM = 4


# single responsibility
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def join_ranked_room(request):
    """Used to join a rating room.
    If there is no rating rooms that didn't begin the new one will be created.
    Returns information about a Room instance player has joined."""
    if request.method == 'PUT':
        player = Player.objects.get(user=request.user)
        room = Room.objects.annotate(players_num=Count('playerinroom')).filter(players_num__lt=PlAYERS_IN_RR_NUM,
                                                                               end_time__gt=timezone.now(),
                                                                               start_time__gt=timezone.now()).exclude(
            playerinroom__player=player).first()
        if room is None:
            room = Room.objects.create_ranked_room()
            # TODO: implement all cases
            if player.rating <= BRONZE_END:
                tasks = [Task.objects.create_easy_task(room, index=i) for i in range(room.tasks_num)]
                for task in tasks:
                    task.save()

            if room.playerinroom_set.count() == PlAYERS_IN_RR_NUM:
                room.start_time = timezone.now()
            room.save()
        player_in_room = PlayerInRoom(player=player, room=room)
        player_in_room.save()
        return Response(RoomSerializer(room).data)


# single responsibility
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_task_rr(request, room_pk):
    """Used to get a task.
    Returns the content of the task to solve."""
    if request.method == 'GET':
        room = get_object_or_404(Room, id=room_pk)
        player = Player.objects.get(user=request.user)
        p_in_r = get_object_or_404(room.playerinroom_set, player=player)
        if room.type != 'RR':
            return Response({'error': 'This room is not rating'})
        if room.end_time <= timezone.now():
            return Response({'error': 'This room already expired'})
        if room.start_time > timezone.now():
            return Response({})
        task = get_object_or_404(Task, room__id=room.pk, index=p_in_r.task_index)
        return Response(TaskSerializer(task).data)


# single responsibility
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def submit_answer_rr(request, room_pk, answer):
    """Used to submit an answer for a task.
    Returns 'is_correct field with the result'"""
    if request.method == 'PUT':
        room = get_object_or_404(Room, id=room_pk)
        player = Player.objects.get(user=request.user)
        p_in_r = get_object_or_404(room.playerinroom_set, player=player)
        if room.type != 'RR':
            return Response({'error': 'This room is not rating'})
        if room.end_time <= timezone.now():
            return Response({'error': 'This room already expired'})
        task = get_object_or_404(Task, room__id=room.pk, index=p_in_r.task_index)

        p_in_r.attempts += 1
        p_in_r.last_activity = timezone.now()
        if task.answer == answer:
            p_in_r.task_index += 1
            p_in_r.save()
            return Response({'is_correct': True})
        else:
            p_in_r.save()
            return Response({'is_correct': False})


# single responsibility
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_nicknames(request, room_pk):
    """Used to get nicknames of players that are currently in a room"""
    if request.method == 'GET':
        room = get_object_or_404(Room, pk=room_pk)
        users_in_r = User.objects.filter(player__playerinroom__room=room)
        return Response(UsernameSerializer(users_in_r, many=True).data)


# single responsibility
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_players_progress(request, room_pk):
    """Used to get progresses of users that are currently in a room"""
    if request.method == 'GET':
        room = get_object_or_404(Room, id=room_pk)
        players_in_r = PlayerInRoom.objects.filter(room=room)
        return Response(PlayerInRoomProgressSerializer(players_in_r, many=True).data)


# singe responsibility
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_player_stats_in_rr(request, room_pk):
    """Used to get player stats when the game finishes
    """
    if request.method == 'GET':
        room = get_object_or_404(Room, id=room_pk)
        players_in_r = PlayerInRoom.objects.filter(room=room)
        return Response(PlayerInRoomResultsSerializer(players_in_r, many=True, context={'request': request}).data)


# singe responsibility
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_player_overall_stats(request):
    """Returns player overall stats"""
    if request.method == 'GET':
        user = request.user
        if user.is_active:
            player = get_object_or_404(Player, user=user)
            return Response(PlayerSerializer(player).data)
        else:
            return Response(status=401)


@api_view(['DELETE'])
def delete_expired_rooms(request):
    """This function is only for testing purposes on non UNIX machines.
    exit_ranked_rooms() normally should be run by cronjob"""
    if request.method == 'DELETE':
        exit_ranked_rooms()
        return Response({'deleted': 'True'})


# singe responsibility
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    """Returns users name and surname"""
    user = request.user
    return Response({"name": user.first_name, "surname": user.last_name})
