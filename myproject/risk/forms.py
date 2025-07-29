from django import forms
from .models import RiskLog

class RiskLogForm(forms.ModelForm):
    class Meta:
        model = RiskLog
        fields = [
            # Remove 'project' since it doesn't exist
            'risk', 'description', 
            'severity', 'probability', 
            'contingency_plan', 'is_resolved'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'contingency_plan': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)