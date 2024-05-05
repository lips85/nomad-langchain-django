from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "first_name",
            "last_name",
            "groups",
            "name",
            "user_permissions",
        )
