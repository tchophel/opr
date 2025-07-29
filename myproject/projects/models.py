from django.db import models
from accounts.models import CustomUser

class Project(models.Model):
    STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
        ('cancelled', 'Cancelled'),
    ]
    
    BUDGET_HEADS = [
        ('capital', 'Capital Expenditure'),
        ('revenue', 'Revenue Expenditure'),
        ('grant', 'Grant'),
        ('donation', 'Donation'),
    ]
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=200)
    description = models.TextField()
    budget_head = models.CharField(max_length=50, choices=BUDGET_HEADS)
    budget = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.project_id} - {self.project_name}"