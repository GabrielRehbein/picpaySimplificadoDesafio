from rest_framework.serializers import ModelSerializer
from users_picpay.models import ShopKeeper

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = ShopKeeper
        fields = '__all__'
