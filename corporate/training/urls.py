from django.urls import path, re_path
from .views import getTraining,getTrainingDetail

app_name = "training"

urlpatterns = [
    path("/",getTraining, name="trainings"),
    path("/<int:tid>",getTrainingDetail, name="detail"),
]
