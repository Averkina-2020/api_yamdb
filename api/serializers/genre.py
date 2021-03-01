from rest_framework import serializers

from api.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    #slug = serializers.SlugRelatedField(
     #   validators=[validators.UniqueValidator(
      #      queryset=Genre.objects.all())],
    #)

    class Meta:
        fields = ('name', 'slug',)
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        model = Genre
