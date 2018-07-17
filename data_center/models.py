from django.db import models

# Create your models here.
class DatabaseConfig(models.Model):
    '''数据库连接信息表'''
    name = models.CharField(max_length=32, verbose_name='连接名称', unique=True)
    host = models.CharField(max_length=32, verbose_name='数据库地址')
    port = models.CharField(max_length=16, verbose_name='数据库端口')
    user = models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
    db = models.CharField(max_length=32, verbose_name='数据库名称')
    charset = models.CharField(max_length=16, verbose_name='字符集')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
