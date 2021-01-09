from rest_framework import serializers
from ..models import Region


# Сериализация региона
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'title']
