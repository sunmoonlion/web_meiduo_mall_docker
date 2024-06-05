from django.urls import re_path, path

from . import views

app_name = 'payment'
urlpatterns = [
    # 支付
    re_path(r'payment/(?P<order_id>\d+)/', views.PaymentView.as_view()),
    # 保存订单状态
    path(r'payment/status/', views.PaymentStatusView.as_view()),
]