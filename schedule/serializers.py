from rest_framework import serializers

from schedule.models import Hall, Schedule, Ticket
from schedule.services import get_free_places_in_hall


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

    def validate(self, data):
        """Check that start date is before end date"""
        all_schedule = Schedule.objects.filter(hall=data["hall"])
        for schedule in all_schedule:
            if schedule.start_time <= data["start_time"] <= schedule.end_time and \
                    schedule.start_date <= data["start_date"] <= schedule.end_date or \
                    schedule.start_time <= data["end_time"] <= schedule.end_time and \
                    schedule.start_date <= data["end_date"] <= schedule.end_date:
                raise serializers.ValidationError("This schedule book yet. Choose other time and date")
        if data["start_date"] > data["end_date"]:
            raise serializers.ValidationError("End Date must occur after start date")
        if data["start_time"] > data["end_time"]:
            raise serializers.ValidationError("End time must occur after start time")
        if data["price"] <= 0:
            raise serializers.ValidationError("Enter a price more then 0")
        return data


class TicketSerializer(serializers.ModelSerializer):
    """Ticket Serializer implementation"""

    class Meta:
        model = Ticket
        exclude = ['total', 'customer']

    def validate(self, data):
        """Check that quantity more than 0"""
        free_places = get_free_places_in_hall(data["schedule"])

        if data["quantity"] > free_places:
            raise serializers.ValidationError(f"This quantity is not in stock {free_places}")
        if data["quantity"] <= 0:
            raise serializers.ValidationError("You have selected the wrong number of tickets. Enter a quantity from 1")
        return data
