from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated,
)

from .models import Review, Title
from .serializers import (
    CommentSerializer,
    ReviewSerializer,
)


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs['title_id'])
        return title.reviews.all()

    def perform_create(self, serializer):
        get_object_or_404(Title, id=self.kwargs['post_id'])
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]  # IsAuthorOrReadOnly
    serializer_class = CommentSerializer

    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs['review_id'])
        return review.comments.all()

    def perform_create(self, serializer):
        get_object_or_404(Review, id=self.kwargs['review_id'])
        serializer.save(author=self.request.user)
