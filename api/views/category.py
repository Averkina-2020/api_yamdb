from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import PageNumberPagination

from ..models.category import Category
from ..permission import IsAdminOrReadOnly
from ..serializers.category import CategorySerializer


class CreateCategoryViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin,
                             mixins.ListModelMixin, viewsets.GenericViewSet):
    pass


class CategoryViewSet(CreateCategoryViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    lookup_field = 'slug'
