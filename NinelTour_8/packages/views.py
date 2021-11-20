from packages.serializers import PackageSerializer
from packages.models import Package
from rest_framework import viewsets
from application.views import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class PackageViewSet(viewsets.ModelViewSet):
    serializer_class = PackageSerializer
    queryset = Package.objects.all()
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch']

