from rest_framework.serializers import ModelSerializer
from users_picpay.models import ShopKeeper

class ShopKeeperSerializer(ModelSerializer):
    class Meta:
        model = ShopKeeper
        fields = ['fullname', 'cnpj', 'email', 'password', 'created_at', 'updated_at']
