from django.shortcuts import render
from share.models import *

# Create your views here.


def shareSomething(request):
    try:
        # 获取电影信息
        movie_list = MovieModel.objects.all()

        # 获取书籍信息
        book1_list = FirstBookModel.objects.all()

        book2_list = SecondBookModel.objects.all()
    except Exception as e:
        pass
    return render(request, 'share.html', locals())
