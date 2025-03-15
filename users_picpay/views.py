from rest_framework import generics
from rest_framework.views import APIView
from .models import PicPayUser
from .serializers import PicPayUserSerializer
from rest_framework.request import Request
from utils.calculate import reverse_transfer
from decimal import Decimal

class PicPayUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = PicPayUser.objects.all()
    serializer_class = PicPayUserSerializer



class PicPayUserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PicPayUser.objects.all()
    serializer_class = PicPayUserSerializer

