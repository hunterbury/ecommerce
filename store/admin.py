from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(ProductImage)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

    class Meta:
        model = Product