from django.contrib import admin
from .models import Package


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_filter = ('id', 'tour_operator', 'airline', 'departure_country', 'hotel_name')
    list_display = ('id', 'tour_operator', 'airline', 'departure_country', 'hotel_name')
    search_fields = ("operator__startswith", "departure_country__startswith")

