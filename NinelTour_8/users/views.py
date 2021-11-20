from users.serializers import UserSerializer
from users.models import User
from rest_framework import viewsets
from application.views import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    http_method_names = ['get', 'head', 'options', 'delete', 'put', 'patch']

    def get_queryset(self):
        if self.action in ['destroy', 'update', 'partial_update']:
            return User.objects.filter(id=self.request.user.id)
        else:
            return User.objects.all()
