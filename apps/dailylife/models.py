from django.db import models

# Create your models here.


# 日常生活
class DailyLifeModel(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    dClass = models.CharField(max_length=50, blank=False, null=False, verbose_name='类')
    dSmallImage = models.ImageField(upload_to='dailylife/small/', default='', verbose_name='小图片')
    dLargerImage = models.ImageField(upload_to='dailylife/large/', default='', verbose_name='大图片')
    dContent = models.CharField(max_length=1000, blank=False, null=False, verbose_name='内容', default='')

    class Meta:
        verbose_name = verbose_name_plural = "日常生活"
        ordering = ["id"]

    def __unicode__(self):
        return self.dContent
