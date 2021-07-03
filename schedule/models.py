from django.db import models

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
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __repr__(self):
        """Return a string representation of an instance"""

        return f"<Schedule ({self.id})>"

    def __str__(self):
        """Return a string version of an instance"""

        return f"{self.start_date} ({self.start_time})"


class Ticket(models.Model):
    """Ticket model implementation"""

    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    customer = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        price = Schedule.objects.get(schedule=self.schedule).price
        self.total = self.quantity * price
        self.customer.profile.balance -= self.total()
        self.customer.profile.save()

        super(Ticket, self).save(*args, **kwargs)

