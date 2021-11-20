from orders.serializers import OrderSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from orders.models import Order
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action


class OrderViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        order = get_object_or_404(Order, id=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            Order.objects.create(**serializer.data)
            return Response({"message": "Заказ создан"})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        get_object_or_404(Order, id=pk)
        serializer = OrderSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            Order.objects.filter(id=pk).update(**serializer.data)
            return Response({'message': f'Заказ с id = {pk} успешно изменен.'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        package = get_object_or_404(Order, id=pk)
        package.delete()
        return Response({'message': f'Заказ с id = {pk} удален'})

    @action(detail=True, methods=['get'])
    def show(self, request, pk=None):
        orders = Order.objects.filter(user_id=pk)
        if not orders:
            return Response({'error': 'Не найдено ни одного заказа для данного клиента'}, status=404)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)