from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import timezone, timedelta


class Part(models.Model):
    series = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.number} ({self.brand}) ({self.series})'

class Request(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    customer = models.CharField(max_length=100)
    date = models.DateField()
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')

    def __str__(self):
        return f'{self.part.number} - {self.quantity} - {self.customer}'

class Quota(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=4)
    datecode = models.PositiveIntegerField()
    supplier = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f'{self.part.number} {self.part.brand} {self.quantity}'


class RequestQuotaResult(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    quota = models.ForeignKey(Quota, on_delete=models.SET_NULL, null=True)
    def rubble_price(self):
        if self.quota is None:
            return 0
        return round(float(self.quota.price) * 1.3 * 1.2 * 70, 3)

