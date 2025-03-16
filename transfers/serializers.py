from rest_framework.serializers import ModelSerializer
from .models import Transfer
from users_picpay.models import UserType, PicPayUser


class TransferSerializer(ModelSerializer):
    class Meta:
        model = Transfer
        fields = [
            'value',
            'payer',
            'payee', 
            'reversed_transfer', 
            'created_at', 
            'updated_at'
        ]
    
    def validate_payer(self, value):
        if value.user_type != UserType.NORMAL:
            raise Exception('O usuário pagador não pode ser logista.')
        return value
