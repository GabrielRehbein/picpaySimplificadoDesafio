from . import views
from django.urls import path


urlpatterns = [

    path(
        '',
        views.PicPayUserListCreateAPIView.as_view(),
        name='list_create_picpay_user'
    ),
    path(
        '<int:pk>',
        views.PicPayUserRetrieveUpdateDestroyAPIView.as_view(),
        name='retrieve_update_destroy_picpay_user'
    ),
    
]
