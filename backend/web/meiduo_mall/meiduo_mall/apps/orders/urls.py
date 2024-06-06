from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'orders'
urlpatterns = [
    # 结算订单
    path(r'orders/settlement$', views.OrderSettlementView.as_view(), name='settlement'),
    # 提交订单
    path(r'orders/commit/', views.OrderCommitView.as_view()),
    # 提交订单成功
    path(r'orders/success/', views.OrderSuccessView.as_view()),
]