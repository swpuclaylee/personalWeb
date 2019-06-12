from django.db import models
from django.utils.html import format_html

# Create your models here.


# 内容分类
class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    name = models.CharField(max_length=30, verbose_name='分类名称', null=False, blank=False)
    url = models.CharField(max_length=30, verbose_name='url', default='', null=False, blank=False)
    index = models.IntegerField(default=999, verbose_name='分类排序')

    class Meta:
        verbose_name = verbose_name_plural = '内容分类'
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.name


# 门户网站链接
class WebSite(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name='网站名称')
    url = models.URLField(max_length=50, null=False, blank=False, verbose_name='网站链接')
    index = models.IntegerField(default=999, verbose_name='网站排序')

    class Meta:
        verbose_name = verbose_name_plural = '门户网站'
        ordering = ['id']

    def __unicode__(self):
        return self.name


# 主页欢迎
class HomeWelcome(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    content1 = models.CharField(max_length=200, null=False, blank=False, verbose_name='内容1')
    content2 = models.CharField(max_length=200, null=False, blank=False, verbose_name='内容2')
    pic1_path = models.FileField(upload_to='welcome', verbose_name="图片1路径", default='/static/images/default.png')

    class Meta:
        verbose_name = verbose_name_plural = '主页欢迎'
        ordering = ['id']

    def __unicode__(self):
        return self.content1


# python学习
class PythonStudy(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    source = models.CharField(max_length=50, blank=False, null=False, verbose_name='python学习')
    sourceUrl = models.URLField(max_length=50, blank=False, null=False, verbose_name='python学习连接')

    class Meta:
        verbose_name = verbose_name_plural = '学习Python'
        ordering = ['id']

    def __unicode__(self):
        return self.source


# Django学习
class DjangoStudy(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    source = models.CharField(max_length=50, blank=False, null=False, verbose_name='Django学习')
    sourceUrl = models.URLField(max_length=50, blank=False, null=False, verbose_name='Django学习连接')

    class Meta:
        verbose_name = verbose_name_plural = '学习Django'
        ordering = ['id']

    def __unicode__(self):
        return self.source


# Python爬虫学习
class SpiderStudy(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    source = models.CharField(max_length=50, blank=True, null=False, verbose_name='Spider学习')
    sourceUrl = models.URLField(max_length=50, blank=True, null=False, verbose_name='Spider学习连接')

    class Meta:
        verbose_name = verbose_name_plural = '学习Spider'
        ordering = ['id']

    def __unicode__(self):
        return self.source


# 社交
class SocialMode(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    socialMode = models.CharField(max_length=50, blank=False, null=False, verbose_name='社交方式',)
    socialName = models.CharField(max_length=50, blank=False, null=False, verbose_name='社交内容', )
    socialClass = models.CharField(max_length=50, blank=False, null=False, verbose_name='社交样式',)

    class Meta:
        verbose_name = verbose_name_plural = '社交'
        ordering = ['id']

    def __unicode__(self):
        return self.socialMode


# 最近工作
class RecentWorkModel(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    workName = models.CharField(max_length=50, blank=False, null=False, verbose_name='工作名')
    smallImage = models.ImageField(upload_to='recentWork/small/', verbose_name='小图片路径', default='')
    workContent = models.CharField(max_length=50, blank=False, null=False, verbose_name='工作内容')
    largerImage = models.ImageField(upload_to='recentWork/larger/', verbose_name='大图片路径', default='')
    index = models.IntegerField(default=999, verbose_name='排序')

    class Meta:
        verbose_name = verbose_name_plural = '最近工作'
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.workName


# 搞笑段子
class FunnyParagraphModel(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    pClass = models.CharField(max_length=50, blank=False, null=False, verbose_name='类', default='')
    pId = models.CharField(max_length=50, blank=False, null=False, verbose_name='id', default='')
    pImage = models.ImageField(upload_to='funny/funnyParagraph/', verbose_name='图片路径', default='')
    pContent = models.CharField(max_length=5000, blank=False, null=False, verbose_name='内容', default='')

    class Meta:
        verbose_name = verbose_name_plural = '搞笑段子'

    def __unicode__(self):
        return self.pContent


# 幽默笑话
class HumorousJokeModel(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    pContent = models.CharField(max_length=5000, blank=False, null=False, verbose_name='内容', default='')
    pId = models.CharField(max_length=50, blank=False, null=False, verbose_name='id', default='')

    class Meta:
        verbose_name = verbose_name_plural = '幽默笑话'

    def __unicode__(self):
        return self.pContent











