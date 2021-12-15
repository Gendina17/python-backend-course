from packages.serializers import PackageSerializer
from rest_framework import viewsets
from application.celery import app
from datetime import datetime
from packages.models import Package
from django.core import serializers
from rest_framework.decorators import api_view
from .document import PackageDocument
from rest_framework.response import Response
from elasticsearch_dsl import Q


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


@api_view(('GET',))
def search_package(request):
    query = request.GET.get('key')
    q = Q('multi_match', query=query)
    search = PackageDocument.search().query(q)
    serializer = PackageSerializer(search.to_queryset(), many=True, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def search_package_v2(request):
    if request.GET == {}:
        return Response(PackageSerializer(Package.objects.all(), many=True).data)

    key, value = list(request.GET.items())[0]
    package = PackageDocument.search().query("match", **{key: value})
    serializer = PackageSerializer(package.to_queryset(), many=True, context={'request': request})
    return Response(serializer.data)


@app.task()
def package_list(b):
    with open(f'reports/package_list_{datetime.now()}.txt', 'w') as f:
        f.write(serializers.serialize('json', Package.objects.all()))
