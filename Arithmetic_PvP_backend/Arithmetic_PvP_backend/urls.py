from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # path('auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'), name='api_root'),
    path('api-auth', include('rest_framework.urls')),

    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('activate/', include('authentication.urls'))
    #path('api/v1/users', include('djoser'))

]
