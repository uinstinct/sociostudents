from django.shortcuts import render, get_object_or_404
from .models import Student

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')


def all_students(request):
    students = Student.objects.all()
    return render(request, 'students/all_students.html', {'students': students})

def list_student(request, username):
    student =  get_object_or_404(Student, username=username)
    return render(request, 'students/list_student.html', {'student':student})
    