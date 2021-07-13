import datetime

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.permissions import UserStaffPermission, UserAPIPermission
from schedule.models import Hall, Schedule
from schedule.serializers import HallSerializer, ScheduleSerializer, TicketSerializer


class HallListAPIView(ListCreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [UserStaffPermission]


class HallRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [UserStaffPermission]


class ScheduleListAPIView(ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [UserStaffPermission]


class ScheduleUserListAPIView(ListAPIView):
    queryset = Schedule.objects.filter(date_show=datetime.datetime.today())
    serializer_class = ScheduleSerializer
    permission_classes = [UserAPIPermission]


class TicketCreateAPIView(CreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [UserAPIPermission, IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
