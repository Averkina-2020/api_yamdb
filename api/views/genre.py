from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import PageNumberPagination

from ..models.genre import Genre
from ..permission import IsAdminOrReadOnly
from ..serializers.genre import GenreSerializer


class CreateGenreViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    pass


class GenreViewSet(CreateGenreViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    lookup_field = 'slug'
