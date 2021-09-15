from django.db import models
from random import randint
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class RoomManager(models.Manager):
    def create_ranked_room(self):
        creation_ts = timezone.now()
        start_ts = creation_ts + timezone.timedelta(minutes=1)
        end_ts = start_ts + timezone.timedelta(minutes=5)
        room = self.create(type='RT', create_time=creation_ts, start_time=start_ts, end_time=end_ts)
        return room


class Room(models.Model):
    class RoomType(models.TextChoices):
        PRIVATE = 'PR', _('Private room')
        OPEN = 'OP', _('Open room')
        RATING = 'RT', _('Ranked room')

    type = models.CharField(max_length=2, choices=RoomType.choices)
    create_time = models.DateTimeField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    objects = RoomManager()


class TaskManager(models.Manager):
    def create_easy_task(self, room):
        nums_range = 20
        n1, n2, n3 = randint(1, nums_range), randint(1, nums_range), randint(1, nums_range)
        content = "({} + {}) * {}".format(n1, n2, n3)
        answer = (n1 + n2) * n3
        task = self.create(content=content, answer=answer, room=room)
        return task


class Task(models.Model):
    content = models.CharField(max_length=32)
    answer = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    objects = TaskManager()

    def __str__(self):
        return "Task: {}. Room: {}".format(self.pk, self.room_id)


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avg_speed = models.FloatField(default=0)
    avg_accuracy = models.IntegerField(default=100)

    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    task = models.OneToOneField(Task, on_delete=models.SET_NULL, null=True)
    in_game_speed = models.FloatField(default=0)
    in_game_accuracy = models.IntegerField(default=100)
