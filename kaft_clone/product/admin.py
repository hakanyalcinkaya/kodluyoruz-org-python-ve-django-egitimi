from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'slug',
        'gender',
        'status', 
        'updated_at',
    )
    list_filter = ('status', 'gender', )
    list_editable = (
        'title',
        'status', 
    )



class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'cover_image',
        'price',
        'stock',
        'slug',
        'is_home',
        'status', 
        'updated_at',
    )
    list_filter = ('status', )
    list_editable = (
        'title',
        'is_home',
        'status', 
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)