from django.contrib import admin
from django.urls import path, include
from application.views import index, login
from rest_framework.routers import DefaultRouter
from orders.views import OrderViewSet
from users.views import UserViewSet
from packages.views import PackageViewSet
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'api/orders', OrderViewSet, basename='orders')
router.register(r'api/users', UserViewSet, basename='users')
router.register(r'api/packages', PackageViewSet, basename='packages')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social_auth/', include('social_django.urls', namespace='social'))
]

urlpatterns += router.urls
