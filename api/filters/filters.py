from django_filters import rest_framework as filters
from api.models.title import Title


class TitlesFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='contains')
    category = filters.CharFilter(field_name='categoryslug', lookup_expr='contains')
    genre = filters.CharFilter(field_name='genreslug', lookup_expr='contains')

    class Meta:
        model = Title
        fields = ['name', 'genre', 'category', 'year']