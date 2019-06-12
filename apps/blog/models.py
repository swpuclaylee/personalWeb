# -*- coding:utf-8 -*-
from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.


# 标签
class TagModel(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    tag = models.CharField(max_length=30, verbose_name='标签')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag

    def __unicode__(self):
        return self.tag


# 广告
class AdModel(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    adImage = models.ImageField(upload_to='ad/', default='', verbose_name='图片链接')

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.adImage


# 自定义一个文章model的管理器
class ArticleManager(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('date_publish')
        for date in date_list:
            date = date['date_publish'].strftime('%Y/%m')
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list


# 文章
class ArticleModel(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    title = models.CharField(max_length=50, verbose_name='文章标题', blank=False, null=False, default='')
    image = models.ImageField(upload_to='blog/', default='')
    content = UEditorField(verbose_name='博客内容',
                           width=700,
                           height=400,
                           toolbars='full',
                           imagePath='ueditor/images/',
                           filePath='ueditor/files/',
                           upload_settings={'imageMaxSizing': 1024000}, blank=False, null=False, default='')
    click_count = models.IntegerField(default=0, verbose_name='点击次数')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    tag = models.ManyToManyField(TagModel, verbose_name='标签')

    objects = ArticleManager()

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __str__(self):
        return self.title


# 评论模型
class CommentModel(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    name = models.CharField(max_length=50, blank=False, null=False, default='', verbose_name='姓名')
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='邮箱地址')
    content = UEditorField(verbose_name='评论内容',
                           width=700,
                           height=400,
                           toolbars='full',
                           imagePath='ueditor/images/',
                           filePath='ueditor/files/',
                           upload_settings={'imageMaxSizing': 1024000},
                           default='')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    pid = models.IntegerField(verbose_name='pid', default='0')
    article = models.ForeignKey(ArticleModel, blank=True, null=True, verbose_name='文章')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return str(self.id)



