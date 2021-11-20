from django.contrib import admin
from .models import Order
from users.models import User
from packages.models import Package


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
    list_display = ('id', 'date_travel', 'state', 'price', 'package')
    search_fields = ("user__name__startswith", "user__surname__startswith")
    actions = [make_cancelled, make_paid]

