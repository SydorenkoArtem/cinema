from django.urls import path

from api.view.film import FilmListAPIView, FilmRetrieveUpdateAPIView, GenreListAPIView, GenreRetrieveUpdateAPIView

app_name = "api"


urlpatterns = [
    path("", FilmListAPIView.as_view(), name="list"),
    path("<int:pk>/", FilmRetrieveUpdateAPIView.as_view(), name="detail"),
    path("genre/", GenreListAPIView.as_view(), name="genre_list"),
    path("genre/<int:pk>/", GenreRetrieveUpdateAPIView.as_view(), name="genre_detail"),
]
