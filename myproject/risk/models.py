from django.db import models
from accounts.models import CustomUser

class Expense(models.Model):
    STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('paid', 'Paid'),
        ('pending', 'Pending Approval'),
        ('rejected', 'Rejected'),
    ]
    
  
class RiskLog(models.Model):
    SEVERITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]
    
    PROBABILITY_CHOICES = [
        ('rare', 'Rare (<10%)'),
        ('unlikely', 'Unlikely (10-30%)'),
        ('possible', 'Possible (30-50%)'),
        ('likely', 'Likely (50-70%)'),
        ('certain', 'Certain (>70%)'),
    ]
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='risk_logs' )
    risk = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    probability = models.CharField(max_length=20, choices=PROBABILITY_CHOICES)
    contingency_plan = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Risk Log"
        verbose_name_plural = "Risk Logs"

    def __str__(self):
        return f"{self.risk} ({self.get_severity_display()})"