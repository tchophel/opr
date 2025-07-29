from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from projects_schel.models import Activity
from budget.models import Budget
from django.views.generic import ListView
from projects.models import Project
from django.db.models import Prefetch

def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'accounts/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    budgets = Budget.objects.filter(user=request.user).prefetch_related('expenses')
    total_budget_amount = sum(budget.total_budget for budget in budgets)
    total_expense_amount = sum(
        expense.amount 
        for budget in budgets 
        for expense in budget.expenses.all()
    )
    remaining_balance = total_budget_amount - total_expense_amount
    
    return render(request, 'accounts/dashboard.html', {
        'user': request.user,
        'budgets': budgets,
        'total_budget_amount': total_budget_amount,
        'total_expense_amount': total_expense_amount,
        'remaining_balance': remaining_balance,
        'activities': Activity.objects.filter(user=request.user)  # Keep your activities
    })

class ProjectReportView(ListView):
    template_name = 'accounts/home.html'
    context_object_name = 'project_data'

    def get_queryset(self):
        projects = Project.objects.prefetch_related(
            'activities', 'budgets'
        ).order_by('-created_at')

        project_data = []
        for project in projects:
            project_data.append({
                'project': project,
                'activity': project.activities.first(),
                'budget': project.budgets.first(),
            })

        return project_data
