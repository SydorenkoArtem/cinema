from django.urls import path

from api.view.schedule import HallListAPIView, HallRetrieveUpdateAPIView, ScheduleListAPIView, TicketCreateAPIView, \
    ScheduleUserListAPIView

app_name = "api"

urlpatterns = [
    path("hall/", HallListAPIView.as_view(), name="list"),
    path("hall/<int:pk>/", HallRetrieveUpdateAPIView.as_view(), name="detail"),
    path("", ScheduleUserListAPIView.as_view(), name="schedule"),
    path("create/", ScheduleListAPIView.as_view(), name="create"),
    path("ticket/", TicketCreateAPIView.as_view(), name="ticket"),
]
