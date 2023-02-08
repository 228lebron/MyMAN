from django.urls import path
from . import views


app_name = 'parts'

urlpatterns = [
    path('quotas_on_req/', views.requests_and_quotas, name='requests_and_quotas')
    #path('part/<int:pk>/', views.PartDetailView.as_view(), name='part_detail'),
    #path('part/list/', views.PartListView.as_view(), name='part_list'),
    #path('part/create/', views.PartCreateView.as_view(), name='part_create'),
    #path('part/update/<int:pk>/', views.PartUpdateView.as_view(), name='part_update'),
    #path('part/delete/<int:pk>/', views.PartDeleteView.as_view(), name='part_delete'),
    #path('request/list/', views.RequestListView.as_view(), name='request_list'),
    #path('request/create/', views.RequestCreateView.as_view(), name='request_create'),
    #path('request/update/<int:pk>/', views.RequestUpdateView.as_view(), name='request_update'),
    #path('request/delete/<int:pk>/', views.RequestDeleteView.as_view(), name='request_delete'),
    #path('quote/list/', views.QuoteListView.as_view(), name='quote_list'),
    #path('quote/create/', views.QuoteCreateView.as_view(), name='quote_create'),
    #path('quote/update/<int:pk>/', views.QuoteUpdateView.as_view(), name='quote_update'),
    ##path('quote/delete/<int:pk>/', views.QuoteDeleteView.as_view(), name='quote_delete'),
    #path('order/list/', views.OrderListView.as_view(), name='order_list'),
    #path('order/create/', views.OrderCreateView.as_view(), name='order_create'),
    #path('order/update/<int:pk>/', views.OrderUpdateView.as_view(), name='order_update'),
    ##path('order/delete/<int:pk>/', views.OrderDeleteView.as_view(), name='order_delete'),
]