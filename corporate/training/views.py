from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from .models import Training, Topic
from .forms import TrainingForm, TopicForm
from .serializers import TopicSerializer, TrainingSerializer
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

class AddTopicView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Topic
    form_class = TopicForm
    template_name = "faculty/add_topic.html"
    success_url = reverse_lazy("faculty:dashboard")
    success_message = "%(title)s was created successfully"

class TopicList(APIView):
    serializer = TopicSerializer
    model = Topic

    def get(self, request, format=None):
        # Get all task instances as a queryset
        tasks = self.model.objects.all()
        # Serialize the queryset
        task_serializer = self.serializer(tasks, many=True)
        # Return the JSON Representation
        return Response(task_serializer.data)

class TrainingList(APIView):
    serializer = TrainingSerializer
    model = Training

    def get(self, request, format=None):
        # Get all task instances as a queryset
        tasks = self.model.objects.all()
        # Serialize the queryset
        task_serializer = self.serializer(tasks, many=True)
        # Return the JSON Representation
        return Response(task_serializer.data)