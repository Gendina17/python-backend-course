from django.utils.decorators import method_decorator
from rest_framework import viewsets
from orders.serializers import OrderSerializer
from orders.models import Order
from application.views import login_required


@method_decorator(login_required, name='dispatch')
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    http_method_names = ['get', 'head', 'options', 'delete', 'put', 'patch']

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
