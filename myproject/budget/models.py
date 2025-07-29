from django.db import models
from accounts.models import CustomUser
from django.core.validators import MinValueValidator
from projects.models import Project

class Budget(models.Model):
    BUDGET_HEADS = [
        ('capital', 'Capital Expenditure'),
        ('revenue', 'Revenue Expenditure'),
        ('grant', 'Grant'),
        ('donation', 'Donation'),
    ]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='budgets', null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='budgets')
    total_budget = models.DecimalField(
        max_digits=15, 
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Total Budget (BTN)"
    )
    budget_head = models.CharField(max_length=50, choices=BUDGET_HEADS)
    budget_code = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.budget_code} - {self.get_budget_head_display()}"

class Expense(models.Model):
    STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('paid', 'Paid'),
        ('pending', 'Pending Approval'),
        ('rejected', 'Rejected'),
    ]
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='expenses')
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='expenses')
    date = models.DateField()
    expense_category = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(
        max_digits=15, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"

    def __str__(self):
        return f"{self.expense_category} - {self.amount} BTN"