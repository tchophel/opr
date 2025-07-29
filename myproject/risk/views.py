from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import RiskLog
from .forms import RiskLogForm

class RiskLogListView(LoginRequiredMixin, ListView):
    model = RiskLog
    template_name = 'budget/risk_log_list.html'
    context_object_name = 'risks'

    def get_queryset(self):
        return RiskLog.objects.filter(user=self.request.user)

class RiskLogCreateView(LoginRequiredMixin, CreateView):
    model = RiskLog
    form_class = RiskLogForm
    template_name = 'risk_log_form.html'
    success_url = reverse_lazy('risk:risk_log_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class RiskLogUpdateView(LoginRequiredMixin, UpdateView):
    model = RiskLog
    form_class = RiskLogForm
    template_name = 'risk_log_form.html'
    success_url = reverse_lazy('risk:risk_log_list')

    def get_queryset(self):
        return RiskLog.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class RiskLogDeleteView(LoginRequiredMixin, DeleteView):
    model = RiskLog
    template_name = 'risk_log_confirm_delete.html'
    success_url = reverse_lazy('risk:risk_log_list')

    def get_queryset(self):
        return RiskLog.objects.filter(user=self.request.user)