from django.contrib import admin
from django import forms
from .models import Part, Request, Quota, RequestQuotaResult

# Register your models here.
admin.site.register(Part)
admin.site.register(Request)
admin.site.register(RequestQuotaResult)

@admin.register(Quota)
class QuotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'part_number', 'brand', 'quantity', 'datecode', 'price', 'ruble_price',
                    'supplier', 'date')
    list_filter = ('supplier', 'date')
    search_fields = ('part__number', 'part__brand', 'supplier')
    ordering = ('-date',)

    def part_number(self, obj):
        return obj.part.number
    def brand(self, obj):
        return obj.part.brand
