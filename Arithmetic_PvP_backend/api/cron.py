from .models import Player, PlayerInRoom, Room
from django.db.models import Avg
from django.utils import timezone


def exit_ranked_rooms():
    rooms = Room.objects.filter(type='RR').filter(end_time__lte=timezone.now())
    for room in rooms:
        players = room.playerinroom_set.order_by('-task_index', 'last_activity')
        players_num = players.count()

        new_rating = []
        players_list = []
        place = 0
        for player_in_room in players:
            player = player_in_room.player

            exit_time = min(room.end_time, player_in_room.last_activity)
            player.avg_speed = player.avg_speed * player.tasks_solved / (
                        player.tasks_solved + player_in_room.task_index) + (
                                           exit_time - room.start_time).total_seconds() / (
                                           player.tasks_solved + player_in_room.task_index)
            player.avg_accuracy = (player.rating_tasks_solved + player_in_room.task_index) / \
                                  (player.tasks_solved / player.avg_accuracy + player_in_room.attempts)
            player.rating_tasks_solved += player_in_room.task_index
            player.tasks_solved += player_in_room.task_index
            player.save()

            # elo rating used
            avg_enemy_rating = players.exclude(id=player_in_room.pk).aggregate(Avg('player__rating'))
            player_rating = player.rating
            expected_rating = 1 / (1 + 10 ** ((avg_enemy_rating - player_rating) / 400))
            k = 20
            game_score = 1 - (1 / (players_num - 1) * place)
            new_rating.append(player_rating + k * (game_score - expected_rating))
            players_list.append(player)
            place += 1

        for i in range(len(players_list)):
            players_list[i] = new_rating[i]
            players_list[i].save()

        del room
