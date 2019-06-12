from django.conf.urls import url
from dailylife import views


urlpatterns = [
    url(r'life/', views.life, name='life')
]