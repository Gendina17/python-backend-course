from packages.serializers import PackageSerializer
from packages.models import Package
from application.views import UniversalViewSet


class PackageViewSet(UniversalViewSet):
    serializer_class = PackageSerializer

    def get_queryset(self):
        if self.action in ['destroy', 'update', 'partial_update']:
            return Package.objects.filter(id=self.request.user.id)
        else:
            return Package.objects.all()
