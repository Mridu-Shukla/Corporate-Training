from django.contrib import admin
from .models import Faculty, School, CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Faculty)
admin.site.register(School)
