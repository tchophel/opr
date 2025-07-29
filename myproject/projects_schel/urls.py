from django.urls import path
from . import views

app_name = 'projects_schel'  # Important for using {% url 'projects:activity_create' %} in templates

urlpatterns = [
    # Activity URLs
    # in projects_schel/urls.p
    path('activities/create/', views.ActivityCreateView.as_view(), name='activity_create'),
    path('activities/<int:pk>/edit/', views.ActivityUpdateView.as_view(), name='activity_update'),
    path('activities/<int:pk>/delete/', views.ActivityUpdateView.as_view(), name='activity_delete'),
    path('activities/', views.ActivityListView.as_view(), name='activity_list'),
]
