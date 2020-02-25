from django.db import models
from faculty.models import Faculty
from .constants import ImageConstant
from django.core.validators import RegexValidator
from django.urls import reverse  # new

# TODO : Add absolute_urls


class Topic(models.Model):
    title = models.CharField(verbose_name="Title of topic", max_length=50)
    short_description = models.CharField(
        verbose_name="Short description of topic", max_length=300
    )

    class Meta:
        verbose_name_plural = "Topics"

    def __str__(self):
        return self.title

    def getAllTrainings(self):
        return Topic.trainings.all()


class Training(models.Model):
    title = models.CharField(verbose_name="Title of the workshop", max_length=80)
    training_image = models.ImageField(
        upload_to="images/training/",
        help_text="Training Poster",
        blank=False,
        null=False,
    )
    topic = models.ForeignKey(
        Topic,
        related_name="trainings",
        on_delete=models.CASCADE,
        verbose_name="Topic associated with the training programme",
    )
    faculty = models.ForeignKey(
        Faculty,
        related_name="trainings",
        on_delete=models.CASCADE,
        verbose_name="Faculty associated with the training programme",
    )
    description = models.CharField(
        verbose_name="Training Program Description",
        max_length=500,
        help_text="Maximum number of words is 500",
    )
    cost = models.IntegerField(verbose_name="Cost of training")

    class Meta:
        verbose_name_plural = "Trainings"

    def __str__(self):
        return f"{self.title} : {self.faculty}"

    def getAllComments(self):
        return Training.comments.all()

    # def get_absolute_url(self):
    #     return reverse('training_detail', args=[str(self.id)])


class Comment(models.Model):
    training = models.ForeignKey(
        Training,
        related_name="comments",
        on_delete=models.CASCADE,
        verbose_name="Comments associated with training programme",
    )
    faculty = models.ForeignKey(
        Faculty,
        related_name="comments",
        on_delete=models.CASCADE,
        verbose_name="Faculty associated with the comment",
    )
    comment = models.CharField(verbose_name="Comment on the programme", max_length=500)
    creation_time = models.DateTimeField(verbose_name="Time of creation", auto_now=True)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"{self.training}: {self.comment[0:50]}"
