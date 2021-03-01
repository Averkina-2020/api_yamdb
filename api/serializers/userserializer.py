from rest_framework import serializers

from api.models import TempAuth, User

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


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', )


class TempAuthRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempAuth
        fields = ['email', 'conf_code', ]
