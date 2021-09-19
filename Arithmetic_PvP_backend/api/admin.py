from django.contrib import admin

# Register your models here.
from api.models import Room, Task, Player, PlayerInRoom

admin.site.register(Room)
admin.site.register(Task)
admin.site.register(Player)
admin.site.register(PlayerInRoom)