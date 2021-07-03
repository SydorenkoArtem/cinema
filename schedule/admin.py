from django.contrib import admin

from schedule.models import Hall, Schedule


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    """Hall admin implementation"""

    fields = [
        "hall",
        "place",
    ]


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    """Schedule admin implementation"""

    fields = [
        "start_time",
        "end_time",
        "hall",
        "price",
        "film",
        "start_date",
        "end_date",
    ]
