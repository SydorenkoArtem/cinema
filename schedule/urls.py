from django.urls import path

from schedule.views import ScheduleListView, TicketCreateView, ScheduleCreateView, HallCreateView, TicketUserView, \
    ScheduleDeleteView

app_name = "schedule"
urlpatterns = [
    path('list/', ScheduleListView.as_view(), name='list'),
    path('ticket/', TicketCreateView.as_view(), name='ticket'),
    path('create/', ScheduleCreateView.as_view(), name='create'),
    path('create/hall/', HallCreateView.as_view(), name='hall'),
    path('mytickets/', TicketUserView.as_view(), name='my_tickets'),
    path('delete/<int:pk>/', ScheduleDeleteView.as_view(), name='delete'),
]
