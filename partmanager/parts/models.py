from django.db import models
from django.utils.timezone import timezone, timedelta


class RequestQuotaQuerySet(models.QuerySet):
    def matching_quotas(self):
        requests = self.filter(part_number__series__isnull=False)
        quotas = Quota.objects.all()
        matching_quotas = []
        #result = []
        for req in requests:
            match = False
            for quo in quotas:
                if (req.part_number.series == quo.part_number.series) and (abs((req.date - quo.date).days) <= 2):
                    matching_quotas.append((req, quo))
            #if not match:
            #    #matching_quotas.append({'request': req, 'quota': None})
            #    matching_quotas.append((req, None))
        return matching_quotas

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

    objects = RequestQuotaQuerySet.as_manager()
    def __str__(self):
        return f'{self.part_number.number} {self.brand} {self.quantity}'

class Quota(models.Model):
    part_number = models.ForeignKey(Part, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.CharField(max_length=100)
    date = models.DateField()
    def __str__(self):
        return f'{self.part_number.number} {self.brand} {self.quantity}'

class RequestQuotaResult(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    quota = models.ForeignKey(Quota, on_delete=models.SET_NULL, null=True)