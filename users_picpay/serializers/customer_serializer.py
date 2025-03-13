from rest_framework.serializers import ModelSerializer
from users_picpay.models import Customer

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['fullname', 'cpf', 'email', 'password', 'created_at', 'updated_at']
