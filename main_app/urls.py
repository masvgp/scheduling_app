from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'exam_info', views.get_exam_info),
    url(r'date_info', views.get_date_info),
    url(r'test_request/(?P<id>\d+)/$', 
        views.test_request,
        name="test_request"),
]
