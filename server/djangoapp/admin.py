from django.contrib import admin
from .models import CarMake, CarModel


class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 3


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_type', 'year', 'car_make')
    list_filter = ['car_make', 'car_type', 'year']
    search_fields = ['name', 'car_make__name']


class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'country_of_origin')
    search_fields = ['name']
    inlines = [CarModelInline]


admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
