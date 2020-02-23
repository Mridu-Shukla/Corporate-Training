from django.urls import path
from .views import FacultyView

app_name = 'faculty'

urlpatterns = [
    path('faculty/', FacultyView.as_view(), name="faculty-list"),
]