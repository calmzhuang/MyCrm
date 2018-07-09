# import json

from django.shortcuts import render, HttpResponse
# import importlib
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from king_admin.utils import table_filter, paginator_class
# Create your views here.
from king_admin import king_admin
from king_admin.templatetags.tags import build_table_row
from django.utils.safestring import mark_safe

def index(request):
    #print(king_admin.enabled_admins['crm']['customerfollowup'].model )
    return render(request, "king_admin/table_index.html", {'table_list': king_admin.enabled_admins})


def display_table_objs(request, app_name, table_name):

    print("-->", app_name, table_name)
    #models_module = importlib.import_module('%s.models'%(app_name))
    #model_obj = getattr(models_module,table_name)
    admin_class = king_admin.enabled_admins[app_name][table_name]
    #admin_class = king_admin.enabled_admins[crm][userprofile]

    #object_list = admin_class.model.objects.all()
    object_list, filter_condtions = table_filter(request, admin_class)
    page = request.GET.get('page')
    query_sets = paginator_class(object_list, admin_class, page)
    return render(request, "king_admin/table_objs.html", {"admin_class": admin_class,
                                                        "query_sets": query_sets,
                                                        "filter_condtions": filter_condtions,
                                                        'app_name': app_name,
                                                        'table_name': table_name},)

def display_table_ajax(request):
    if request.method == 'GET':
        admin_class_detail = request.GET.get('admin_class_detail')
        admin_class_detail = eval(admin_class_detail)
        admin_class = king_admin.enabled_admins[admin_class_detail[0]][admin_class_detail[1]]
        page = request.GET.get('page')
        object_list, filter_condtions = table_filter(request, admin_class)
        query_sets = paginator_class(object_list, admin_class, page)
        for obj in query_sets:
            str_list = '<tr>'
            str_list += build_table_row(obj, admin_class)
            str_list += '</tr>'
        return HttpResponse(mark_safe(str_list))

