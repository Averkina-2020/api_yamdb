from rest_framework import serializers

from .models import Comment, Review, Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Comment


class TitleSerializer(serializers.ModelSerializer):
    average_score = serializers.SerializerMethodField()

    class Meta:
        model = Title

    def get_average_score(self, obj):
        reviews = obj.review.all()
        total = sum(
            review.amount for review in reviews if reviews.count())
        average_score = total / reviews.count()
        return average_score
