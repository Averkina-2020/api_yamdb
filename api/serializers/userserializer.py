from api.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'username',
            'role',
            'email',
            'first_name',
            'last_name',
            'bio']
        model = User
        lookup_field = 'username'
