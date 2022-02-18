from django.db import models


# Create your models here.
class Clients(models.Model):
    name = models.CharField('Имя', max_length=255)
    email = models.EmailField()
    phone = models.CharField('Телефон', max_length=11)
    orders = models.ForeignKey(to='orders.Orders', on_delete=models.CASCADE)

    class Meta:
        db_table = "clients"
