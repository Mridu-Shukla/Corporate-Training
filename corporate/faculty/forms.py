from django.forms import ModelForm
from .models import Faculty, School


class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"


class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = "__all__"
