import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    prince = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.FilterSet()

    class Meta:
        model = Product
        fields = ('name', 'description', 'prince', 'category')
