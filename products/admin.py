from django.contrib import admin
from .models import Category, Plant


class PlantAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'botanical_name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('friendly_name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Plant, PlantAdmin)
