from django.urls import path
from users.views import index, show, create

urlpatterns = [
    path('', index, name='index_users'),
    path('<int:id>/', show, name='show_user'),
    path('create/', create, name='create'),
]