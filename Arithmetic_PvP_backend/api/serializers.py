from rest_framework import serializers
from .models import Player, Room, Task, PlayerInRoom
from django.contrib.auth.models import User


# single responsibility
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'create_time', 'start_time', 'end_time', 'tasks_num']


class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


#
class PlayerNameSerializer(serializers.ModelSerializer):
    user = UsernameSerializer(read_only=True)

    class Meta:
        model = Player
        fields = ['id', 'user']


class PlayerInRoomProgressSerializer(serializers.ModelSerializer):
    player = PlayerNameSerializer(read_only=True)

    class Meta:
        model = PlayerInRoom
        fields = ['id', 'task_index', 'player']


class PlayerInRoomResultsSerializer(serializers.ModelSerializer):
    player = PlayerNameSerializer(read_only=True)
    place = serializers.SerializerMethodField()
    start_time = serializers.SerializerMethodField()

    class Meta:
        model = PlayerInRoom
        fields = ['id', 'player', 'task_index', 'attempts', 'last_activity', 'place', 'start_time']

    def get_place(self, obj):
        return obj.room.playerinroom_set.filter(task_index__gt=obj.task_index).count() + \
               obj.room.playerinroom_set.filter(task_index=obj.task_index).filter(
                   last_activity__lt=obj.last_activity).count() +\
               obj.room.playerinroom_set.filter(task_index=obj.task_index).filter(
            last_activity=obj.last_activity).filter(attempts__lt=obj.attempts).count() + 1

    def get_start_time(self, obj):
        return obj.room.start_time


class PlayerSerializer(serializers.ModelSerializer):
    user = UsernameSerializer(read_only=True)

    class Meta:
        model = Player
        fields = ['user', 'avg_speed', 'avg_accuracy', 'tasks_solved', 'rating_tasks_solved', 'rating',
                  'matches_played']


# single responsibility
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['content', 'index']
