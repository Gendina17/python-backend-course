from django.contrib import admin
from .models import Order
from users.models import User
from packages.models import Package
from django.utils.html import format_html
from django.urls import reverse


class UsersInline(admin.TabularInline):
    model = User


class PackagesInline(admin.TabularInline):
    model = Package


@admin.action(description='Пометить заказ как отмененный')
def make_cancelled(modeladmin, request, queryset):
    queryset.update(state='cancelled')


@admin.action(description='Пометить заказ как оплаченный')
def make_paid(modeladmin, request, queryset):
    queryset.update(state='paid')


@admin.register(Order)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('id', 'date_travel', 'state', 'price', 'package')
    list_display = ('id', 'date_travel', 'state', 'price', 'package', 'show_client')
    search_fields = ("user__name__startswith", "user__surname__startswith")
    actions = [make_cancelled, make_paid]

    def show_client(self, obj):
        url = reverse("show_user", kwargs={'id': obj.user_id})
        return format_html('<a href="{}">{}</a>', url, User.objects.get(id=obj.user_id))

    show_client.short_description = "Клиент"
