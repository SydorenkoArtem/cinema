from django.urls import path

from schedule.views import ScheduleListView, TicketCreateView

app_name = "schedule"
urlpatterns = [
    path('list/', ScheduleListView.as_view(), name='list'),
    path('ticket/', TicketCreateView.as_view(), name='ticket')
]
