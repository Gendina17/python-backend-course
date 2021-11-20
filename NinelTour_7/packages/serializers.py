from packages.models import Package
from rest_framework import serializers
import re


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

    def validate(self, data):
        if re.fullmatch(r'^[A-Z]{2}$', data['flight_number'][:1]):
            raise serializers.ValidationError("Номер рейса должен содержать 2 заглавные буквы в начале")
        if data['departure_city'] == data['arrival_city']:
            raise serializers.ValidationError("Города вылета и назначения должны различаться")
        return data
