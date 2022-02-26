from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=512)
    price = models.FloatField(validators=[MinValueValidator(1)])
    merchant = models.ForeignKey(to='merchants.Merchants', on_delete=models.CASCADE)

    class Meta:
        db_table = "products"
