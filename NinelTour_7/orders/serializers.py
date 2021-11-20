from orders.models import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data['number_rest_days'] < 2:
            raise serializers.ValidationError("Количество дней отдыха не может быть меньше двух")
        if data['number_of_tourists'] < 1:
            raise serializers.ValidationError("Количество туристов не может быть меньше одного")
        if data['price'] < 5000:
            raise serializers.ValidationError("Цена тура не может быть меньше пяти тысяч")
        return data

    class Meta:
        model = Order
        fields = "__all__"
