from django.views.generic import ListView
from .models import Job


class HomePage(ListView):
    model = Job
    template_name = 'index.html'
    context_object_name = 'jobs'