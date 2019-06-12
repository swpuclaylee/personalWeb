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


# 电影推荐
class MovieModelAdmin(object):
    list_display = ("mImage", "mName", "mComment", "mUrl")
    search_fields = ("mName",)
    list_filter = ("mName",)


# 书籍推荐1
class FirstBookModelAdmin(object):
    list_display = ("bName", "bImage", "bAuthor", "bComment", "bUrl", "bClassFirst", "bClassSecond")
    search_fields = ("bName", "bAuthor")
    list_filter = ("bName", "bAuthor")


# 书籍推荐2
class SecondBookModelAdmin(object):
    list_display = ("bName", "bImage", "bAuthor", "bComment", "bUrl")
    search_fields = ("bName", "bAuthor")
    list_filter = ("bName", "bAuthor")


xadmin.site.register(FirstBookModel, FirstBookModelAdmin)
xadmin.site.register(MovieModel, MovieModelAdmin)
xadmin.site.register(SecondBookModel, SecondBookModelAdmin)

