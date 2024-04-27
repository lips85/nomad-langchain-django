from rest_framework import serializers
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = [
            "id",
            "payload",
            "user",
            "created_at",
            "updated_at",
        ]
        pk_field = "id"
