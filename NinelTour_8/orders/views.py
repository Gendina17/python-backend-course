from orders.serializers import OrderSerializer
from orders.models import Order
from application.views import UniversalViewSet


class OrderViewSet(UniversalViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
