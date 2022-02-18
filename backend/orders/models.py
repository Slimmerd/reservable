from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Orders(models.Model):
    is_reservation = models.BooleanField(default=False)
    reserved_date = models.DateTimeField()
    persons = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    reservation_cost = models.FloatField()
    percent = models.IntegerField(validators=[MaxValueValidator(100)])
    total = models.FloatField()
    total_after_percent = models.FloatField()
    order_items = models.ForeignKey(to='order_items.OrderItems', on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'
