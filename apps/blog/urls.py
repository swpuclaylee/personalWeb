from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^blog/', blog, name='blog'),
    url(r'^archive/', archive, name='archive'),
    url(r'article/', article, name='article'),
    url(r'^comment_post/', comment_post, name='comment_post'),
    url(r'^tags/', tag_article, name='tag_name'),
]