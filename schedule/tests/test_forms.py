import datetime

from django.test import TestCase

from film.models import Film, Genre
from schedule.forms import ScheduleForm, HallForm, TicketForm
from schedule.models import Hall, Schedule


class ScheduleFormTest(TestCase):

    def test_schedule_form_date_in_past(self):
        hall = Hall.objects.create(hall="Hall 7")
        genre = Genre.objects.create(genre="comedy")
        film = Film.objects.create(film="Film3", genre=genre)
        date = datetime.date.today() - datetime.timedelta(days=1)
        end_date = datetime.date.today()
        form_data = {'start_date': date,
                     'end_date': end_date,
                     'start_time': '13:00:00',
                     'end_time': '15:00:00',
                     'hall': hall
                     }
        form = ScheduleForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_schedule_form_start_date_more_then_end_date(self):
        hall = Hall.objects.create(hall="Hall 8")
        genre = Genre.objects.create(genre="comedy")
        film = Film.objects.create(film="Film4", genre=genre)
        start_date = datetime.date.today() + datetime.timedelta(days=4)
        end_date = datetime.date.today() + datetime.timedelta(days=3)
        date_show = start_date
        form_data = {'start_date': start_date,
                     'end_date': end_date,
                     'start_time': '13:00:00',
                     'end_time': '15:00:00',
                     'hall': hall,
                     'date_show': date_show,
                     'film': film,
                     'price': '100.00',
                     }
        form = ScheduleForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_schedule_form_is_valid(self):
        hall = Hall.objects.create(hall="Hall 9")
        genre = Genre.objects.create(genre="comedy")
        film = Film.objects.create(film="Film2", genre=genre)
        start_date = datetime.date.today()
        end_date = datetime.date.today() + datetime.timedelta(days=3)
        date_show = start_date
        form_data = {'start_date': start_date,
                     'end_date': end_date,
                     'start_time': '13:00:00',
                     'end_time': '15:00:00',
                     'date_show': date_show,
                     'hall': hall,
                     'film': film,
                     'price': '100.00',
                     }
        form = ScheduleForm(data=form_data)
        self.assertTrue(form.is_valid())


class HallFormTest(TestCase):

    def test_hall_form_is_valid(self):
        form_data = {
                     'hall': 'Hall 2',
                     'place': '50',
                     }
        form = HallForm(data=form_data)
        self.assertTrue(form.is_valid())


class TicketFormTest(TestCase):

    def test_ticket_form_is_valid(self):
        hall = Hall.objects.create(hall="Hall 10", place='50')
        genre = Genre.objects.create(genre="genre 1")
        film = Film.objects.create(film="film 3", genre=genre)
        schedule = Schedule.objects.create(start_time="12:00:00", end_time="14:00:00", start_date="2021-07-10",
                                           end_date="2021-07-15", date_show="2021-07-14", hall=hall, film=film,
                                           price="100.00")
        form_data = {
            'quantity': '3',
            'schedule': schedule,
        }
        form = TicketForm(data=form_data)
        self.assertTrue(form.is_valid())

# def test_invalid_form(self):
#     w = Whatever.objects.create(title='Foo', body='')
#     data = {'title': w.title, 'body': w.body,}
#     form = WhateverForm(data=data)
#     self.assertFalse(form.is_valid())
#
#     class EntryResourceTest(ResourceTestCase):
#
#         def test_get_api_json(self):
#             resp = self.api_client.get('/api/whatever/', format='json')
#             self.assertValidJSONResponse(resp)
#
#         def test_get_api_xml(self):
#             resp = self.api_client.get('/api/whatever/', format='xml')
#             self.assertValidXMLResponse(resp)

