from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('delete_expired_rooms/', views.delete_expired_rooms),
    path('get_nicknames/<int:room_pk>/', views.get_nicknames),
    path('get_rr_progress/<int:room_pk>/', views.get_players_progress),
    path('get_rr_stats/<int:room_pk>/', views.get_player_stats_in_rr),
    path('get_player_overall_stats/', views.get_player_overall_stats),
    path('ranked_room/join/', views.join_ranked_room),
    path('ranked_room/get_task/<int:room_pk>/', views.get_task_rr),
    path('ranked_room/submit_task/<int:room_pk>/<int:answer>/', views.submit_answer_rr),


    path('get_user_info/', views.get_user_info)
]

urlpatterns = format_suffix_patterns(urlpatterns)
