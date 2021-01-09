import django_filters
from .models import Harm


# Фильтрация вредности
class HarmFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
    	model =  Harm
    	fields = ['title']