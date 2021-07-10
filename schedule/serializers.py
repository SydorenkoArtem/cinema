from rest_framework import serializers

from schedule.models import Hall, Schedule, Ticket


class HallSerializer(serializers.ModelSerializer):
    """Hall Serializer implementation"""
    class Meta:
        model = Hall
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    """Schedule Serializer implementation"""

    class Meta:
        model = Schedule
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    """Ticket Serializer implementation"""

    class Meta:
        model = Ticket
        fields = '__all__'
