from django.contrib import admin
from .models import *
import xadmin
# Register your models here.


# 日常生活
class DailyLifeModelAdmin(object):
    list_display = ("dClass", "dSmallImage", "dLargerImage", "dContent")
    search_fields = ("dContent",)
    list_filter = ("dContent",)


xadmin.site.register(DailyLifeModel, DailyLifeModelAdmin)


