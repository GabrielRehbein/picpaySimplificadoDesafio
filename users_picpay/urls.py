from django.urls import path
from .views import customer_views
from .views import shopkeeper_views


urlpatterns = [
    path('customers/', customer_views.CustomerView.as_view(), name='customers'),
    path('shopkeepers/', shopkeeper_views.ShopKeeperView.as_view(), name='shopkeepers'),
]
