from django.urls import path, re_path
from king_admin import views

urlpatterns = [
    path('index/', views.index),
]