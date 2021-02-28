from django.shortcuts import get_object_or_404

from rest_framework import viewsets

from api.models import Title
from api.permission import IsAuthorModeratorAdmin
from api.serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorModeratorAdmin, ]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs['title_id'])
        return title.reviews.all()

    def perform_create(self, serializer):
        get_object_or_404(Title, id=self.kwargs['post_id'])
        serializer.save(author=self.request.user, title=title)