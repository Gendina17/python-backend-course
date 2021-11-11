from django.urls import path
from orders.views import index, show, create, update, delete

urlpatterns = [
    path('', index, name='index_orders'),
    path('<int:user_id>/', show, name='show_orders'),
    path('create/', create, name='create_order'),
    path('<int:id>/update', update, name='update_order'),
    path('<int:id>/delete', delete, name='delete_order'),
]