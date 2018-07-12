from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def table_filter(request,admin_class):
    '''进行条件过滤并返回过滤后的数据'''
    filter_conditions = {}
    for k, v in request.GET.items():
        if v and k != 'page' and k != 'admin_class_detail' and k != 'ordername': #保留的分页关键字
            filter_conditions[k] = v
    ordername = request.GET.get('ordername')
    if ordername:
        return admin_class.model.objects.filter(**filter_conditions).order_by(ordername), filter_conditions
    else:
        return admin_class.model.objects.filter(**filter_conditions), filter_conditions

def paginator_class(object_list, admin_class, page):
    paginator = Paginator(object_list, admin_class.list_per_page)  # Show 25 contacts per page
    try:
        query_sets = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        query_sets = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        query_sets = paginator.page(paginator.num_pages)
    return query_sets
