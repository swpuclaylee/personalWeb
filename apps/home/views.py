# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.conf import settings
from home.models import *
from django.views.decorators.csrf import csrf_exempt
# import logging

# Create your views here.
# logger = logging.getLogger('home.views')


def global_settings(request):
    # 站点基本信息
    PHONE = settings.PHONE
    SITE_NAME = settings.SITE_NAME
    SITE_URL = settings.SITE_URL

    # 分类内容获取
    category_list = Category.objects.all()

    # 门户网站获取
    website_list = WebSite.objects.all()

    python_list = PythonStudy.objects.all()

    spider_list = SpiderStudy.objects.all()

    django_list = DjangoStudy.objects.all()

    return locals()


@csrf_exempt
def index(request):
    try:
        # 主页欢迎信息获取
        home_welcome_list = HomeWelcome.objects.all()

        # 主页社交方式信息获取
        social_list = SocialMode.objects.all()

        # 最近工作信息获取
        recent_work_list = RecentWorkModel.objects.all()

        # 搞笑段子信息获取
        funny_paragraph_list = FunnyParagraphModel.objects.all()

        # 幽默笑话信息获取
        humorous_joke_list = HumorousJokeModel.objects.all()

    except Exception as e:
        pass
        # logger.error(e)
    return render(request, 'index.html', locals())


# 404
def page_not_found(request):
    return render(request, '404.html')


# 500
def page_error(request):
    return render(request, '500.html')