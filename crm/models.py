from django.db import models
from django.contrib.auth.models import User

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
    tags = models.ManyToManyField("Tag", blank=True, null=True, verbose_name='客户对应标签')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_date = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.qq

class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='标签')

    def __str__(self):
        return self.name


class CustomerFollowUp(models.Model):
    '''客户跟进表'''
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, verbose_name='跟进客户')
    content = models.TextField(verbose_name='跟进内容')
    consultant = models.ForeignKey("UserProfile", on_delete=models.CASCADE, verbose_name='跟进人')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update = models.DateTimeField(auto_now=True, verbose_name='最新跟进时间')
    intention_choices = ((0, '2周内报名'),
                         (1, '1个月内报名'),
                         (2, '近期无报名计划'),
                         (3, '已在其他机构报名'),
                         (4, '已报名'),
                         (5, '已拉黑'))
    intention = models.SmallIntegerField(choices=intention_choices, verbose_name='跟进状态')

    def __str__(self):
        return "<%s : %s>" % (self.customer.qq, self.intention)


class Course(models.Model):
    '''课程表'''
    name = models.CharField(max_length=64, unique=True, verbose_name='课程名称')
    price = models.PositiveSmallIntegerField(verbose_name='课程价格')
    period = models.PositiveSmallIntegerField(verbose_name='周期（月）')
    outline = models.TextField(verbose_name='大纲')

    def __str__(self):
        return self.name

class Branch(models.Model):
    '''校区'''
    name = models.CharField(max_length=128, unique=True, verbose_name='校区名称')
    addr = models.CharField(max_length=128, verbose_name='校区地址')

    def __str__(self):
        return self.name

class ClassList(models.Model):
    '''班级表'''
    branch = models.ForeignKey("Branch", on_delete=models.CASCADE, verbose_name='所属分校')
    course = models.ForeignKey("Course", on_delete=models.CASCADE, verbose_name='所学课程')
    class_type_choices = (
        (0, '面授（脱产）'),
        (1, '面授（周末）'),
        (2, '网络班'),
    )
    class_type = models.SmallIntegerField(choices=class_type_choices, verbose_name='班级类型')
    semester = models.PositiveSmallIntegerField(verbose_name='学期')
    teachers = models.ManyToManyField("UserProfile", verbose_name='授课老师')
    start_date = models.DateTimeField(verbose_name='开班日期')
    end_date = models.DateTimeField(verbose_name='结业日期', blank=True, null=True)

    def __str__(self):
        return "%s %s %s" % (self.branch, self.course, self.semester)

    class Meta:
        unique_together = ('branch', 'course', 'semester')

class CourseRecord(models.Model):
    '''上课记录'''
    from_class = models.ForeignKey("ClassList", on_delete=models.CASCADE, verbose_name='班级')
    day_num = models.PositiveSmallIntegerField(verbose_name='第几节（天）')
    teacher = models.ForeignKey("UserProfile", on_delete=models.CASCADE, verbose_name='上课老师')
    has_homework = models.BooleanField(default=True, verbose_name='是否有有作业')
    homework_title = models.CharField(max_length=128, blank=True, null=True, verbose_name='作业主题')
    homework_content = models.TextField(blank=True, null=True, verbose_name='作业主题')
    outline = models.TextField(verbose_name='本节课程大纲')
    date = models.DateTimeField(auto_now_add=True, verbose_name='上课时间')

    def __str__(self):
        return "%s %s" % (self.from_class, self.day_num)

    class Meta:
        unique_together = ('from_class', 'day_num')

class StudentRecord(models.Model):
    '''学习记录'''
    student = models.ForeignKey("Enrollment", on_delete=models.CASCADE, verbose_name='关联学生')
    course_record = models.ForeignKey("CourseRecord", on_delete=models.CASCADE, verbose_name='关联课程记录')
    attendance_choices = (
        (0, '已签到'),
        (1, '迟到'),
        (2, '缺勤'),
        (3, '早退'),
    )
    attendance = models.SmallIntegerField(choices=attendance_choices, default=0, verbose_name='出勤')

    score_choices = (
        (100, 'A+'),
        (90, 'A'),
        (85, 'B+'),
        (80, 'B'),
        (75, 'B-'),
        (70, 'C+'),
        (60, 'C'),
        (40, 'C-'),
        (0, 'Not Available'),
        (-50, 'D'),
        (-100, 'Copy'),
    )
    score = models.SmallIntegerField(choices=score_choices, verbose_name='课程成绩')
    memo = models.TextField(blank=True, null=True, verbose_name='备注')
    date = models.DateTimeField(auto_now_add=True, verbose_name='上课时间')

    def __str__(self):
        return "%s %s %s" % (self.student, self.course_record, self.score)

class Enrollment(models.Model):
    '''报名表'''
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, verbose_name='客户')
    enrolled_class = models.ForeignKey("ClassList", on_delete=models.CASCADE, verbose_name='所报班级')
    consultant = models.ForeignKey("UserProfile", on_delete=models.CASCADE, verbose_name='课程顾问')
    contract_agreed = models.BooleanField(default=False, verbose_name='学生同意条款')
    contract_approved = models.BooleanField(default=False, verbose_name='合同已审核')
    date = models.DateTimeField(auto_now_add=True, verbose_name='报名时间')

    def __str__(self):
        return "%s %s" % (self.customer, self.enrolled_class)

    class Meta:
        unique_together = ('customer', 'enrolled_class')

class Payment(models.Model):
    '''缴费记录'''
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, verbose_name='缴费人')
    course = models.ForeignKey("Course", on_delete=models.CASCADE, verbose_name='所报课程')
    amount = models.PositiveIntegerField(default=500, verbose_name='缴费数额')
    consultant = models.ForeignKey("UserProfile", on_delete=models.CASCADE, verbose_name='办理人')
    date = models.DateTimeField(auto_now_add=True, verbose_name='缴费时间')

    def __str__(self):
        return "%s %s" % (self.customer, self.amount)

class UserProfile(models.Model):
    '''账号表'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, verbose_name='用户名')
    roles = models.ManyToManyField("Role", blank=True, null=True, verbose_name='关联角色')

    def __str__(self):
        return self.name

class Role(models.Model):
    '''角色表'''
    name = models.CharField(max_length=32, unique=True, verbose_name='角色级别')
    def __str__(self):
        return self.name