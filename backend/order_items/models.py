from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class OrderItems(models.Model):
    name = models.CharField('Название позиции', max_length=255)
    price = models.FloatField(validators=[MinValueValidator(1)])
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    order = models.ForeignKey(to='orders.Orders', on_delete=models.CASCADE)

    class Meta:
        db_table = "order_items"
