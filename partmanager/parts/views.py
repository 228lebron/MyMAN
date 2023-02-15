import openpyxl
from django.shortcuts import render, redirect, get_object_or_404
from django.core.cache import cache
from django.views import View
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.db.models import Q, F, QuerySet, Min, Subquery
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from .models import Request, Quota, Part, RequestQuotaResult
from .filters import ReqFilter, QuotaFilter, PartFilter, RequestFilter
from .forms import QuotaUploadForm, PartForm, RequestQuotaForm

def in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

#@user_passes_test(lambda u: in_group(u, 'product'))
#@login_required(login_url='/login/')
#def requests_and_quotas(request):
#    requests = Request.objects.all()
#    quotas = Quota.objects.all()
#    for req in requests:
#        match = False
#        for quo in quotas:
#            if (req.part.series == quo.part.series) and (abs((req.date - quo.date).days) <= 5):
#                if not RequestQuotaResult.objects.filter(request=req, quota=quo).exists():
#                    RequestQuotaResult.objects.update_or_create(request=req, quota=quo)
#                    RequestQuotaResult.objects.filter(request=req, quota=None).delete()
#                match = True
#        if not match:
#            if not RequestQuotaResult.objects.filter(request=req, quota=None).exists():
#                RequestQuotaResult.objects.create(request=req, quota=None)
#
#    result_qs = RequestQuotaResult.objects.all().order_by('request_id')
#
#    myFilter = ReqFilter(request.GET, queryset=result_qs)
#    result_qs = myFilter.qs
#
#    return render(request, 'requests_and_quotas.html', {'result': result_qs,'filter': myFilter})

def requests_and_quotas(request):
    result_qs = RequestQuotaResult.objects.all().order_by('request_id')
    myFilter = ReqFilter(request.GET, queryset=result_qs)
    result_qs = myFilter.qs

    return render(request, 'requests_and_quotas.html', {'result': result_qs,'filter': myFilter})




@login_required(login_url='login/')
def sale_manager_view(request):
    manager = request.user

    results = RequestQuotaResult.objects.filter(request__manager=manager).select_related('request', 'quota__part').order_by('quota__price')
    unique_results = []
    part_numbers = []

    for result in results:
        try:
            if result.quota.part.number not in part_numbers:
                unique_results.append(result)
                part_numbers.append(result.quota.part.number)
        except AttributeError:
            continue

    return render(request, 'manager_view.html', {'result': unique_results, 'manager': manager,})

def create_quotas_from_xlsx(file):
    wb = openpyxl.load_workbook(file)
    ws = wb.active

    quotas = []
    for row in ws.iter_rows(values_only=True):
        part_number, brand, quantity, price, datecode, supplier, date = row
        print(row)
        try:
            part = Part.objects.get(number=part_number, brand=brand)
            print('Нашел совпадение по Part')
        except Part.DoesNotExist:
            part = Part.objects.create(number=part_number, series=f"Введите серию {part_number[:6]}", brand=brand)
        quotas.append(Quota(part=part, quantity=quantity, price=price, datecode=datecode, supplier=supplier, date=date))

    Quota.objects.bulk_create(quotas)

@login_required(login_url='login/')
def upload_quotas(request):
    if request.method == 'POST':
        form = QuotaUploadForm(request.POST, request.FILES)
        if form.is_valid():
            create_quotas_from_xlsx(request.FILES['file'])
            return redirect('/quotas/')
    else:
        form = QuotaUploadForm()
    return render(request, 'quotas_upload.html', {'form': form})

@login_required(login_url='login/')
def quota_list(request):
    result_qs = Quota.objects.all().order_by('id')

    quotaFilter = QuotaFilter(request.GET, queryset=result_qs)
    result_qs = quotaFilter.qs

    return render(request, 'quotas_list.html', {'result': result_qs, 'filter': quotaFilter})

@login_required(login_url='login/')
def part_list(request):
    parts = Part.objects.all()
    partFilter = PartFilter(request.GET, queryset=parts)
    parts = partFilter.qs
    return render(request, 'parts/part_list.html', {'parts': parts, 'filter':partFilter,})

class PartDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'parts/part_detail.html'
    login_url = 'accounts/login/'

    def get(self, request, *args, **kwargs):
        part_id = kwargs.get('part_id')
        part = get_object_or_404(Part, pk=part_id)
        quotas = Quota.objects.filter(part=part)
        requests = Request.objects.filter(part=part)
        total_requests = requests.count()
        last_quota_date = quotas.last().date if quotas.exists() else None
        last_price = quotas.last().price if quotas.exists() else None
        return render(request, self.template_name, {'part': part, 'total_requests': total_requests,
                                                    'last_price': last_price, 'last_quota_date': last_quota_date})

class PartCreateView(CreateView, LoginRequiredMixin):
    model = Part
    fields = ['series', 'number', 'brand']
    template_name = 'parts/part_form.html'
    success_url = reverse_lazy('parts:part_list')

class RequestCreateView(CreateView, LoginRequiredMixin):
    model = Request
    fields = ['part', 'quantity', 'customer', 'date']
    template_name = 'requests/request_form.html'
    success_url = reverse_lazy('parts:request_list')

    def form_valid(self, form):
        form.instance.manager = self.request.user
        return super().form_valid(form)

@login_required(login_url='login/')
def request_list(request):
    manager = request.user
    requests = Request.objects.all()
    reqFilter = RequestFilter(request.GET, queryset=requests)
    requests = reqFilter.qs
    for i in requests:
        print(i.part.package_weight())
    return render(request, 'requests/request_list.html', {'requests': requests, 'filter':reqFilter, 'user': manager,})
class AttachQuotaToRequestView(UpdateView):
    model = Request
    fields = ['selected_quota', 'customer_price']
    template_name = 'attach_quota.html'
    success_url = reverse_lazy('parts:request_list')
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        request = self.get_object()
        creation_date_cutoff = timezone.now() - timezone.timedelta(days=5)
        form.fields['selected_quota'].queryset = Quota.objects.filter(part__series=request.part.series,
                                                                      date__gte=creation_date_cutoff,)
        return form
