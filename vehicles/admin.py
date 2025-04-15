from django.contrib import admin
from vehicles.models import Vehicle, VehicleType

@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['license_plate', 'brand', 'model', 'color']
    search_fields = ['license_plate', 'brand', 'model']
    