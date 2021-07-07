from django.urls import path

from api.view.schedule import HallListAPIView, HallRetrieveUpdateAPIView, ScheduleListAPIView, TicketListAPIView

app_name = "api"

urlpatterns = [
    path("hall/", HallListAPIView.as_view(), name="list"),
    path("hall/<int:pk>/", HallRetrieveUpdateAPIView.as_view(), name="detail"),
    path("", ScheduleListAPIView.as_view(), name="schedule"),
    path("ticket/", TicketListAPIView.as_view(), name="ticket"),
]
