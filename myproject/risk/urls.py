from django.urls import path
from . import views

app_name = 'risk'

urlpatterns = [
path('risk-log/', views.RiskLogListView.as_view(), name='risk_log_list'),
path('risk-log/create/', views.RiskLogCreateView.as_view(), name='risk_log_create'),
path('risk-log/<int:pk>/edit/', views.RiskLogUpdateView.as_view(), name='risk_log_update'),
path('risk-log/<int:pk>/delete/', views.RiskLogDeleteView.as_view(), name='risk_log_delete'),
]