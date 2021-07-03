"""
Store Application URLs Configuration
====================================

"""

from django.urls import path

from film.views import FilmCreateView, FilmDetailView, FilmUpdateView, FilmDeleteView, FilmListView

app_name = "film"
urlpatterns = [
    path("create/", FilmCreateView.as_view(), name="create"),
    path("<slug:slug>/", FilmDetailView.as_view(), name="detail"),
    path("update/<slug:slug>/", FilmUpdateView.as_view(), name="update"),
    path("delete/<slug:slug>/", FilmDeleteView.as_view(), name="delete"),
    path("", FilmListView.as_view(), name="list"),
]
