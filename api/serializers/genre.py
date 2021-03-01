from rest_framework import serializers

from api.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug',)
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        model = Genre
