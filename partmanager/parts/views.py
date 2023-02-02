from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Part, Request, Quote, Order


class PartDetailView(DetailView):
    model = Part
    template_name = 'part_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quotes'] = Quote.objects.filter(part=self.object)
        return context

class PartListView(LoginRequiredMixin, ListView):
    model = Part
    template_name = 'part_list.html'
    context_object_name = 'parts'

class PartCreateView(LoginRequiredMixin, CreateView):
    model = Part
    template_name = 'part_form.html'
    fields = ['number', 'series', 'manufacturer', 'digikey_link', 'manufacturer_link']
    success_url = reverse_lazy('parts:part_list')

class PartUpdateView(LoginRequiredMixin, UpdateView):
    model = Part
    template_name = 'part_form.html'
    fields = ['number', 'series', 'manufacturer', 'digikey_link', 'manufacturer_link']
    success_url = reverse_lazy('part_list')

class PartDeleteView(LoginRequiredMixin, DeleteView):
    model = Part
    template_name = 'part_confirm_delete.html'
    success_url = reverse_lazy('parts:part_list')

class RequestListView(LoginRequiredMixin, ListView):
    model = Request
    template_name = 'request_list.html'
    context_object_name = 'requests'

class RequestDetailView(DetailView):
    model = Request
    template_name = 'request_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sale_rubles_price'] = self.object.sale_rubles_price
        return context

class RequestCreateView(LoginRequiredMixin, CreateView):
    model = Request
    template_name = 'request_form.html'
    fields = ['part', 'quantity', 'reason']
    success_url = reverse_lazy('parts:request_list')

class RequestUpdateView(LoginRequiredMixin, UpdateView):
    model = Request
    template_name = 'request_form.html'
    fields = ['part', 'quantity', 'reason']
    success_url = reverse_lazy('parts:request_list')

class RequestDeleteView(LoginRequiredMixin, DeleteView):
    model = Request
    template_name = 'request_confirm_delete.html'
    success_url = reverse_lazy('parts:request_list')

class QuoteListView(LoginRequiredMixin, ListView):
    model = Quote
    template_name = 'quote_list.html'
    context_object_name = 'quotes'

class QuoteCreateView(LoginRequiredMixin, CreateView):
    model = Quote
    template_name = 'quote_form.html'
    fields = ['part', 'supplier', 'price']
    success_url = reverse_lazy('parts:quote_list')

class QuoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Quote
    template_name = 'quote_form.html'
    fields = ['part', 'supplier', 'price']
    success_url = reverse_lazy('parts:quote_list')

class OrderListView(ListView):
    model = Order
    template_name = "order_list.html"
    context_object_name = "orders"

class OrderCreateView(CreateView):
    model = Order
    template_name = "order_form.html"
    fields = ["part", "quantity", "price", "supplier"]
    success_url = reverse_lazy("parts:order_list")

class OrderUpdateView(UpdateView):
    model = Order
    template_name = "order_form.html"
    fields = ["part", "quantity", "price", "supplier"]
    success_url = reverse_lazy("parts:order_list")