from django import forms
from .models import Budget, Expense

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['total_budget', 'budget_head', 'budget_code']
        widgets = {
            'total_budget': forms.NumberInput(attrs={'step': '0.01'}),
        }

class ExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['budget'].queryset = Budget.objects.filter(user=user)
    
    class Meta:
        model = Expense
        fields = ['budget', 'date', 'expense_category', 'description', 'amount', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }