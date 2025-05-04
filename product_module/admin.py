from django.contrib import admin
from product_module.models import Product, ProductComment, ProductCategories, ProductCategoriesMain


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'inventory', 'price')


@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'success', 'user', 'parent')


@admin.register(ProductCategories)
class ProductCategoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')


@admin.register(ProductCategoriesMain)
class ProductCategoriesMainAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
