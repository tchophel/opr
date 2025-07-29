from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project
from .forms import ProjectForm

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'form.html'  # Direct path without projects/ prefix
    success_url = reverse_lazy('projects:project_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'project_detail.html'

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'form.html'
    success_url = reverse_lazy('project_list')

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'project_confirm_delete.html'
    success_url = reverse_lazy('project_list')

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)