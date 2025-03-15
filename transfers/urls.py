from .views import TransferListCreateAPIView, TransferAPIView
from django.urls import path


urlpatterns = [
    path(
        '',
        TransferListCreateAPIView.as_view(),
        name='list_create_transfer'
    ),
    path(
        '<int:pk>',
        TransferAPIView.as_view(),
        name='detail_transfer'
    ),
]
