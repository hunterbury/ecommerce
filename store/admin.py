from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(ProductImage)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Category)


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

class CategoryAdmin(admin.StackedInline):
    model = Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin, CategoryAdmin]

    class Meta:
        model = Product