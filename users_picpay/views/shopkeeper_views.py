from rest_framework.views import View
from django.http import HttpResponse


class ShopKeeperView(View):

    def get(self, request):
        return HttpResponse('ok')