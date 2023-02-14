from django import forms
from .models import *


class QuotaUploadForm(forms.Form):
    file = forms.FileField()

class PartForm(forms.Form):
    class Meta:
        model = Part
        fields = ['series', 'number', 'brand']


class RequestQuotaForm(forms.ModelForm):
    selected_quota = forms.ModelChoiceField(
        queryset=Quota.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None,
    )
    class Meta:
        model = Request
        fields = ['selected_quota']