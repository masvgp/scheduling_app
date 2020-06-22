from django.conf.urls import url
from . import views

app_name = 'main_app'

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'exam_info', views.ExamView.as_view(), name='exam_info'),
    # url(r'date_info', views.DateView.as_view(), name='date_info'),
]
