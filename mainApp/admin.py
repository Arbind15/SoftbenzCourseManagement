from django.contrib import admin
from .models import Course, Category, Document, Video, Enrollment, Student, MCQ

# Register your models here.
admin.site.register(Document)
admin.site.register(Video)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(MCQ)