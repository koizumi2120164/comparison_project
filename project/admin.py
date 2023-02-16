from django.contrib import admin

from shop.models import Category, Product
from django.contrib import admin
from import_export import fields, resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from import_export.formats import base_formats
from import_export.admin import ImportExportModelAdmin

from .models import *
class CategoryWidget(ForeignKeyWidget):
    def clean(self, value, row=None, *args, **kwargs):
        obj, created = self.model.objects.get_or_create(category=value)
        return obj

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        category = fields.Field(
        column_name='category',
        attribute='category',
        widget=CategoryWidget(Category, 'category')
    )

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        resource_class = CategoryResource
        fields = ('id', 'category', 'product_name', 'description', 'image1', 'image2','image3', 'price1','link1', 'slug', )

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['id', 'category_name', 'slug']
    prepopulated_fields = {'slug': ('category_name',)}

    resource_class = CategoryResource
    from_encoding= 'utf-8-sig'
    formats = [base_formats.XLS]

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ['product_name', 'description', 'image1','image2','image3','price1','link1','price2', 'link2','price3', 'link3','category','rating','slug', 'product_brand','is_active']
    list_filter = ['is_active']
    list_editable = ['is_active']
    prepopulated_fields = {'slug': ('product_name',)}

    resource_class = ProductResource
    from_encoding= 'utf-8-sig'
    formats = [base_formats.CSV, base_formats.XLS]

admin.site.register(Word)
admin.site.register(Review)
admin.site.register(Wishlist)
admin.site.register(Recently_viewed)