from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

app_name = "api"

urlpatterns = [
    path('user/', include("api.urls.user", namespace="user"), name="user"),
    path('film/', include("api.urls.film", namespace="film"), name="film"),
    path('schedule/', include("api.urls.schedule", namespace="schedule"), name="schedule"),
    path('login/', obtain_auth_token, name="login")
]
