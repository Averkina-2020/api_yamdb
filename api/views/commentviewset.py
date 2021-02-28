from api.models import Review
from api.permission import IsAuthorModeratorAdmin
from api.serializers import CommentSerializer

from django.shortcuts import get_object_or_404

from rest_framework import viewsets


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorModeratorAdmin, ]
    serializer_class = CommentSerializer

    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs['review_id'])
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            id=self.kwargs['review_id'],
            title__id=self.kwargs['title_id']
        )
        serializer.save(author=self.request.user, review=review)
