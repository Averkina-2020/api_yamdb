from rest_framework import serializers

from api.models import Title


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