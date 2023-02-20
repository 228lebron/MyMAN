from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


app_name = 'parts'

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    path('responses/', views.sale_manager_view, name='responses'),
    path('', views.requests_and_quotas, name='requests_and_quotas'),
    path('quotas/', views.quota_list, name='quota_list'),
    path('quotas/upload/', views.upload_quotas, name='upload_quotas'),
    path('parts/', views.part_list, name='part_list'),
    path('parts/<int:part_id>/', views.PartDetailView.as_view(), name='part_detail'),
    path('parts/create/', views.PartCreateView.as_view(), name='part_create'),
    path('<int:pk>/edit/', views.PartUpdateView.as_view(), name='part_edit'),
    path('request/create/', views.RequestCreateView.as_view(), name='request_create'),
    path('request/list/', views.request_list, name='request_list'),
    path('request/attach_quota/<int:pk>/', views.AttachQuotaToRequestView.as_view(), name='attach_quota'),
]
