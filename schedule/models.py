from django.db import models
from django.urls import reverse_lazy

from film.models import Film


class Hall(models.Model):
    """Hall model implementation"""

    hall = models.CharField(max_length=255)
    place = models.IntegerField(default=60)

    def __str__(self):
        return self.hall


class Schedule(models.Model):
    """Schedule model implementation"""

    start_time = models.TimeField()
    end_time = models.TimeField()
    start_date = models.DateField()
    end_date = models.DateField()
    date_show = models.DateField()
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __repr__(self):
        """Return a string representation of an instance"""

        return f"<Schedule ({self.id})>"

    def __str__(self):
        """Return a string version of an instance"""

        return f"{self.date_show} ({self.start_time})"


class Ticket(models.Model):
    """Ticket model implementation"""

    quantity = models.PositiveIntegerField()
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    customer = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def get_total(self):
        """Get total for ticket"""

        total = self.schedule.price * self.quantity
        return total

    @property
    def get_absolute_url(self):
        return reverse_lazy("film:list")

    def save(self, *args, **kwargs):
        """Save total in ticket and save profile after minus total ticket"""
        self.customer.profile.balance -= self.get_total()
        self.customer.profile.save()
        self.total = self.get_total()

        super(Ticket, self).save(*args, **kwargs)

