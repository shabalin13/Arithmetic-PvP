from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('delete_expired_rooms/', views.delete_expired_rooms),
    path('get_players_num/<int:pk>/', views.get_players_num),
    path('ranked_room/join/', views.join_ranked_room),
    path('ranked_room/get_task/<int:room_pk>/', views.get_task_rr),
    path('ranked_room/submit_task/<int:room_pk>/<int:answer>/', views.submit_answer_rr),
]

urlpatterns = format_suffix_patterns(urlpatterns)
