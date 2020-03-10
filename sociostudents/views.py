from django.shortcuts import render
from .models import Student

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')


def all_students(request):
    students = Student.objects.all()
    return render(request, 'students/all_students.html', {'students': students})
