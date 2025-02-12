from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.utils.crypto import get_random_string


class Video(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to="Course_Videos/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Uploaded by {self.uploaded_by.username if self.uploaded_by else 'Unknown'}"


class Document(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to="Course_Documents/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Uploaded by {self.uploaded_by.username if self.uploaded_by else 'Unknown'}"


class MCQ(models.Model):
    question = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_answers = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.question

class Category(models.Model):
    title = models.CharField(max_length=100)
    priority = models.IntegerField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    videos = models.ManyToManyField(Video, null=True, blank=True)
    document = models.ManyToManyField(Document, null=True, blank=True)
    mcqs = models.ManyToManyField(MCQ, null=True, blank=True)

    def __str__(self):
        return self.title


class Student(AbstractUser):
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="student_users",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="student_permissions",
        blank=True
    )
    def save(self, *args, **kwargs):
        if not self.pk:
            pss = get_random_string(8)
            self.set_password(pss)
            send_mail(
                'Your Account Credentials',
                f'Your password is {pss}',
                settings.DEFAULT_FROM_EMAIL,
                [self.email],
            )
        super().save(*args, **kwargs)


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.username + ' - ' + self.course.title
