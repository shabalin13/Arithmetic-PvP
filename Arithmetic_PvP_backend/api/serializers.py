from rest_framework import serializers
from .models import Player, Room, Task, PlayerInRoom
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


# single responsibility
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'create_time', 'start_time', 'end_time', 'tasks_num']


# single responsibility
class PlayerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Player
        fields = ['id', 'user']


class PlayerInRoomSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)

    class Meta:
        model = PlayerInRoom
        fields = ['id', 'task_index', 'player']


# single responsibility
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['content', 'index']
