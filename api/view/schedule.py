from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from schedule.models import Hall, Schedule, Ticket
from schedule.serializers import HallSerializer, ScheduleSerializer, TicketSerializer


class HallListAPIView(ListCreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer


class HallRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer


class ScheduleListAPIView(ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class TicketListAPIView(ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
