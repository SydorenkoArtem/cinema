from django.urls import include, path

app_name = "api"

urlpatterns = [
    path('user/', include("api.urls.user", namespace="user"), name="user"),
    path('film/', include("api.urls.film", namespace="film"), name="film"),
    path('schedule/', include("api.urls.schedule", namespace="schedule"), name="schedule"),
]
