import django_filters
from django import forms
from .models import Product, BRAND_CHOICES, TYPE_CHOICES
from django_filters import ChoiceFilter, CharFilter, MultipleChoiceFilter

class ProductFilter(django_filters.FilterSet):
    brand = ChoiceFilter(field_name="brand", choices=BRAND_CHOICES, lookup_expr='icontains', label='Brand:', widget=forms.Select(attrs={'class': 'form-control'}))
    type = ChoiceFilter(field_name="type", choices=TYPE_CHOICES, lookup_expr='icontains', label='Type:', widget=forms.Select(attrs={'class': 'form-control'}))
    search = CharFilter(field_name="name", lookup_expr='icontains', label='', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ['brand', 'type', 'search']