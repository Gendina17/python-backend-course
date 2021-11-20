from django.contrib import admin
from .models import User
from orders.models import Order


class OrdersInline(admin.TabularInline):
    model = Order


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
    list_filter = ('id', 'first_name', 'last_name', 'email', 'gender')
    list_display = ('id', 'first_name', 'last_name', 'email', 'gender')
    inlines = [OrdersInline]
    search_fields = ("first_name__startswith", "last_name__startswith")

