import django_filters
from .models import *

class ReqFilter(django_filters.FilterSet):
    request__part__number = django_filters.CharFilter(lookup_expr='icontains', label='Part number')
    request__part__brand = django_filters.CharFilter(lookup_expr='icontains', label='Brand')
    request__customer = django_filters.CharFilter(lookup_expr='icontains', label='Клиент')
    request__date = django_filters.DateFromToRangeFilter(label='Date')

    class Meta:
        model = RequestQuotaResult
        fields = ['request__part__number', 'request__part__brand', 'request__date']

class QuotaFilter(django_filters.FilterSet):
    part__number = django_filters.CharFilter(lookup_expr='icontains', label='Part number')
    class Meta:
        model = Quota
        fields = ['part__number']

class PartFilter(django_filters.FilterSet):
    number = django_filters.CharFilter(lookup_expr='icontains', label='Part number')
    brand = django_filters.CharFilter(lookup_expr='icontains', label='Brand')
    class Meta:
        model = Part
        fields = ['number', 'brand']

class RequestFilter(django_filters.FilterSet):
    part__number = django_filters.CharFilter(lookup_expr='icontains', label='Part number')
    customer = django_filters.CharFilter(lookup_expr='icontains', label='Клиент')
    class Meta:
        model = Part
        fields = ['part__number', 'customer']