from rest_framework import serializers
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = "__all__"
        pk_field = "id"


class UserTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ["user", "payload", "created_at", "updated_at"]
        pk = "user"
