from packages.serializers import PackageSerializer
from rest_framework import viewsets
from application.celery import app
from datetime import datetime
from packages.models import Package
from django.core import serializers


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


@app.task()
def package_list(b):
    with open(f'reports/package_list_{datetime.now()}.txt', 'w') as f:
        f.write(serializers.serialize('json', Package.objects.all()))
