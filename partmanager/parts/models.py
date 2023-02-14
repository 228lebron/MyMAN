from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import timezone, timedelta

PACKAGE_WEIGHTS = {
    'SOIC-8': 0.32,
    'SOIC-14': 0.55,
    'TO-92': 0.16,
    # add more
}

class Part(models.Model):
    series = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    case_type = models.CharField(max_length=50, null=True, default='Заполни корпус!')

    def __str__(self):
        return f'{self.number} ({self.brand}) ({self.series}) ({self.case_type})'
    def package_weight(self):
        return PACKAGE_WEIGHTS.get(self.case_type, 0)


class Quota(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=4)
    datecode = models.PositiveIntegerField()
    supplier = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f'{self.part.number} {self.part.brand} {self.quantity} {self.supplier} {self.date}'
    def rubble_price(self):
        if self is None:
            return 0
        part_weight = self.part.package_weight()
        ruble_price = float(self.price) * 1.3 * 1.2 * 70 + part_weight * 1000
        return round(ruble_price, 3)
class Request(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    customer = models.CharField(max_length=100)
    date = models.DateField()
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')

    selected_quota = models.ForeignKey(Quota, on_delete=models.SET_NULL, null=True, related_name='selected_quotas')
    customer_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    def __str__(self):
        return f'{self.part.number} - {self.quantity} - {self.customer}'


class RequestQuotaResult(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    quota = models.ForeignKey(Quota, on_delete=models.SET_NULL, null=True)



