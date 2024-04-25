from .models import Tweet
from users.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TweetSerializer
from rest_framework.exceptions import NotFound


# Create your views here.
@api_view(["GET"])
def see_all_tweets(request):
    all_tweets = Tweet.objects.all()
    serializer = TweetSerializer(all_tweets, many=True)
    return Response(serializer.data)

@api_view(["GET",])
def see_one_room(request, user):
    try:
        user = User.objects.get(username=user)
        tweet = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(tweet, many=True)
        return Response(serializer.data)

    except User.DoesNotExist:
        raise NotFound
    
