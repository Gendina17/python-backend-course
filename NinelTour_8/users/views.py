from users.serializers import UserSerializer
from users.models import User
from application.views import UniversalViewSet


class UserViewSet(UniversalViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.action in ['destroy', 'update', 'partial_update']:
            return User.objects.filter(id=self.request.user.id)
        else:
            return User.objects.all()
