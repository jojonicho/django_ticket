from django.db import models
from .utils import generate_time
from django.utils.timezone import now
# Create your models her


class Movie(models.Model):
    name = models.CharField(max_length=40)
    desc = models.TextField()
    play_date_time = models.DateField()

    def __str__(self):
        return self.name
    objects = models.Manager()


class Seat(models.Model):
    # movie_id = models.SmallIntegerField(default=0)
    seat_num = models.CharField(max_length=3)
    movie = models.ForeignKey(
        Movie, null=True, blank=True, related_name='seats', on_delete=models.CASCADE)
    # movie = models.ManyToManyField(Movie, related_name='Movies')

    class Meta:
        ordering = ('seat_num',)
        verbose_name_plural = 'Seats'

    def __str__(self):
        return self.seat_num
    objects = models.Manager()


class Order(models.Model):
    # seat_id = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(default=now, editable=False)
    seat = models.ForeignKey(
        Seat, null=True, blank=True, related_name='orders', on_delete=models.CASCADE)
    # seat = models.ManyToManyField(Seat, related_name='Seats')

    class Meta:
        ordering = ('created_at',)
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.created_at
    objects = models.Manager()
