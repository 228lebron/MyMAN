import django_filters
from .models import *

class ReqFilter(django_filters.FilterSet):
    request__part_number__number = django_filters.CharFilter(lookup_expr='icontains', label='Part number')
    request__brand = django_filters.CharFilter(lookup_expr='icontains', label='Brand')
    request__date = django_filters.DateFilter(label='Date')

    class Meta:
        model = RequestQuotaResult
        fields = ['request', 'quota', 'request__part_number__number', 'request__brand', 'request__date']