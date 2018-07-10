from crm import models
enabled_admins = {}


class BaseAdmin(object):
    list_display = []
    list_filter = []
    list_per_page = 5

class CustomerAdmin(BaseAdmin):
    list_display = ['qq', 'name', 'source', 'consultant', 'consult_course', 'create_date']
    list_filters = ['source', 'consultant', 'consult_course']

class CustomerFollowUpAdmin(BaseAdmin):
    list_display = ('customer', 'consultant')

def register(model_class, admin_class=None):
    if model_class._meta.app_label not in enabled_admins:
        enabled_admins[model_class._meta.app_label] = {} #enabled_admins['crm'] = {}
    #admin_obj = admin_class()
    admin_class.model = model_class #绑定model 对象和admin 类
    enabled_admins[model_class._meta.app_label][model_class._meta.model_name] = admin_class
    #enabled_admins['crm']['customerfollowup'] = CustomerFollowUpAdmin

register(model_class=models.Customer, admin_class=CustomerAdmin)
register(model_class=models.CustomerFollowUp, admin_class=CustomerFollowUpAdmin)