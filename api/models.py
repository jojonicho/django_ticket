from django.db import models
# from .utils import generate_time
from django.utils.timezone import now

class Item(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.SmallIntegerField()
    created_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name
    objects = models.Manager()