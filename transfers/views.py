from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transfer
from .serializers import TransferSerializer
from rest_framework.request import Request
from users_picpay.models import Customer, ShopKeeper
from rest_framework import status
from decimal import Decimal
from utils.calculate import calculate_balance

class TransferListCreateView(APIView):
    
    def get(self, request: Request, format=None):
        transfers = Transfer.objects.all()
        serializer = TransferSerializer(transfers, many=True)
        return Response(serializer.data)

    def post(self, request: Request): 
        serializer = TransferSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            value = Decimal(data.get('value'))

            customer: Customer = data.get('payer')

            if customer.balance < value:
                return Response(
                    {'message': 'Saldo insuficiente'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            shopkeeper: ShopKeeper = data.get('payee')

            calculate_balance(customer, shopkeeper, value)
            shopkeeper.save()
            customer.save()
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {'message': 'Dados errados'},
            status=status.HTTP_400_BAD_REQUEST
            )
