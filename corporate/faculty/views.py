from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.conf import settings
from .constants import AuthConstants
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from .models import Faculty, School
from .auth_forms import UserLoginForm
from .forms import FacultyForm, SchoolForm
from .serializers import FacultySerializer, SchoolSerializer
from training.models import Training

User = settings.AUTH_USER_MODEL


@api_view(["GET"])
def apiRoot(request, format=None):
    # Return the tasklist and trackerlist api
    api_info = {
        "faculties": reverse("faculty:api_faculty", request=request, format=format),
        "schools": reverse("faculty:api_school", request=request, format=format),
        "trainings": reverse("faculty:api_training", request=request, format=format),
        "topics": reverse("faculty:api_topic", request=request, format=format),
    }
    return Response(api_info)


class LoginView(View):
    template_name = "faculty/login.html"
    form_class = UserLoginForm

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        userLoginForm = self.form_class(request.POST)
        if userLoginForm.login_user(request):
            return HttpResponseRedirect(reverse("faculty:dashboard"))
        else:
            kwargs = {"form": userLoginForm}
            return render(request, self.template_name, kwargs)


class LogoutView(LoginRequiredMixin, RedirectView):
    permanent = False
    pattern_name = "faculty:login"

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        message = AuthConstants.sucessLogout.value
        messages.success(request, message, fail_silently=True)
        return super().dispatch(request, *args, **kwargs)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "faculty/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["faculty_list"] = Faculty.objects.all().order_by("-id")[:2]
        context["training_list"] = Training.objects.all().order_by("-id")[:2]
        return context


class AddFacultyView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Training
    form_class = FacultyForm
    template_name = "faculty/add_faculty.html"
    success_url = reverse_lazy("faculty:dashboard")
    success_message = "%(user.get_full_name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["school_list"] = School.objects.all()
        return context


class AddSchoolView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = School
    form_class = SchoolForm
    template_name = "faculty/add_school.html"
    success_url = reverse_lazy("faculty:dashboard")
    success_message = "%(school_code)s was created successfully"


class FacultyList(APIView):
    serializer = FacultySerializer
    model = Faculty

    def get(self, request, format=None):
        # Get all task instances as a queryset
        tasks = self.model.objects.all()
        # Serialize the queryset
        task_serializer = self.serializer(tasks, many=True)
        # Return the JSON Representation
        return Response(task_serializer.data)


class SchoolList(APIView):
    serializer = SchoolSerializer
    model = School

    def get(self, request, format=None):
        # Get all task instances as a queryset
        tasks = self.model.objects.all()
        # Serialize the queryset
        task_serializer = self.serializer(tasks, many=True)
        # Return the JSON Representation
        return Response(task_serializer.data)
