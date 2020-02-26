from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


from .models import Training, Topic
from .forms import TrainingForm
from faculty.models import Faculty

# Create your views here.
class AddTrainingView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Training
    form_class = TrainingForm
    template_name = "faculty/add_training.html"
    success_url = reverse_lazy("faculty:dashboard")
    success_message = "%(title)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topic_list"] = Topic.objects.all()
        context["faculty_list"] = Faculty.objects.all()
        return context
