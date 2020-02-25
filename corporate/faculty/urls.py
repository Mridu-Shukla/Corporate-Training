from django.urls import path

from .views import LoginView, LogoutView, DashboardView
from training.views import AddTrainingView

app_name = "faculty"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("addTraining/", AddTrainingView.as_view(), name="add_training"),
]
