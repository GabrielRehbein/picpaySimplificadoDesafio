from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transfer
from .serializers import TransferSerializer
from rest_framework.request import Request
from users_picpay.models import PicPayUser
from rest_framework import status
from decimal import Decimal
from utils.calculate import calculate_balance, reverse_transfer
from django.shortcuts import get_object_or_404
from services.transfer_auth import TransferAuthService
from utils.messages import Message
from rest_framework.generics import RetrieveAPIView

class TransferListCreateAPIView(APIView):
    
    def get(self, request: Request, format=None):
        transfers = Transfer.objects.all()
        serializer = TransferSerializer(transfers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request): 
        serializer: TransferSerializer = TransferSerializer(data=request.data)
        if serializer.is_valid():
            transfer_auth_client = TransferAuthService()
            response: dict = transfer_auth_client.authorized_transfer()
            status_response = response.get('status')
            authorization_response = response.get('authorization')
            if status_response != Message.SUCCESS and not authorization_response:
                return Response(
                    {
                        'status': status_response,
                        'authorization': authorization_response
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                    )
            data = serializer.validated_data 

            value = Decimal(data.get('value'))

            payer: PicPayUser = data.get('payer')
            
            payee: PicPayUser = data.get('payee')

            calculate_balance(payer=payer, payee=payee, value=value)

            payer.save()
            payee.save()
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {'message': 'Dados incorretos'},
            status=status.HTTP_400_BAD_REQUEST
            )

class TransferAPIView(RetrieveAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
