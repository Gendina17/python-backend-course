from django.urls import path
from orders.views import index, show, create

urlpatterns = [
    path('', index, name='index'),
    path('<int:user_id>/', show, name='show'),
    path('create/', create, name='create'),
]