from django.urls import path

from . import views
app_name = 'carts'

urlpatterns = [
    # 购物车管理
    path(r'carts/', views.CartsView.as_view(), name='info'),
    # 全选gwc
    path(r'carts/selection/', views.CartsSelectAllView.as_view()),
]