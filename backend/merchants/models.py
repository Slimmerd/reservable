from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Merchants(models.Model):
    name = models.CharField("Название мерчанта", max_length=255)
    percent = models.FloatField(validators=[MaxValueValidator(100)])
    reservation_cost = models.FloatField(validators=[MinValueValidator(0)])
    owner = models.ForeignKey(to='user.User')

    class Meta:
        db_table = 'merchants'
