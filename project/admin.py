from django.contrib import admin

from shop.models import Category, Product

from django.contrib import admin

from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug']
    prepopulated_fields = {'slug': ('category_name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'description', 'image1','image2','image3','price1','link1','price2', 'link2','price3', 'link3','category','rating','slug', 'product_brand','is_active']
    list_filter = ['is_active']
    list_editable = ['is_active']
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Word)
admin.site.register(Review)
admin.site.register(Wishlist)
admin.site.register(Recently_viewed)