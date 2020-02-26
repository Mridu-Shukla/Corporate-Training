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

from .models import Faculty
from .auth_forms import UserLoginForm
from training.models import Training

User = settings.AUTH_USER_MODEL


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
