from django.urls import path

from .views import LoginView, LogoutView, DashboardView, AddFacultyView, AddSchoolView, FacultyList, apiRoot, SchoolList
from training.views import AddTrainingView, AddTopicView, TrainingList, TopicList

app_name = "faculty"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("addTraining/", AddTrainingView.as_view(), name="add_training"),
    path("addFaculty/", AddFacultyView.as_view(), name="add_faculty"),
    path("addSchool/", AddSchoolView.as_view(), name="add_school"),
    path("addTopic/", AddTopicView.as_view(), name="add_topic"),
    path("api/faculty", FacultyList.as_view(), name="api_faculty"),
    path("api/school", SchoolList.as_view(), name="api_school"),
    path("api/topic", TopicList.as_view(), name="api_topic"),
    path("api/training", TrainingList.as_view(), name="api_training"),
    path("api/", apiRoot, name="api_root"),
]
