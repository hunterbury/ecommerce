import django_filters
from .models import Product, BRAND_CHOICES, TYPE_CHOICES
from django_filters import ChoiceFilter

class ProductFilter(django_filters.FilterSet):
    brand = ChoiceFilter(field_name="brand", choices=BRAND_CHOICES, lookup_expr='icontains', label='Brand:')
    type = ChoiceFilter(field_name="type", choices=TYPE_CHOICES, lookup_expr='icontains', label='Type:')

    class Meta:
        model = Product
        fields = ['brand', 'type']