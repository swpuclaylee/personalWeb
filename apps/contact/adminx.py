import xadmin
from .models import *
# Register your models here.


class CommentMessageModelAdmin(object):
    list_display = ("name", "email", "phone", "theme", "date")
    search_fields = ("name", "phone")
    list_filter = ("name", "email", "phone", "theme", "date")


xadmin.site.register(CommentMessageModel, CommentMessageModelAdmin)