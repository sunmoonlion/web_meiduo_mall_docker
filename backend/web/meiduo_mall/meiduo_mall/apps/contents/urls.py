from django.urls import path

from . import views

app_name = 'contents'
urlpatterns = [
    # 首页广告: '/'
    path(r'', views.IndexView.as_view(), name='index'),
]