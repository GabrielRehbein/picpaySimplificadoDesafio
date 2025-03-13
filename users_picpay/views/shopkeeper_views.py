from rest_framework import generics
from ..models import ShopKeeper
from ..serializers.shopkeeper_serializer import ShopKeeperSerializer


class ShopKeeperListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShopKeeper.objects.all()
    serializer_class = ShopKeeperSerializer


class ShopKeeperRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShopKeeper.objects.all()
    serializer_class = ShopKeeperSerializer
