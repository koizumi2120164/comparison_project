from django.contrib import admin

from .models import Category, Product
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'address', 'description', 'image1','image2','image3','slug', 'conditions', 'rent_price', 'utility_fee', 'admin_fee', 'station', 'is_vacant']
    list_filter = ['is_vacant', 'is_active']
    list_editable = ['rent_price', 'utility_fee', 'admin_fee','is_vacant']
    prepopulated_fields = {'slug': ('title',)}