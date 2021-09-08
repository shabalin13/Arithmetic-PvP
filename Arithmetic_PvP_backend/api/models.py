from django.db import models
from random import randint
from django.contrib.auth.models import User


class Room(models.Model):
    pass


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
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    in_game_speed = models.FloatField(default=0)
    in_game_accuracy = models.IntegerField(default=100)
    avg_speed = models.FloatField(default=0)
    avg_accuracy = models.IntegerField(default=100)
