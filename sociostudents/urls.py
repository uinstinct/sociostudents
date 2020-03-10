from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('students', views.all_students, name='students'),
    path('students/<str:username>', views.list_student,name='list_student'),
]
