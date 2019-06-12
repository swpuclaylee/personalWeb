from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^index/', views.index, name='my_index'),
]
handler404 = views.page_not_found
handler500 = views.page_error
