from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def student_index(request):
    return render(request, 'student/student_index.html')