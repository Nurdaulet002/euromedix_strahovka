import django_filters
from .models import Service, Harm


# Фильтрация работников
class ServiceFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    code = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Service
        fields = ['title', 'code']


# Фильтрация вредности
class HarmFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
    	model =  Harm
    	fields = ['title']
