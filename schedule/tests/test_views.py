import datetime

from django.test import TestCase
from django.urls import reverse

from film.models import Film, Genre
from schedule.models import Hall, Schedule


class ScheduleListViewTestCase(TestCase):

    def setUp(self):
        hall = Hall.objects.create(hall="Hall 6")
        genre = Genre.objects.create(genre="comedy")
        film = Film.objects.create(film="film 2", genre=genre)
        start_date = datetime.datetime.today()
        end_date = datetime.datetime.today() + datetime.timedelta(days=5)
        date_show = start_date
        Schedule.objects.create(start_time="12:00:00", end_time="14:00:00", start_date=start_date,
                                end_date=end_date, date_show=date_show, hall=hall, film=film, price="100.00")

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('schedule:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'schedule/schedule_list.html')
