from .models import Player, PlayerInRoom, Room
from django.db.models import Avg
from django.utils import timezone


def exit_ranked_rooms():
    def calculate_avg_speed(player, player_in_room):
        exit_time = min(room.end_time, player_in_room.last_activity)
        try:
            return player.avg_speed * player.tasks_solved / (
                    player.tasks_solved + player_in_room.task_index) + (
                           exit_time - room.start_time).total_seconds() / (
                           player.tasks_solved + player_in_room.task_index)
        except ZeroDivisionError:
            return 0

    def calculate_avg_accuracy(player, player_in_room):
        try:
            return (player.rating_tasks_solved + player_in_room.task_index) / \
                                  (player.tasks_solved / player.avg_accuracy + player_in_room.attempts)
        except ZeroDivisionError:
            return 1

    def calculate_new_rating(player, players, place):
        players_num = players.count()
        if players_num > 1:
            avg_enemy_rating = players.exclude(id=player.pk).aggregate(Avg('player__rating'))
            expected_rating = 1 / (1 + 10 ** ((avg_enemy_rating - player.rating) / 400))
            k = 20
            game_score = 1 - (1 / (players_num - 1) * place)
            return player.rating + k * (game_score - expected_rating)
        else:
            return player.rating

    def calculate_ratings(p_in_r_ordered):
        players = Player.objects.filter(playerinroom__in=p_in_r_ordered)
        rating_list = []
        place = 0
        for p_in_r in p_in_r_ordered:
            rating_list.append(calculate_new_rating(p_in_r.player, players, place))
            place += 1
        return rating_list

    def update_player_stats(player, player_in_room, rating):
        player.avg_speed = calculate_avg_speed(player, player_in_room)
        player.avg_accuracy = calculate_avg_accuracy(player, player_in_room)
        player.rating_tasks_solved += player_in_room.task_index
        player.tasks_solved += player_in_room.task_index
        player.matches_played += 1
        player.rating = rating
        player.save()

    def update_all_stats(p_in_r_ordered):
        rating_list = calculate_ratings(p_in_r_ordered)
        i = 0
        for p_in_r in p_in_r_ordered:
            update_player_stats(p_in_r.player, p_in_r, rating_list[i])
            i += 1

    rooms = Room.objects.filter(type='RR').filter(end_time__lte=timezone.now())
    for room in rooms:
        p_in_r_sorted = room.playerinroom_set.order_by('-task_index', 'last_activity')
        update_all_stats(p_in_r_sorted)

        room.delete()
