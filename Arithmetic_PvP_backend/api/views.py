import json

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Count
from django.utils import timezone
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User, AbstractUser
from .models import Player, Room, Task, PlayerInRoom, SinglePlayerModeLevelsStatistics
from .serializers import RoomSerializer, TaskSerializer, UsernameSerializer, PlayerNameSerializer, \
    PlayerInRoomProgressSerializer, PlayerInRoomResultsSerializer, PlayerSerializer, SingleModelStatisticsSerialize
from .cron import exit_ranked_rooms

BRONZE_END = 999
GOLD_BEGIN, GOLD_END = 1500, 1999
PLATINUM_BEGIN, PLATINUM_END = 2000, 2499
DIAMOND_BEGIN = 2500
PlAYERS_IN_RR_NUM = 4

NUM_OF_LEVELS = 21


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
def get_tasks_rr(request, room_pk):
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
        tasks = get_list_or_404(Task, room__id=room.pk)
        return Response(TaskSerializer(tasks, many=True).data)


# single responsibility
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def submit_answer_rr(request, room_pk, answer):
    """Used to submit an answer for a task.
    Returns 'is_correct' field with the result'"""
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


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_info_about_levels(request):
    if request.method == 'GET':
        user = request.user
        if user.is_active:
            player = get_object_or_404(Player, user=user)
            levels_stats = SinglePlayerModeLevelsStatistics.objects.filter(player=player)
            if levels_stats.count() == 0:
                for i in range(1, NUM_OF_LEVELS + 1):
                    level_stats_new = SinglePlayerModeLevelsStatistics(player=player, index=i)
                    level_stats_new.save()
                level_stats = SinglePlayerModeLevelsStatistics.objects.filter(player=player)

            return Response(SingleModelStatisticsSerialize(levels_stats, many=True).data)
        else:
            return Response(status=401)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def submit_level_info(request):
    if request.method == 'POST':
        user = request.user
        if user.is_active:
            body = json.loads(request.body)
            # decode encoded time with 2-side algo
            level_index = body['index']
            time = body['session_id']
            time += 15324
            time *= 2
            player = get_object_or_404(Player, user=user)

            level_info = SinglePlayerModeLevelsStatistics.objects.get(player=player, index=level_index)

            # If previous level wasn't completed (some bugs or hackers)
            if level_index > 1:
                prev_level = SinglePlayerModeLevelsStatistics.objects.get(player=player, index=level_index - 1)
                if prev_level.time == -1:
                    return Response(status=404)

            if level_info.time == - 1:
                level_info.time = time
                level_info.save()
                return Response(data={'changed': True})
            else:
                if level_info.time > time:
                    level_info.time = time
                    level_info.save()
                    return Response(data={'changed': True})
            return Response(data={'changed': False})

        return Response(status=401)
