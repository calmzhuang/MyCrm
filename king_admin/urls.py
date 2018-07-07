from django.urls import path, re_path
from king_admin import views

urlpatterns = [
    path('index/', views.index, name="table_index"),
    re_path('(\w+)/(\w+)/', views.display_table_objs, name="table_objs"),
]