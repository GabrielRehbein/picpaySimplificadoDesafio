from .views import TransferListCreateView
from django.urls import path


urlpatterns = [
    path(
        'transfers/',
        TransferListCreateView.as_view(),
        name='list_create_transfer'
    ),
]