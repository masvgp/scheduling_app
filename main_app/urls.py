from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'exam_info', views.exam_info)
]
