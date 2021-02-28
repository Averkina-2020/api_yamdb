from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import SAFE_METHODS

from api.models import Title
from api.permission import IsAdminOrReadOnly
from api.serializers import TitleSerializer
from api.filters import TitlesFilter


class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = TitleSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    pagination_class = PageNumberPagination
    queryset = Title.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitlesFilter

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return TitleSerializer
