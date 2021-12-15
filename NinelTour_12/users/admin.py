from django.contrib import admin
from .models import User
from orders.models import Order
from django.utils.html import format_html
from django.urls import reverse


class OrdersInline(admin.TabularInline):
    model = Order


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
    list_filter = ('id', 'first_name', 'last_name', 'email', 'gender')
    list_display = ('id', 'first_name', 'last_name', 'email', 'gender', 'show_orders')
    inlines = [OrdersInline]
    search_fields = ("first_name__startswith", "last_name__startswith")

    def show_orders(self, obj):
        count = len(Order.objects.filter(user_id=obj.id))
        url = reverse("show_orders", kwargs={'user_id': obj.id})
        return format_html('<a href="{}">{}</a>', url, count)

    show_orders.short_description = "Количество заказов"
