from django.shortcuts import render
from django.db.models import Q
from .models import Request, Quota
import datetime

#def requests_and_quotas(request):
#    requests = Request.objects.all()
#    quotas = Quota.objects.all()
#    results = []
#    for req in requests:
#        for quo in quotas:
#            if (req.part_number.series == quo.part_number.series) and (abs((req.date - quo.date).days) <= 2):
#                results.append((req, quo))
#    return render(request, 'requests_and_quotas.html', {'results': results})


def requests_and_quotas(request):
    requests = Request.objects.all()
    quotas = Quota.objects.all()
    results = []
    for req in requests:
        match = False
        for quo in quotas:
            if (req.part_number.series == quo.part_number.series) and (abs((req.date - quo.date).days) <= 2):
                results.append((req, quo))
                match = True
                #break
        if not match:
            results.append((req, None))
    return render(request, 'requests_and_quotas.html', {'results': results})