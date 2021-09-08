from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import Player
from .serializers import PlayerSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def test(request):
    if request.method == 'GET':
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)
