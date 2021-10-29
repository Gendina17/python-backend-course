from django.urls import path
from users.views import index, show, create

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', show, name='show'),
    path('create/', create, name='create'),
]