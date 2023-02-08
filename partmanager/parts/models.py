from django.db import models
from django.utils.timezone import timezone, timedelta

class Part(models.Model):
    series = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return f'БРЕНД: {self.brand} СЕРИЯ: {self.series} НОМЕР:{self.number}'

class Request(models.Model):
    part_number = models.ForeignKey(Part, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    date = models.DateField()
    def __str__(self):
        return f'{self.part_number.number} {self.brand} {self.quantity}'

class Quota(models.Model):
    part_number = models.ForeignKey(Part, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.CharField(max_length=100)
    date = models.DateField()