from rest_framework import serializers
from .models import Player, Room, Task, PlayerInRoom
from django.contrib.auth.models import User


# single responsibility
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'avg_speed', 'avg_accuracy', 'tasks_solved', 'rating_tasks_solved', 'rating', 'matches_played']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


# single responsibility
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'create_time', 'start_time', 'end_time', 'tasks_num']


class PlayerInRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerInRoom
        fields = ['id', 'task_index', 'player']


# single responsibility
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['content', 'index']