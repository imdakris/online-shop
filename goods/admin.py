from django.contrib import admin

from goods.models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    '''Methods for fine-tuning the admin panel'''
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    '''Methods for fine-tuning the admin panel'''
    prepopulated_fields = {'slug': ('name',)}

