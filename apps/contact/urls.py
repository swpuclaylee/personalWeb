from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^contactMe/', contact, name='contactMe'),
    url(r'^add/', add, name='add'),
    url(r'^sucess/', sucess, name='sucess')
]