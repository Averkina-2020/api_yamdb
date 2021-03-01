from api.models import Genre

from rest_framework import serializers


class GenreSerializer(serializers.ModelSerializer):
    # slug = serializers.SlugRelatedField(
    #   validators=[validators.UniqueValidator(
    #      queryset=Genre.objects.all())],
    # )

    class Meta:
        fields = ('name', 'slug',)
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        model = Genre
