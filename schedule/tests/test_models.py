from django.test import TestCase

from film.models import Film, Genre
from schedule.models import Hall, Schedule


class HallTestCase(TestCase):
    def setUp(self):
        Hall.objects.create(hall="hall 1", place="30")
        Hall.objects.create(hall="hall 2", place="40")
        Hall.objects.create(hall="hall 3", place="50")

    def test_hall_count(self):
        """Hall count that were created correctly identified"""
        self.assertEqual(3, Hall.objects.count())

    @staticmethod
    def create_hall(hall="hall 4", place="60"):
        return Hall.objects.create(hall=hall, place=place)

    def test_hall_creation(self):
        hall = self.create_hall()
        self.assertTrue(isinstance(hall, Hall))
        self.assertEqual(hall.__str__(), hall.hall)


class ScheduleTestCase(TestCase):
    def setUp(self):
        hall = Hall.objects.create(hall="Hall 6")
        genre = Genre.objects.create(genre="comedy")
        film = Film.objects.create(film="film 2", genre=genre)
        Schedule.objects.create(start_time="12:00:00", end_time="14:00:00", start_date="2021-07-10",
                                end_date="2021-07-15", date_show="2021-07-10", hall=hall, film=film, price="100.00")
        Schedule.objects.create(start_time="12:00:00", end_time="14:00:00", start_date="2021-07-10",
                                end_date="2021-07-15", date_show="2021-07-11", hall=hall, film=film, price="100.00")
        Schedule.objects.create(start_time="12:00:00", end_time="14:00:00", start_date="2021-07-10",
                                end_date="2021-07-15", date_show="2021-07-12", hall=hall, film=film, price="100.00")
        Schedule.objects.create(start_time="12:00:00", end_time="14:00:00", start_date="2021-07-10",
                                end_date="2021-07-15", date_show="2021-07-13", hall=hall, film=film, price="100.00")

    def test_schedule_count(self):
        """Schedule count that were created correctly identified"""
        self.assertEqual(4, Schedule.objects.count())

    def test_schedule_creation(self):
        hall = Hall.objects.create(hall="Hall 7")
        genre = Genre.objects.create(genre="genre 1")
        film = Film.objects.create(film="film 3", genre=genre)
        schedule = Schedule.objects.create(start_time="12:00:00", end_time="14:00:00", start_date="2021-07-10",
                                           end_date="2021-07-15", date_show="2021-07-14", hall=hall, film=film,
                                           price="100.00")
        self.assertTrue(isinstance(schedule, Schedule))
        self.assertEqual(schedule.__str__(), f"{schedule.film} {schedule.date_show} ({schedule.start_time})")
