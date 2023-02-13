from django import forms
from .models import Part


class QuotaUploadForm(forms.Form):
    file = forms.FileField()

class PartForm(forms.Form):
    class Meta:
        model = Part
        fields = ['series', 'number', 'brand']