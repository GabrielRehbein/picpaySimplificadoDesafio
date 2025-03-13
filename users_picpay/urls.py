from .views import customer_views, shopkeeper_views
from .views.user_view import UserPicpayView
from django.urls import path


urlpatterns = [
    path(
        'customers/',
        customer_views.CustomerListCreateAPIView.as_view(),
        name='list_create_customers'
    ),
    path(
        'customers/<int:pk>/',
        customer_views.CustomerRetrieveUpdateDestroyAPIView.as_view(),
        name='retrieve_update_destroy_customers'
    ),


    path(
        'shopkeepers/',
        shopkeeper_views.ShopKeeperListCreateAPIView.as_view(),
        name='list_create_shopkeeper'
    ),
    path(
        'shopkeepers/<int:pk>/',
        shopkeeper_views.ShopKeeperRetrieveUpdateDestroyAPIView.as_view(),
        name='retrieve_update_destroy_shopkeeper'
    ),

    path(
        '',
        UserPicpayView.as_view(),
        name='list_user'
    ),
]
