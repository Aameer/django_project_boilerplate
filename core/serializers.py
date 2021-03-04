from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #extra_kwargs = {'password': {'write_only': True}}
        fields = [
            'id',
            'last_login',
            "username",
            'first_name',
            'last_name',
            'email',
            'is_active'
        ]

