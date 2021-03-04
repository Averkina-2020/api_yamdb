from api.models import Category

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug',)
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        model = Category
