from django.urls import path
from users.views import index, show, create, update, delete

urlpatterns = [
    path('', index, name='index_users'),
    path('<int:id>/', show, name='show_user'),
    path('create/', create, name='create_user'),
    path('<int:id>/update', update, name='update_user'),
    path('<int:id>/delete', delete, name='delete_user'),
]