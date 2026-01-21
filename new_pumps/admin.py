from django.contrib import admin
from .models import Oil_Company, Pumps, Readings, Nozzles  # Exact names

@admin.register(Oil_Company)
class OilCompanyAdmin(admin.ModelAdmin):
    list_display = ['oc_name', 'oc_shorthand']

@admin.register(Pumps)
class PumpsAdmin(admin.ModelAdmin):
    list_display = ['pump_id', 'name', 'owner_name', 'address', 'city', 'get_oilcompany']
    search_fields = ['name', 'owner_name']
    
    def get_oilcompany(self, obj):
        return obj.oil_company.oc_name if obj.oil_company else '-' 
    get_oilcompany.short_description = 'Oil Company'

@admin.register(Nozzles)
class NozzlesAdmin(admin.ModelAdmin):
    list_display = ['nozzle_name', 'fuel']

@admin.register(Readings)
class ReadingsAdmin(admin.ModelAdmin):
    list_display = ['nozzleid', 'reading_date', 'reading']
