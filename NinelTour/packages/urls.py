from django.urls import path
from packages.views import index, show, create

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('<str:departure_country>/', show, name='show'),
]