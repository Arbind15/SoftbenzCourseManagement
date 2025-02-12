from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.timezone import now

from .models import Enrollment, Student, Category, MCQ, Course, Video, Document


def dashboard(request):
    ctx = {}
    ctx['enrolls'] = Enrollment.objects.all().order_by('-id')
    return render(request, 'mainApp/dashboard.html', ctx)


def addStudent(request):
    if request.method == "POST":
        Student.objects.create(username=request.POST.get('name'), email=request.POST.get('email'))
    return render(request, 'mainApp/addStudent.html', {})


def mcq(request):
    if request.method == "POST":
        MCQ.objects.create(
            question=request.POST.get('question'),
            option1=request.POST.get('op1'),
            option2=request.POST.get('op2'),
            option3=request.POST.get('op3'),
            option4=request.POST.get('op4'),
            correct_answers=request.POST.get('ans')
        )
    return render(request, 'mainApp/addMCQs.html', {})


def addCategory(request):
    if request.method == "POST":
        print(request.POST.get('parent'))
        if 'parent' in request.POST and request.POST.get('parent') != '':
            Category.objects.create(title=request.POST.get('tittle'), priority=request.POST.get('priority'),
                                    parent=Category.objects.get(id=int(request.POST.get('parent'))))
        else:
            Category.objects.create(title=request.POST.get('tittle'), priority=request.POST.get('priority'))
    return render(request, 'mainApp/addCategory.html', {'categories': Category.objects.all()})


def addCourse(request):
    if request.method == "POST":
        cou = Course.objects.create(
            title=request.POST.get('tittle'),
            description=request.POST.get('description'),
            price=request.POST.get('price'),
            category=Category.objects.get(id=int(request.POST.get('category')))
        )
        for mc in request.POST.getlist('mcqs', []):
            cou.mcqs.add(MCQ.objects.get(id=int(mc)))
        for vid in request.FILES.getlist('videos', []):
            cou.videos.add(Video.objects.create(file=vid, description='', uploaded_by=request.user))
        for doc in request.FILES.getlist('docs', []):
            cou.document.add(Document.objects.create(file=doc, description='', uploaded_by=request.user))
        cou.save()
    return render(request, 'mainApp/addCourse.html', {'categories': Category.objects.all(), 'mcqs': MCQ.objects.all()})


def enroll(request):
    if request.method == "POST":
        Enrollment.objects.create(student=Student.objects.get(id=int(request.POST.get('student'))),
                                  course=Course.objects.get(id=int(request.POST.get('course'))), enrolled_on=now())
    return render(request, 'mainApp/enrollStudent.html',
                  {'courses': Course.objects.all(), 'students': Student.objects.all()})
