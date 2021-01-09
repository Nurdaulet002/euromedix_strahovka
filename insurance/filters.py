import django_filters
from .models import Personification, Hospital,\
    Profession


# Фильтрация профессии
class ProfessionFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Profession
        fields = ['title']


# Фильтрация работников
class PersonificationFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    first_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Personification
        fields = ['last_name', 'first_name']


# Фильтрация больницы
class HospitalFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Hospital
        fields = ['title']
