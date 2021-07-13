from django.test import TestCase
from django.urls import reverse

from film.models import Genre, Film


class FilmListViewTestCase(TestCase):

    def setUp(self):
        genre_1 = Genre.objects.create(genre="comedy")
        genre_2 = Genre.objects.create(genre="travel")
        Film.objects.create(film="Film 1", description="dsfsdfsefec", genre=genre_1)
        Film.objects.create(film="Film 2", description="sdfsdfwefd", genre=genre_2)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('film:list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('film:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'film/film.html')


class FilmDetailViewTestCase(TestCase):
    def setUp(self):
        genre_1 = Genre.objects.create(genre="comedy")
        Film.objects.create(film="Film 1", description="dsfsdfsefec", genre=genre_1)

    def test_view_uses_correct_template(self):
        resp = self.client.get("/film-1/")
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'film/film_card.html')
