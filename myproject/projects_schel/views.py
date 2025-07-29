from django.contrib.auth.mixins import LoginRequiredMixin  # ✅ Add this
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse
from .models import Activity
from .forms import ActivityForm

class ActivityCreateView(LoginRequiredMixin, CreateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'activity_form.html'

    def form_valid(self, form):
        # Assign the logged-in user to the activity
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dashboard')

class ActivityUpdateView(LoginRequiredMixin, UpdateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'activity_form.html'

    def get_success_url(self):
        return reverse('projects_schel:project_detail', kwargs={'pk': self.object.project.pk})

class ActivityDeleteView(LoginRequiredMixin, DeleteView):
    model = Activity
    template_name = 'activity_confirm_delete.html'

    def get_success_url(self):
        return reverse('projects_schel:project_detail', kwargs={'pk': self.object.project.pk})
    
class ActivityListView(LoginRequiredMixin, ListView):
    model = Activity
    template_name = 'projects/activity_list.html'
    context_object_name = 'activities'

    def get_queryset(self):
        # Only show activities for the logged-in user
        return Activity.objects.filter(user=self.request.user).order_by('-created_at')