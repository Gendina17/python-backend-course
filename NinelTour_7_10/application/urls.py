from django.contrib import admin
from django.urls import path
from application.views import index
from rest_framework.routers import DefaultRouter
from orders.views import OrderViewSet
from users.views import UserViewSet
from packages.views import PackageViewSet

router = DefaultRouter()
router.register(r'api/orders', OrderViewSet, basename='orders')
router.register(r'api/users', UserViewSet, basename='users')
router.register(r'api/packages', PackageViewSet, basename='packages')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
]

urlpatterns += router.urls
