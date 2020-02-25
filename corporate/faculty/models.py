from django.db import models
from django.conf import settings
from .constants import ImageConstant
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

# TODO : Add absolute_urls


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)


class School(models.Model):
    school_code_validator = RegexValidator(
        regex="^[A-Z]{3,10}$", message="Not a valid School Code"
    )
    school_code = models.CharField(
        verbose_name="School Code", max_length=10, validators=[school_code_validator]
    )
    school_name = models.CharField(verbose_name="School Name", max_length=80)

    class Meta:
        verbose_name_plural = "Schools"
        unique_together = ["school_code", "school_name"]

    def __str__(self):
        return self.school_code


class Faculty(models.Model):
    phone_number_regex = RegexValidator(
        regex="^[1-9][0-9]{9}$", message="Not a valid phone number",
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="users", on_delete=models.CASCADE
    )
    phone = models.BigIntegerField(
        verbose_name="Phone number", validators=[phone_number_regex], unique=True
    )
    bio = models.CharField(verbose_name="Faculty Bio", max_length=300)
    school = models.ForeignKey(
        School,
        related_name="faculties",
        on_delete=models.CASCADE,
        verbose_name="School of the faculty",
    )
    profile_photo = models.ImageField(
        upload_to="images/profile/",
        help_text="Profile Photo",
        default=ImageConstant.defaultImage.value,
    )

    class Meta:
        verbose_name_plural = "Faculties"

    def __str__(self):
        return f"{self.user.username} {self.school}"

    def getAllComments(self):
        return Faculty.comments.all()

    def getAllTrainings(self):
        return Faculty.trainings.all()
