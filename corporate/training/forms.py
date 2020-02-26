from django.forms import ModelForm
from .models import Training, Topic


class TrainingForm(ModelForm):
    class Meta:
        model = Training
        fields = "__all__"


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"
