from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Player
from django.utils import timezone


class TestPerm(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        print(view)
        print(obj)
        return obj.user == request.user


class CanJoinNewRoom(permissions.BasePermission):
    def has_permission(self, request, view):
        player = Player.objects.get(user=request.user)
        if player.room is not None:
            if player.room.end_time <= timezone.now():
                player.room.delete()
                return True
            else:
                return False
        else:
            return True
