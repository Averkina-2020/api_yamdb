from rest_framework import serializers

from api.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = '__all__'
        model = Review

    def validate(self, attrs):
        if not self.context['request'].method == 'POST':
            return attrs
        author = self.context['request'].user
        title = self.context['request'].parser_context['view'].kwargs.get(
            'title_id')
        if Review.objects.filter(title=title, author=author).exists():
            raise serializers.ValidationError(
                'Вы можете оставить только один отзыв для этого произведения'
            )
        return attrs
