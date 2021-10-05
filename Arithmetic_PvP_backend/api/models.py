from django.db import models
from random import randint
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


# open/closed principle
# to create a room differently one can just add new function
class RoomManager(models.Manager):
    # TODO: create different room types with different difficulties
    def create_ranked_room(self):
        creation_ts = timezone.now()
        start_ts = creation_ts + timezone.timedelta(minutes=1)
        end_ts = start_ts + timezone.timedelta(minutes=5)
        tasks_num = 10
        room = self.create(type='RR', create_time=creation_ts, start_time=start_ts, end_time=end_ts, tasks_num=tasks_num)
        return room


class Room(models.Model):
    class RoomType(models.TextChoices):
        PRIVATE = 'PR', _('Private room')
        OPEN = 'OR', _('Open room')
        RATING = 'RR', _('Ranked room')
        CAMPAIGN = 'CR', _('Campaign room')

    type = models.CharField(max_length=2, choices=RoomType.choices)
    create_time = models.DateTimeField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    tasks_num = models.SmallIntegerField()

    objects = RoomManager()


# open/closed principle
class TaskManager(models.Manager):
    def create_easy_task(self, room, index):
        nums_range = 10
        n1, n2, n3 = randint(1, nums_range), randint(1, nums_range), randint(1, nums_range)
        content = "({} + {}) * {}".format(n1, n2, n3)
        answer = (n1 + n2) * n3
        task = self.create(content=content, answer=answer, room=room, index=index)
        return task


class Task(models.Model):
    content = models.CharField(max_length=32)
    answer = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    index = models.IntegerField()

    objects = TaskManager()

    def __str__(self):
        return "Task: {}. Room: {}".format(self.pk, self.room_id)


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # speed in seconds per task
    avg_speed = models.FloatField(default=0)
    avg_accuracy = models.FloatField(default=1)
    tasks_solved = models.IntegerField(default=0)
    rating_tasks_solved = models.IntegerField(default=0)
    rating = models.IntegerField(default=500)
    matches_played = models.IntegerField(default=0)


class PlayerInRoom(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    # actual only for one game
    room = models.ForeignKey(Room, on_delete=models.CASCADE,  blank=True)
    task_index = models.IntegerField(default=0)
    attempts = models.IntegerField(default=0)
    last_activity = models.DateTimeField(default=timezone.now)
