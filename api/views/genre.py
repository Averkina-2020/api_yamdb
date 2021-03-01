from rest_framework import viewsets, filters, mixins
from rest_framework.pagination import PageNumberPagination

from ..models.genre import Genre
from ..serializers.genre import GenreSerializer
from ..permission import IsAdminOrReadOnly


class CreateGenreViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin,
                            mixins.ListModelMixin, viewsets.GenericViewSet):
    pass


class GenreViewSet(CreateGenreViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    lookup_field = 'slug'
