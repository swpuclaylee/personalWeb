"""newproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import serve
from django.conf.urls.static import static
from django.conf import settings
# from django.contrib import admin
import xadmin
import django

urlpatterns = [
    url(r'^xadmin', xadmin.site.urls),
    url(r'^home/', include('home.urls')),
    url(r'^share/', include('share.urls')),
    url(r'^daily/', include('dailylife.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    url(r'^ueditor/',include('DjangoUeditor.urls')),

    # url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}, name='upload_pic')
]
