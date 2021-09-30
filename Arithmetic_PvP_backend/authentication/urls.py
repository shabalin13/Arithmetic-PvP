from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # path('google/', views.GoogleLogin.as_view(), name='google_login'),
    path('<str:uid>/<str:token>', views.activate_user)
]

urlpatterns = format_suffix_patterns(urlpatterns)
