# -*- coding:utf-8-*-
from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage,PageNotAnInteger
from django.views import View
from .forms import *
# Create your views here.


def global_settings(request):
    # 获取标签信息
    tag_list = TagModel.objects.all()

    # 广告信息获取
    ad_list = AdModel.objects.all()

    # 文章归档
    archive_list = ArticleModel.objects.distinct_date()
    return locals()


def blog(request):
    try:
        # 文章信息获取
        article_list = ArticleModel.objects.all()

        # 分页
        paginator = Paginator(article_list, 1)
        try:
            page = int(request.GET.get('page', 1))
            article_list = paginator.page(page)
        except (EmptyPage, InvalidPage, PageNotAnInteger):
            article_list = paginator.page(1)
    except Exception as e:
        pass
    return render(request, 'blog.html', locals())


def archive(request):
    try:
        year = request.GET.get('year', None)
        month = request.GET.get('month', None)

        # 归档文章获取
        article_list = ArticleModel.objects.filter(date_publish__icontains=year+'-'+month)
        paginator = Paginator(article_list, 1)
        try:
            page = int(request.GET.get('page', 1))
            article_list = paginator.page(page)
        except (EmptyPage, InvalidPage, PageNotAnInteger):
            article_list = paginator.page(1)
    except Exception as e:
        pass
    return render(request, 'archive.html', locals())


def article(request):
    try:
        # 文章信息获取
        id = request.GET.get('id', None)
        comment_list = CommentModel.objects.filter(pid=id)
        try:
            article = ArticleModel.objects.get(pk=id)
            article.click_count += 1
            article.save(update_fields=['click_count'])
        except ArticleModel.DoesNotExist:
            return render(request, 'failure.html')
    except Exception as e:
        pass
    return render(request, 'blog-item.html', locals())


def comment_post(request):
    try:
        if request.method == 'POST':
            name = request.POST.get("name")
            email = request.POST.get("email")
            id = request.POST.get("id")
            message = request.POST.get("message")
            CommentModel.objects.create(
                name=name,
                email=email,
                pid=id,
                content=message,
            )
    except Exception as e:
        pass
    return redirect(request.META['HTTP_REFERER'])


def tag_article(request):
    try:
        tag = request.GET.get('tag', None)

        # 标签文章获取
        article_list = ArticleModel.objects.get(tag=tag)
        print(type(article_list))
        paginator = Paginator(article_list, 1)
        try:
            page = int(request.GET.get('page', 1))
            article_list = paginator.page(page)
        except (EmptyPage, InvalidPage, PageNotAnInteger):
            article_list = paginator.page(1)
    except Exception as e:
        pass
    return render(request, 'tag.html', locals())

