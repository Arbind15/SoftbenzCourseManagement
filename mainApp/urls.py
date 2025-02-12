from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("add-student/", views.addStudent, name="addStudent"),
    path("add-course/", views.addCourse, name="addCourse"),
    path("add-category/", views.addCategory, name="addCategory"),
    path("enroll/", views.enroll, name="enroll"),
    path("add-mcq/", views.mcq, name="mcq"),
    ]