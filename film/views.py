from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from film.forms import FilmDeleteForm
from film.models import Film


class FilmListView(ListView):
    """Film list view implementation"""

    http_method_names = ["get", "head", "options", "trace"]
    model = Film
    template_name = "film/film.html"


class FilmDetailView(DetailView):
    """Film detail view implementation"""

    http_method_names = ["get", "head", "options", "trace"]
    model = Film
    template_name = "film/film_card.html"


class FilmCreateView(CreateView):
    """Film create view implementation"""

    http_method_names = ["get", "post", "head", "options", "trace"]
    model = Film
    fields = [
        "genre",
        "pic",
        "film",
        "description",
    ]


class FilmUpdateView(UpdateView):
    """Film update view implementation"""

    http_method_names = ["get", "post", "head", "options", "trace", "patch", "put"]
    template_name = "film/film_form.html"
    model = Film
    fields = [
        "genre",
        "pic",
        "film",
        "description",
    ]


class FilmDeleteView(DeleteView):
    """Film delete view implementation"""

    http_method_names = ["get", "post", "head", "options", "trace"]
    model = Film
    template_name = 'film/film_confirm_delete.html'
    success_url = reverse_lazy("film:list")
