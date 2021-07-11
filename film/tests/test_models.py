from django.test import TestCase

from film.models import Genre, Film


class GenreTestCase(TestCase):
    def setUp(self):
        Genre.objects.create(genre="travel")
        Genre.objects.create(genre="comedy")
        Genre.objects.create(genre="fantasy")

    def test_genre_count(self):
        """Genre count that were created correctly identified"""
        self.assertEqual(3, Genre.objects.count())

    def create_genre(self, genre="drama"):
        return Genre.objects.create(genre=genre)

    def test_genre_creation(self):
        genre = self.create_genre()
        self.assertTrue(isinstance(genre, Genre))
        self.assertEqual(genre.__str__(), genre.genre)


class FilmTestCase(TestCase):
    def setUp(self):
        genre_1 = Genre.objects.create(genre="comedy")
        genre_2 = Genre.objects.create(genre="travel")
        Film.objects.create(film="Film 1", description="dsfsdfsefec", genre=genre_1)
        Film.objects.create(film="Film 2", description="sdfsdfwefd", genre=genre_2)

    def test_film_count(self):
        """Film count that were created correctly identified"""
        self.assertEqual(2, Film.objects.count())

    def create_film(self):
        genre_3 = Genre.objects.create(genre="cosmos")
        return Film.objects.create(film="Film 3", description="dsfsdfsefec", genre=genre_3)

    def test_film_creation(self):
        film = self.create_film()
        self.assertTrue(isinstance(film, Film))
        self.assertEqual(film.__str__(), film.film)
