from django.db import models

# Create your models here.

class Customer(models.Model):
    '''客户信息表'''
    name = models.CharField(max_length=32, null=True, blank=True, verbose_name='客户名称')#blank作用：django-admin中可以为空
    qq = models.CharField(max_length=64, null=False, unique=True, verbose_name='客户QQ')
    qq_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='客户名称')
    phone = models.CharField(max_length=64, blank=True, null=True, verbose_name='客户手机号')
    source_choices = (('0', '转介绍'),
                     ('1', 'QQ群'),
                     ('2', '官网'),
                     ('3', '百度推广'),
                     ('4', '51CTO'),
                     ('5', '知乎'),
                     ('6', '市场推广'),
                     )
    source = models.SmallIntegerField(choices=source_choices, verbose_name='客户介绍来源')
    referral_from = models.CharField(max_length=64, blank=True, null=True, verbose_name='客户介绍人')

    consult_course = models.ForeignKey("Course", on_delete=models.CASCADE, verbose_name='咨询课程')
    content = models.TextField(verbose_name='咨询详情')
    consultant = models.ForeignKey("UserProfile", on_delete=models.CASCADE, verbose_name='跟进销售')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_date = models.DateTimeField(auto_now=True, verbose_name='更新时间')

class CustomerFollowUp(models.Model):
    '''客户跟进表'''
    pass

class Course(models.Model):
    '''课程表'''
    pass

class ClassList(models.Model):
    '''班级表'''
    pass

class CourseRecord(models.Model):
    '''上课记录'''
    pass

class StudentRecord(models.Model):
    '''学习记录'''
    pass

class Enrollment(models.Model):
    '''报名表'''
    pass

class UserProfile(models.Model):
    '''账号表'''
    pass

class Role(models.Model):
    '''权限表'''
    pass