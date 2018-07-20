from django.shortcuts import render, HttpResponse, redirect
from data_center.utils import data_config_list, create_data_config_list, update_data_config_list

# Create your views here.

def index(request):
    pass

#数据库连接视图
def data_config(request):
    if request.method == 'GET':
        data_list = data_config_list()
        return render(request, 'data_center/database_config.html', {"data_list": data_list})

def create_data_config(request):
    if request.method == 'POST':
        data = request.POST
        result = create_data_config_list(data)
        if result == 'fail':
            return HttpResponse('数据库连接已存在！')
        else:
            return HttpResponse('数据库连接创建成功！')


def update_data_config(request):
    if request.method == 'POST':
        data = request.POST
        result = update_data_config_list(data)
        if result == 'fail':
            return HttpResponse('无此链接信息！')
        else:
            return HttpResponse('数据修改成功！')