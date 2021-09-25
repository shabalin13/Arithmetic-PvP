from rest_framework import serializers
from .models import Player, Room, Task


# single responsibility
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['avg_speed']


# single responsibility
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'create_time', 'start_time', 'end_time']


# single responsibility
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['content', 'index']