
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'admin/', admin.site.urls),

    # haystack
    path(r'search/', include('haystack.urls')),

    # users
    path(r'', include('users.urls', namespace='users')),
    # contents
    path(r'', include('contents.urls', namespace='contents')),
    # verifications
    path(r'', include('verifications.urls')),
    # oauth
    path(r'', include('oauth.urls')),
    # areas
    path(r'', include('areas.urls')),
    # goods
    path(r'', include('goods.urls', namespace='goods')),
    # carts
    path(r'', include('carts.urls', namespace='carts')),
    # orders
    path(r'', include('orders.urls', namespace='orders')),
    # payment
    path(r'', include('payment.urls', namespace='payment')),
    path('meiduo_admin/', include('meiduo_admin.urls')),
]
