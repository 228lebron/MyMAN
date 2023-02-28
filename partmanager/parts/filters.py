from cProfile import label

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
    part__brand = django_filters.CharFilter(lookup_expr='icontains', label='Brand')
    date = django_filters.DateFromToRangeFilter(label='Date')
    class Meta:
        model = Quota
        fields = ['part__number', 'part__brand', 'date', 'supplier']

class PartFilter(django_filters.FilterSet):
    number = django_filters.CharFilter(lookup_expr='icontains', label='Part number')
    brand = django_filters.CharFilter(lookup_expr='icontains', label='Brand')
    class Meta:
        model = Part
        fields = ['number', 'brand']

class RequestFilter(django_filters.FilterSet):
    date = django_filters.DateFromToRangeFilter(label='Date')
    part__number = django_filters.CharFilter(lookup_expr='icontains', label='Part number')
    customer = django_filters.CharFilter(lookup_expr='icontains', label='Клиент')
    manager = django_filters.CharFilter(lookup_expr='icontains', label='Менеджер')
    class Meta:
        model = Part
        fields = ['part__number', 'customer', 'manager', 'date']