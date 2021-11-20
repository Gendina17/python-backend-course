from packages.serializers import PackageSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from packages.models import Package
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action


class PackageViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Package.objects.all()
        serializer = PackageSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        package = get_object_or_404(Package, id=pk)
        serializer = PackageSerializer(package)
        return Response(serializer.data)

    def create(self, request):
        serializer = PackageSerializer(data=request.data)
        if serializer.is_valid():
            Package.objects.create(**serializer.data)
            return Response({"message": "Туристический пакет создан"})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        get_object_or_404(Package, id=pk)
        serializer = PackageSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            Package.objects.filter(id=pk).update(**serializer.data)
            return Response({'message': f'Туристический пакет с id = {pk} успешно изменен.'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        package = get_object_or_404(Package, id=pk)
        package.delete()
        return Response({'message': f'Туристический пакет с id = {pk} удален'})

    @action(detail=True, methods=['get'])
    def show(self, request, pk=None):
        packages = Package.objects.filter(departure_country=pk)
        if not packages:
            return Response({'error': 'Не найдено ни одного туристического пакета'}, status=404)
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data)
