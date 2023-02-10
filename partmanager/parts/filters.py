import django_filters
from .models import *

class ReqFilter(django_filters.FilterSet):
    part_number__number = django_filters.CharFilter(lookup_expr='icontains', label='Part number')
    brand = django_filters.CharFilter(lookup_expr='icontains', label='Brand')
    date = django_filters.DateFilter(label='Date')

    class Meta:
        model = RequestQuotaResult
        fields = ['request', 'quota', 'part_number__number', 'brand', 'date']