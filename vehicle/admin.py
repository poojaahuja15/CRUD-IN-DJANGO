from django.contrib import admin
from .models import vehicle

# Register your models here.
@admin.register(vehicle)
class vehicleAdmin(admin.ModelAdmin):
    list_display = ('id','vehicletype','modelname','vehiclecolor','enginetype')