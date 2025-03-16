from .views import TransferListCreateAPIView, TransferDetailAPIView
from django.urls import path


urlpatterns = [
    path(
        '',
        TransferListCreateAPIView.as_view(),
        name='list_create_transfer'
    ),
    path(
        '<int:pk>',
        TransferDetailAPIView.as_view(),
        name='detail_transfer'
    ),
]
