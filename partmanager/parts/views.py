from django.shortcuts import render
from django.core.cache import cache
from django.db.models import Q, F, QuerySet
from .models import Request, Quota, Part, RequestQuotaResult
from .forms import PartNumberSearchForm
from .tables import RequestsAndQuotasTable
from .filters import ReqFilter
from datetime import datetime, timedelta
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django_tables2 import RequestConfig
from django_filters.views import FilterView
from django.utils import timezone


#def requests_and_quotas(request):
#    requests = Request.objects.all()
#    quotas = Quota.objects.all()
#    results = []
#    for req in requests:
#        for quo in quotas:
#            if (req.part_number.series == quo.part_number.series) and (abs((req.date - quo.date).days) <= 2):
#                results.append((req, quo))
#    return render(request, 'requests_and_quotas.html', {'results': results})


#def requests_and_quotas(request):
#    requests = Request.objects.all()
#    quotas = Quota.objects.all()
#    parts = Part.objects.all()
#    results = []
#    for req in requests:
#        match = False
#        for quo in quotas:
#            if (req.part_number.series == quo.part_number.series) and (abs((req.date - quo.date).days) <= 2):
#                results.append((req, quo))
#                match = True
#                #break
#        if not match:
#            results.append((req, None))
#    return render(request, 'requests_and_quotas.html', {'results': results, 'parts': parts, })

#def requests_and_quotas(request):
#    result_qs = cache.get('result_qs')
#    if not result_qs:
#        requests = Request.objects.all()
#        quotas = Quota.objects.all()
#        for req in requests:
#            match = False
#            for quo in quotas:
#                if (req.part_number.series == quo.part_number.series) and (abs((req.date - quo.date).days) <= 2):
#                    RequestQuotaResult.objects.create(request=req, quota=quo)
#                    match = True
#                    #break
#            if not match:
#                RequestQuotaResult.objects.create(request=req, quota=None)
#        result_qs = RequestQuotaResult.objects.all()
#        cache.set('result_qs', result_qs)
#
#    myFilter = ReqFilter(request.GET, queryset=result_qs)
#    result_qs = myFilter.qs
#
#    return render(request, 'requests_and_quotas.html', {'result': result_qs, 'filter': myFilter, })


def requests_and_quotas(request):
    requests = Request.objects.all()
    quotas = Quota.objects.all()
    for req in requests:
        match = False
        for quo in quotas:
            if (req.part_number.series == quo.part_number.series) and (abs((req.date - quo.date).days) <= 2):
                if not RequestQuotaResult.objects.filter(request=req, quota=quo).exists():
                    RequestQuotaResult.objects.create(request=req, quota=quo)
                match = True
                #break
        if not match:
            if not RequestQuotaResult.objects.filter(request=req, quota=None).exists():
                RequestQuotaResult.objects.create(request=req, quota=None)

    #result_qs = RequestQuotaResult.objects.all()
    result_qs = RequestQuotaResult.objects.all().order_by('request__part_number__number')

    myFilter = ReqFilter(request.GET, queryset=result_qs)
    result_qs = myFilter.qs

    return render(request, 'requests_and_quotas.html', {'result': result_qs,'filter': myFilter})


#def requests_and_quotas(request):
#    matching_quotas = Request.objects.matching_quotas()
#    print(matching_quotas)
#    print(type(matching_quotas))
#    return render(request, 'requests_and_quotas.html', {'result': matching_quotas,})