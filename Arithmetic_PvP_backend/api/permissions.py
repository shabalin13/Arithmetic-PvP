from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.exceptions import ObjectDoesNotExist
from .models import Player
from django.utils import timezone


class IsPlayer(permissions.BasePermission):
    message = "You are not a player"

    def has_permission(self, request, view):
        try:
            player = Player.objects.get(user=request.user)
            return True
        except ObjectDoesNotExist:
            return False


class IsInRoom(IsPlayer):
    message = "The player is not in any room"

    def has_permission(self, request, view):
        if not IsPlayer.has_permission(self, request, view):
            self.message = IsPlayer.message
            return False
        player = Player.objects.get(user=request.user)
        if player.room is None:
            return False
        return True


class IsNotInRoom(IsPlayer):
    message = "Player is already in a room"

    def has_permission(self, request, view):
        if not IsPlayer.has_permission(self, request, view):
            self.message = IsPlayer.message
            return False
        player = Player.objects.get(user=request.user)
        if player.room is not None:
            return False
        return True


class IsInRankedRoom(IsPlayer):
    message = "The player is not in ranked room"

    def has_permission(self, request, view):
        if not IsPlayer.has_permission(self, request, view):
            self.message = IsPlayer.message
            return False
        player = Player.objects.get(user=request.user)
        if player.room is None:
            return False
        if player.room.type != 'PR':
            return False
        return True
