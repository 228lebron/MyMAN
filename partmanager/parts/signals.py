from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=Request)
def create_request_quota_result(sender, instance, **kwargs):
    if kwargs['created']:
        RequestQuotaResult.objects.update_or_create(request=instance, quota=None)
        for quo in Quota.objects.all():
            if (instance.part.series == quo.part.series) and (abs((instance.date - quo.date).days) <= 5):
                if not RequestQuotaResult.objects.filter(request=instance, quota=quo).exists():
                    RequestQuotaResult.objects.update_or_create(request=instance, quota=quo)
                    RequestQuotaResult.objects.filter(request=instance, quota=None).delete()

@receiver(post_save, sender=Quota)
def create_quota_request_result(sender, instance, **kwargs):
    if kwargs['created']:
        for req in Request.objects.all():
            if (instance.part.series == req.part.series) and (abs((req.date - instance.date).days) <= 5):
                if not RequestQuotaResult.objects.filter(request=req, quota=instance).exists():
                    RequestQuotaResult.objects.update_or_create(request=req, quota=instance)
                    RequestQuotaResult.objects.filter(request=req, quota=None).delete()

#@receiver(post_save, sender=Request)
#def update_request_status(sender, instance, **kwargs):
#    if instance.selected_quota and instance.status != 'PAID':
#        instance.status = 'QUOTA'
#        instance.save()