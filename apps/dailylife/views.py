from django.shortcuts import render
from dailylife.models import *
# Create your views here.


def life(request):
    try:
        # 日常生活信息获取
        daily_life_list = DailyLifeModel.objects.all()
    except Exception as e:
        pass

    return render(request, 'dailylife.html', locals())