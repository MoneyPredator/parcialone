from django.db import models

# Create your models here.
'''
Liste todos los vuelos con los siguientes datos: id, nombre, tipo y precio
'''
class Flight(models.Model):
    f_type = [('Nacional'), ('Internacional'),]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    type = models.CharField(max_length=f_type)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name