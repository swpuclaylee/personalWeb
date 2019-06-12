from django.conf.urls import url
from share import views


urlpatterns = [
    url(r'^sharesomething/', views.shareSomething, name='share'),
]