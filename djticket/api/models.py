from django.db import models
from .utils import generate_time
from django.utils.timezone import now
# Create your models her


class Movie(models.Model):
    name = models.CharField(max_length=40)
    desc = models.TextField()
    play_date_time = models.DateTimeField()
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name
    objects = models.Manager()


class Seat(models.Model):
    movie_id = models.SmallIntegerField(default=0)
    seat_num = models.CharField(max_length=3)

    def __str__(self):
        return self.seat_num
    objects = models.Manager()


class Order(models.Model):
    seat_id = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.seat_id
    objects = models.Manager()
