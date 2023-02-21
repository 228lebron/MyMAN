import django_tables2 as tables
from .models import Part, Request, Quota, RequestQuotaResult
from django.urls import reverse
from django.utils.safestring import mark_safe


class PartTable(tables.Table):
    edit_button = tables.TemplateColumn(
        '<a href="{% url "parts:part_edit" record.id %}" class="btn btn-outline-dark btn-sm">Edit</a>',
        verbose_name='',
        orderable=False)

    class Meta:
        model = Part
        fields = ('id', 'series', 'number', 'brand', 'case_type')
        attrs = {'class': 'table table-hover table table-bordered',}
        row_attrs = {
            'style': 'text-align:center;'
        }

    def render_number(self, value, record):
        url = reverse('parts:part_detail', args=[record.id])
        return mark_safe('<a href="{}">{}</a>'.format(url, value))


class RequestTable(tables.Table):
    customer_price_with_currency = tables.TemplateColumn('{{ record.customer_price }} {{ record.currency }}',
                                                         verbose_name='Цена клиенту')
    edit_button = tables.TemplateColumn(
        '<a href="{% url "parts:attach_quota" record.id %}" class="btn btn-outline-success btn-sm">+</a>',
        verbose_name='',
        orderable=False)
    class Meta:
        model = Request
        fields = ('part.number', 'part.brand', 'customer', 'date', 'manager', 'selected_quota.part.number',
                  'selected_quota.part.brand', 'selected_quota.date')
        attrs = {'class': 'table table-hover table table-bordered', }
        row_attrs = {
            'style': 'text-align:center;'
        }


class RequestQuotaTable(tables.Table):
    quota_number = tables.Column(verbose_name='Номер квоты', accessor='quota.part.number')
    quota_brand = tables.Column(verbose_name='Бренд квоты', accessor='quota.part.brand')
    class Meta:
        model = RequestQuotaResult
        fields = ('request.id', 'request.part.number', 'request.part.brand', 'request.quantity', 'request.customer',
                  'request.date', 'request.manager', 'quota_number', 'quota_brand', 'quota.quantity',
                  'quota.price', 'quota.ruble_price', 'ruble_sea_price', 'ruble_air_price', 'quota.datecode',
                  'quota.lead_time', 'quota.supplier', 'quota.date')
        attrs = {'class': 'table table-hover table table-bordered table table-sm', }
        row_attrs = {
            'style': 'text-align:center;'
        }

