from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


app_name = 'parts'

# URLs for sales managers
sales_manager_patterns = [
    path('responses/', views.sale_manager_view, name='sales_manager_responses'),
    path('request/<int:pk>/add_bill', views.AddAccountView.as_view(), name='add_bill'),
]

# URLs for product managers
product_manager_patterns = [
    path('parts/', views.part_list, name='part_list'),
    path('parts/<int:pk>/', views.PartDetailView.as_view(), name='part_detail'),
    path('parts/create/', views.PartCreateView.as_view(), name='part_create'),
    path('<int:pk>/edit/', views.PartUpdateView.as_view(), name='part_edit'),
    path('request/list/', views.request_list, name='request_list'),
    path('quotas/', views.quota_list, name='quota_list'),
    path('products/list/', views.product_manager_view, name='requests_and_quotas'),
]

# Common URLs for both sales and product managers
common_patterns = [
    path('', views.initial_view, name='initial_view'),

    path('clients/', views.clients, name='clients_list'),
    path('quotas/upload/', views.upload_quotas, name='upload_quotas'),
    path('request/create/', views.RequestCreateView.as_view(), name='request_create'),
    path('request/attach_quota/<int:pk>/', views.AttachQuotaToRequestView.as_view(), name='attach_quota'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.profile, name='profile'),
]

# Combine the URL patterns for each user type
urlpatterns = common_patterns + sales_manager_patterns + product_manager_patterns
