from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import PageNumberPagination

from ..models.category import Category
from ..models.genre import Genre
from ..permission import IsAdminOrReadOnly
from ..serializers.category import CategorySerializer
from ..serializers.genre import GenreSerializer


class CreateCategoryOrGenreViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    pass


class CategoryOrGenreViewSet(CreateCategoryOrGenreViewSet):
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    lookup_field = 'slug'

    def get_queryset(self):
        if self.basename == 'categories':
            return Category.objects.all()
        return Genre.objects.all()

    def get_serializer_class(self):
        if self.basename == 'categories':
            return CategorySerializer
        return GenreSerializer
