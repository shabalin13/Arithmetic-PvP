from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('get_players_num/<int:pk>/', views.get_players_num),
    path('join_ranked_room/', views.join_ranked_room),
]

urlpatterns = format_suffix_patterns(urlpatterns)
