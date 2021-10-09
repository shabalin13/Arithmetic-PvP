from rest_framework import permissions
from django.core.exceptions import ObjectDoesNotExist
from .models import Player
from django.utils import timezone
from django.shortcuts import get_object_or_404


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
        if player.room.type != 'RR':
            return False
        return True


class IsInActiveRankedRoom(permissions.BasePermission):
    message = "This room is not active ranked room or player is not in this room"

    def has_object_permission(self, request, view, obj):
        player = Player.objects.get(user=request.user)
        p_in_r = get_object_or_404(obj.playerinroom_set, player=player)
        if obj.type != 'RR':
            return False
        if obj.end_time <= timezone.now():
            return False
        if obj.start_time > timezone.now():
            return False
        return True
