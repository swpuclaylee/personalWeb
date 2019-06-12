from django.db import models

# Create your models here.


class CommentMessageModel(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='联系人姓名')
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='邮箱地址')
    phone = models.CharField(max_length=50, blank=True, null=True, verbose_name='电话')
    theme = models.CharField(max_length=50, blank=True, null=True, verbose_name='主题')
    date = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    message = models.TextField(verbose_name='信息', blank=False, null=False)

    class Meta:
        verbose_name = verbose_name_plural = '联系人信息'
        ordering = ["id"]

    def __unicode__(self):
        return self.name

