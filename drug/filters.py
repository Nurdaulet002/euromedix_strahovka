import django_filters
from .models import Drug


# Фильтрация работников
class DrugFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    code = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Drug
        fields = ['title', 'code']
