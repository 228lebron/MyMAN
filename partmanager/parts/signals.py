from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import *
import datetime

@receiver(post_save, sender=Request)
def create_request_quota_result(sender, instance, **kwargs):
    if kwargs['created']:
        RequestQuotaResult.objects.update_or_create(request=instance, quota=None)
        for quo in Quota.objects.all():
            instance_date = instance.date.date() if isinstance(instance.date, datetime.datetime) else instance.date
            quo_date = quo.date.date() if isinstance(quo.date, datetime.datetime) else quo.date
            if (instance.part.series == quo.part.series) and (abs((instance_date - quo_date).days) <= 5):
                if not RequestQuotaResult.objects.filter(request=instance, quota=quo).exists():
                    RequestQuotaResult.objects.update_or_create(request=instance, quota=quo)
                    RequestQuotaResult.objects.filter(request=instance, quota=None).delete()

@receiver(post_save, sender=Quota)
def create_quota_request_result(sender, instance, **kwargs):
    if kwargs['created']:
        for req in Request.objects.all():
            instance_date = instance.date.date() if isinstance(instance.date, datetime.datetime) else instance.date
            req_date = req.date.date() if isinstance(req.date, datetime.datetime) else req.date
            if (instance.part.series == req.part.series) and (abs((req_date - instance_date).days) <= 5):
                if not RequestQuotaResult.objects.filter(request=req, quota=instance).exists():
                    RequestQuotaResult.objects.update_or_create(request=req, quota=instance)
                    RequestQuotaResult.objects.filter(request=req, quota=None).delete()
