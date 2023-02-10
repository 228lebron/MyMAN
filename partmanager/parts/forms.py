from django import forms
import django_filters
from .models import Part
class PartNumberSearchForm(forms.Form):
    term = forms.CharField(label='Part Number', max_length=100)


class PartsFilter(django_filters.FilterSet):
    class Meta:
        model = Part
        fields = ['series', 'number', 'brand',]