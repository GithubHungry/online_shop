from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'available', 'created', 'updated',)
    list_filter = ('available', 'created', 'updated',)
    list_editable = ('price', 'available',)  # if we want change attrs in list (admin)
    prepopulated_fields = {'slug': ('name',)}
