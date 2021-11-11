from django.urls import path
from packages.views import index, show, create, update, delete

urlpatterns = [
    path('', index, name='index_packages'),
    path('create/', create, name='create_package'),
    path('<str:departure_country>/', show, name='show_package'),
    path('<int:id>/update', update, name='update_package'),
    path('<int:id>/delete', delete, name='delete_package'),
]