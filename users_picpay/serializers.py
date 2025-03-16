from rest_framework.serializers import ModelSerializer
from users_picpay.models import PicPayUser

class PicPayUserSerializer(ModelSerializer):
    class Meta:
        model = PicPayUser
        fields = [
            'id',
            'fullname',
            'user_type',
            'document',
            'email',
            'password',
            'created_at',
            'updated_at'
        ]
