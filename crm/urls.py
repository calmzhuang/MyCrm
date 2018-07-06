from django.urls import path
from crm import views

urlpatterns = [
    path('index/', views.index),
    path('sales_index/', views.sales_index, name="sales_index"),
    path('customer_index/', views.customer_index, name="customer_index"),
]