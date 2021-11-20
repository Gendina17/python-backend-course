from packages.serializers import PackageSerializer
from rest_framework import viewsets
from packages.models import Package


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
