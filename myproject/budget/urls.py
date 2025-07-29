from django.urls import path
from . import views

app_name = 'budget'

urlpatterns = [
    path('', views.BudgetListView.as_view(), name='budget_list'),
    path('create/', views.BudgetCreateView.as_view(), name='budget_create'),
    path('<int:pk>/edit/', views.BudgetUpdateView.as_view(), name='budget_update'),
    path('<int:pk>/delete/', views.BudgetDeleteView.as_view(), name='budget_delete'),
    
    path('expenses/', views.ExpenseListView.as_view(), name='expense_list'),
    path('expenses/create/', views.ExpenseCreateView.as_view(), name='expense_create'),
    path('expenses/<int:pk>/edit/', views.ExpenseUpdateView.as_view(), name='expense_update'),
    path('expenses/<int:pk>/delete/', views.ExpenseDeleteView.as_view(), name='expense_delete'),
]