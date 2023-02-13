from django.contrib import admin
from .models import Part, Request, Quota, RequestQuotaResult

# Register your models here.
admin.site.register(Part)
admin.site.register(Request)
admin.site.register(Quota)
admin.site.register(RequestQuotaResult)
