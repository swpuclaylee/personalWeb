from django.db import models

# Create your models here.


# 推荐电影
class MovieModel(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    mImage = models.ImageField(upload_to='movie/', default='', verbose_name='图片路径')
    mComment = models.CharField(max_length=1000, blank=False, null=False, verbose_name='电影评价', default='')
    mName = models.CharField(max_length=50, blank=False, null=False, verbose_name='电影名', default='')
    mUrl = models.URLField(max_length=100, blank=False, null=False, verbose_name='电影连接', default='')

    class Meta:
        verbose_name = verbose_name_plural = '电影推荐'
        ordering = ['id']

    def __unicode__(self):
        return self.mName


# 推荐书籍1
class FirstBookModel(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    bClassFirst = models.CharField(max_length=50, blank=False, null=False, default='')
    bClassSecond = models.CharField(max_length=50, blank=False, null=False, default='')
    bName = models.CharField(max_length=50, blank=False, null=False, verbose_name='书名', default='')
    bImage = models.ImageField(upload_to='book/', default='', verbose_name='图片路径')
    bComment = models.CharField(max_length=1000, blank=False, null=False, verbose_name='书籍评价', default='')
    bAuthor = models.CharField(max_length=50, blank=False, null=False, verbose_name='书籍作者', default='')
    bUrl = models.URLField(max_length=100, blank=False, null=False, verbose_name='书籍连接', default='')

    class Meta:
        verbose_name = verbose_name_plural = '书籍推荐1'
        ordering = ['id']

    def __unicode__(self):
        return self.bName


# 推荐书籍1
class SecondBookModel(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    bName = models.CharField(max_length=50, blank=False, null=False, verbose_name='书名', default='')
    bImage = models.ImageField(upload_to='book/', default='', verbose_name='图片路径')
    bComment = models.CharField(max_length=5000, blank=False, null=False, verbose_name='书籍评价', default='')
    bAuthor = models.CharField(max_length=50, blank=False, null=False, verbose_name='书籍作者', default='')
    bUrl = models.URLField(max_length=100, blank=False, null=False, verbose_name='书籍连接', default='')

    class Meta:
        verbose_name = verbose_name_plural = '书籍推荐2'
        ordering = ['id']

    def __unicode__(self):
        return self.bName



