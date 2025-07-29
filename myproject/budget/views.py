from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Budget, Expense
from .forms import BudgetForm, ExpenseForm

class BudgetListView(LoginRequiredMixin, ListView):
    model = Budget
    template_name = 'budget_list.html'
    context_object_name = 'budgets'

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

class BudgetCreateView(LoginRequiredMixin, CreateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'budget_form.html'
    success_url = reverse_lazy('budget:budget_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BudgetUpdateView(UpdateView):
    model = Budget
    fields = ['name', 'amount']  # change fields as per your model
    template_name = 'budget_form.html'  # or your actual template
    success_url = reverse_lazy('budget_list')  # adjust as needed

class BudgetDeleteView(DeleteView):
    model = Budget
    template_name = 'budget_confirm_delete.html'  # Create this template
    success_url = reverse_lazy('budget_list')  # Adjust to your actual budget list view name

class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = 'expense_list.html'
    context_object_name = 'expenses'

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expense_form.html'
    success_url = reverse_lazy('budget:expense_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'budget/expense_form.html'
    success_url = reverse_lazy('budget:expense_list')

    def get_queryset(self):
        # Only allow updating expenses owned by the current user
        return Expense.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass user to filter budgets
        return kwargs
    
class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = 'budget/expense_confirm_delete.html'
    success_url = reverse_lazy('budget:expense_list')

    def get_queryset(self):
        # Only allow deleting expenses owned by the current user
        return Expense.objects.filter(user=self.request.user)