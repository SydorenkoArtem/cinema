from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from api.permissions import UserPermission
from schedule.models import Hall, Schedule, Ticket
from schedule.serializers import HallSerializer, ScheduleSerializer, TicketSerializer


class HallListAPIView(ListCreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [UserPermission]


class HallRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [UserPermission]


class ScheduleListAPIView(ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [UserPermission]


class TicketListAPIView(ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [UserPermission]
