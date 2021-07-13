from django.urls import path

from api.view.film import FilmListAPIView, FilmRetrieveUpdateAPIView, GenreListAPIView, GenreRetrieveUpdateAPIView, \
    FilmCreateAPIView, FilmDetailAPIView

app_name = "api"


urlpatterns = [
    path("", FilmListAPIView.as_view(), name="list"),
    path("create/", FilmCreateAPIView.as_view(), name="create"),
    path("<int:pk>/", FilmDetailAPIView.as_view(), name="detail"),
    path("update/<int:pk>/", FilmRetrieveUpdateAPIView.as_view(), name="update"),
    path("genre/", GenreListAPIView.as_view(), name="genre_list"),
    path("genre/<int:pk>/", GenreRetrieveUpdateAPIView.as_view(), name="genre_detail"),
]
