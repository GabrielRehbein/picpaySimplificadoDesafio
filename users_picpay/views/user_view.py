from rest_framework.views import View
from ..models import Customer
from ..models import ShopKeeper
from ..serializers.customer_serializer import CustomerSerializer
from ..serializers.shopkeeper_serializer import ShopKeeperSerializer
from django.http import JsonResponse


class UserPicpayView(View):
    
    def get(self, request):
        queryset_customer = Customer.objects.all()
        queryset_shopkeeper = ShopKeeper.objects.all()

        customer_serializer = CustomerSerializer(queryset_customer, many=True)
        shopkeeper_serializer = ShopKeeperSerializer(queryset_shopkeeper, many=True)
        
        return JsonResponse({
            'customers': customer_serializer.data,
            'shopkeepers': shopkeeper_serializer.data
        })
    