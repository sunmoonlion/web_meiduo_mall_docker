
# from .views import RegisterView
from django.urls import path, re_path

from . import views
app_name = 'users'
urlpatterns = [
    # 用户注册: reverse(users:register) == '/register/'
    path(r'register/', views.RegisterView.as_view(), name='register'),
    # 判断用户名是否重复注册
    re_path(r'^usernames/(?P<username>[a-zA-Z0-9_-]{5,20})/count/$', views.UsernameCountView.as_view()),
    # 判断用户名是否重复注册
    re_path(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$', views.MobileCountView.as_view()),
    # 用户登录
    path(r'login/', views.LoginView.as_view(), name='login'),
    # 用户退出登录
    path(r'logout/', views.LogoutView.as_view(), name='logout'),
    # 用户中心
    path(r'info/', views.UserInfoView.as_view(), name='info'),
    # 添加邮箱
    path(r'emails/', views.EmailView.as_view()),
    # 验证邮箱
    path(r'emails/verification/', views.VerifyEmailView.as_view()),
    # 展示用户地址
    path(r'addresses/', views.AddressView.as_view(), name='address'),
    # 新增用户地址
    path(r'addresses/create/', views.AddressCreateView.as_view()),
    # 更新和删除地址
    re_path(r'^addresses/(?P<address_id>\d+)/$', views.UpdateDestoryAddressView.as_view()),
    # 设置默认地址
    re_path(r'^addresses/(?P<address_id>\d+)/default/$', views.DefaultAddressView.as_view()),
    # 更新地址标题
    re_path(r'^addresses/(?P<address_id>\d+)/title/$', views.UpdateTitleAddressView.as_view()),
    # 用户商品浏览记录
    path(r'browse_histories/', views.UserBrowseHistory.as_view()),
]