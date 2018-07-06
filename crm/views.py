from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def sales_index(request):
    return render(request, 'sales_index.html')

def customer_index(request):
    return render(request, 'customer_index.html')
