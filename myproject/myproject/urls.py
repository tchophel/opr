from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('projects/', include('projects.urls')),
    path('projects_schel/', include('projects_schel.urls')),
    path('budget/', include('budget.urls')),
    path('risk/', include('risk.urls')),
]