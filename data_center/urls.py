from django.urls import path, re_path
from data_center import views

urlpatterns = [
    path('index/', views.index, name="data_center_index"),
    path('config/', views.data_config, name="data_center_config"),
    path('create_data/', views.create_data_config, name="create_data_config"),
    path('update_data/', views.update_data_config, name="update_data_config"),
]