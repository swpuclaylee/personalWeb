import xadmin
from .models import *
from xadmin import views
# Register your models here.


# 后台主题功能
class AdminSettings(object):
    enable_themes = True
    use_bootswatch = True


# 标题及版权修改
class GlobalSettings(object):
    site_title = '二两个人网站管理系统'
    site_footer = 'erliang.com'
    # 菜单样式设置
    menu_style = 'accordion'


# 内容分类
class CateGoryAdmin(object):
    list_display = ("name", "id", "url")
    search_fields = ("name",)
    list_filter = ("name", "id")


# 门户网站
class WebSiteAdmin(object):
    list_display = ("name", "url")
    search_fields = ("name",)
    list_filter = ("name", "url")


# 主页欢迎
class HomeWelcomeAdmin(object):
    list_display = ("content1", "content2", "pic1_path")
    search_fields = ("content1",)
    list_filter = ("content1", "content2")


# Python学习
class PythonStudyAdmin(object):
    list_display = ("source", "sourceUrl")
    search_fields = ("source",)
    list_filter = ("source", "sourceUrl")


# Django学习
class DjangoStudyAdmin(object):
    list_display = ("source", "sourceUrl")
    search_fields = ("source",)
    list_filter = ("source", "sourceUrl")


# Spider学习
class SpiderStudyAdmin(object):
    list_display = ("source", "sourceUrl")
    search_fields = ("source",)
    list_filter = ("source", "sourceUrl")


# 社交
class SocialModeAdmin(object):
    list_display = ("socialMode", "socialName")
    search_fields = ("socialMode",)
    list_filter = ("socialMode", "socialName")


# 最近工作
class RecentWorkAdmin(object):
    list_display = ("workName", "smallImage", "workContent", "largerImage")
    search_fields = ("workName",)
    list_filter = ("workName", "smallImage", "workContent", "largerImage")


# 最近工作
class FunnyParagraphAdmin(object):
    list_display = ("pClass", "pId", "pImage", "pContent")
    list_filter = ("pClass", "pId", "pImage", "pContent")


# 最近工作
class HumorousJokeAdmin(object):
    list_display = ("pContent", "pId")
    search_fields = ("pContent", "pId")
    list_filter = ("pContent", "pId")


xadmin.site.register(FunnyParagraphModel, FunnyParagraphAdmin)
xadmin.site.register(HumorousJokeModel, HumorousJokeAdmin)
xadmin.site.register(RecentWorkModel, RecentWorkAdmin)
xadmin.site.register(SocialMode, SocialModeAdmin)
xadmin.site.register(SpiderStudy, SpiderStudyAdmin)
xadmin.site.register(DjangoStudy, DjangoStudyAdmin)
xadmin.site.register(PythonStudy, PythonStudyAdmin)
xadmin.site.register(WebSite, WebSiteAdmin)
xadmin.site.register(Category, CateGoryAdmin)
xadmin.site.register(HomeWelcome, HomeWelcomeAdmin)
xadmin.site.register(views.BaseAdminView, AdminSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)
