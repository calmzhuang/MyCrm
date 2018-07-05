from django.contrib import admin
from crm import models
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'qq', 'source', 'consultant', 'content', 'create_date')#页面展示字段
    list_filter = ('source', 'consultant', 'create_date')#页面筛选器
    search_fields = ('qq', 'name')#页面查询项
    raw_id_fields = ('consult_course',)#显示外键的详细信息
    filter_horizontal = ('tags',)#一种友好样式的复选框
    list_editable = ('content',)#设置默认可编辑字段

admin.site.register(models.Role)
admin.site.register(models.Course)
admin.site.register(models.UserProfile)
admin.site.register(models.ClassList)
admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.CourseRecord)
admin.site.register(models.Enrollment)
admin.site.register(models.Branch)
admin.site.register(models.CustomerFollowUp)
admin.site.register(models.Payment)
admin.site.register(models.StudentRecord)
admin.site.register(models.Tag)
admin.site.register(models.Menu)
