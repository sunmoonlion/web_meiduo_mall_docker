from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    # 提供QQ登录扫码页面
    path(r'qq/login/', views.QQAuthURLView.as_view()),
    # 处理QQ登录回调
    url(r'oauth_callback/', views.QQAuthUserView.as_view()),
]