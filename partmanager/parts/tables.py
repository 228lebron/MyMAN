import django_tables2 as tables
from .models import Part, Request, Quota


class RequestsAndQuotasTable(tables.Table):
    request_part_number = tables.Column(accessor='request.part_number.number')
    request_brand = tables.Column(accessor='request.brand')
    request_quantity = tables.Column(accessor='request.quantity')
    request_date = tables.Column(accessor='request.date')
    quota_part_number = tables.Column(accessor='quota.part_number.number')
    quota_brand = tables.Column(accessor='quota.brand')
    quota_quantity = tables.Column(accessor='quota.quantity')
    quota_price = tables.Column(accessor='quota.price')
    quota_supplier = tables.Column(accessor='quota.supplier')
    quota_date = tables.Column(accessor='quota.date')

    class Meta:
        model = Request
        template_name = 'django_tables2/bootstrap4.html'
        fields = (
            'request_part_number',
            'request_brand',
            'request_quantity',
            'request_date',
            'quota_part_number',
            'quota_brand',
            'quota_quantity',
            'quota_price',
            'quota_supplier',
            'quota_date'
        )