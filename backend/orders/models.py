from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from django.utils import timezone


class Orders(models.Model):
    is_reservation = models.BooleanField(default=False)
    reserved_date = models.DateTimeField()
    persons = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    percent = models.IntegerField(validators=[MaxValueValidator(100)])
    reservation_cost = models.FloatField()
    total = models.FloatField()
    total_after_percent = models.FloatField()

    comment = models.CharField(blank=True, max_length=512)
    created_at = models.DateTimeField(default=timezone.now())

    merchant = models.ForeignKey(to='merchants.Merchants', on_delete=models.CASCADE)
    client = models.ForeignKey(to='clients.Client', on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'
