from django.contrib import admin
from .models import *
import xadmin
# Register your models here.


# 标签
class TagModelAdmin(object):
    list_display = ("tag",)
    search_fields = ("tag",)
    list_filter = ("tag",)


# 广告
class AdModelAdmin(object):
    list_display = ("adImage",)
    search_fields = ("adImage",)
    list_filter = ("adImage",)


# 文章
class ArticleModelAdmin(object):
    list_display = ("title", "date_publish", "click_count")
    search_fields = ("title",)
    list_filter = ("title",)
    style_fields = {'content': 'ueditor'}


# 评论
class CommentModelAdmin(object):
    list_display = ("name", "date_publish", "pid")
    search_fields = ("date_publish",)
    list_filter = ("date_publish",)
    style_fields = {'content': 'ueditor'}


xadmin.site.register(TagModel, TagModelAdmin)
xadmin.site.register(AdModel, AdModelAdmin)
xadmin.site.register(ArticleModel, ArticleModelAdmin)
xadmin.site.register(CommentModel, CommentModelAdmin)
