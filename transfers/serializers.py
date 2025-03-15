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
            raise Exception('O usuário não pode ser logista.')
        return value
    
    def validate_value(self, value):

        payer_id = self.initial_data.get("payer")
        payer = PicPayUser.objects.get(id=payer_id)
        if value > payer.balance:
            raise Exception('Saldo insuficiente.')
        return value
