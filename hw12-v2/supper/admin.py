from django.contrib import admin
from supper.models import FunnyWord


@admin.register(FunnyWord)
class FunnyWordAdmin(admin.ModelAdmin):
    list_filter = ('id', 'word')
    list_display = ('id', 'word')

