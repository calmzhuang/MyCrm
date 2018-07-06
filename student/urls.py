from django.urls import path
from student import views

urlpatterns = [
    path('index/', views.index),
    path('student_index/', views.student_index, name="student_index"),
]