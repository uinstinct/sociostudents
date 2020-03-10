from django import forms

from .models import Student

class StudentForm:

    class Meta:
        model = Student
        fields = ('username','name',)